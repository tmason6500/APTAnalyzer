import mitreattack.attackToExcel.attackToExcel as attackToExcel
import mitreattack.attackToExcel.stixToDf as stixToDf
import pandas as pd
import os
import math
import re
from IPython.display import HTML
#added imports from Thomas
from collections import Counter
import itertools

def updateDataFrameSources() -> None:
    """
    Update the sources of the dataframes
    """
    # Get MemoryStore from Mitre
    attackdata = attackToExcel.get_stix_data("enterprise-attack")

    # Get data from MemoryStore for each dataframe
    techniques_data = stixToDf.techniquesToDf(attackdata, "enterprise-attack")
    tactics_data = stixToDf.tacticsToDf(attackdata, "enerprise-attack")
    groups_data = stixToDf.groupsToDf(attackdata, "enterprise-attack")
    software_data = stixToDf.softwareToDf(attackdata, "enterprise-attack")
    mitigations_data = stixToDf.mitigationsToDf(attackdata, "enterprise-attack")
    relationship_data = stixToDf.relationshipsToDf(attackdata)

    # Convert data file to dataframe
    df_techniques = techniques_data["techniques"]
    df_tactics = tactics_data["tactics"]
    df_groups = groups_data["groups"]
    df_software = software_data["software"]
    df_mitigations = mitigations_data["mitigations"]
    df_relationships = relationship_data["relationships"]

    """
    Transform dataframes to usuable state
    """

    # Remove spaces from column names
    df_relationships.columns = [column.replace(" ", "_") for column in df_relationships.columns]

    # Rename columns for transforms
    df_relationships.rename(columns={'target_ID': 'technique_ID'}, inplace=True)
    df_relationships.rename(columns={'target_name': 'technique_name'}, inplace=True)
    df_techniques.rename(columns={'ID': 'technique_ID'}, inplace=True)
    df_techniques.rename(columns={'name': 'technique_name'}, inplace=True)

    # Synchronize technique names across required dataframes
    df_relationships.set_index('technique_ID', inplace=True)
    df_relationships.update(df_techniques.set_index('technique_ID'))
    df_relationships.reset_index(inplace=True)

    # Revert column names
    df_relationships.rename(columns={'technique_ID': 'target_ID'}, inplace=True)
    df_relationships.rename(columns={'technique_name': 'target_name'}, inplace=True)
    df_techniques.rename(columns={'technique_ID': 'ID'}, inplace=True)
    df_techniques.rename(columns={'technique_name': 'name'}, inplace=True)

    # Filter for required subset of relationship dataframe
    df_gfr = df_relationships.query("source_type == 'group'")

    # Store dataframes as csv(s)
    df_techniques.to_csv("data/techniques.csv", index=False)
    df_tactics.to_csv("data/tactics.csv", index=False)
    df_groups.to_csv("data/groups.csv", index=False)
    df_software.to_csv("data/software.csv", index=False)
    df_mitigations.to_csv("data/mitigations.csv", index=False)
    df_gfr.to_csv("data/df_gfr.csv", index=False)
    df_relationships.to_csv("data/relationships.csv", index=False)

def buildDataFrames() -> pd.DataFrame:
    """
    Build dataframes from csv(s)
    """
    try:
        df_techniques = pd.read_csv("data/techniques.csv")
        df_techniques = build_new_descriptions(df_techniques)
        df_tactics = pd.read_csv("data/tactics.csv")
        df_tactics = build_new_descriptions(df_tactics)
        df_groups = pd.read_csv("data/groups.csv")
        df_groups = build_new_descriptions(df_groups)
        df_software = pd.read_csv("data/software.csv")
        df_software = build_new_descriptions(df_software)
        df_mitigations = pd.read_csv("data/mitigations.csv")
        df_mitigations = build_new_descriptions(df_mitigations)
        df_gfr = pd.read_csv("data/df_gfr.csv")
        # df_gfr = build_new_descriptions(df_gfr)
        df_relationships = pd.read_csv("data/relationships.csv")
        # df_relationships = build_new_descriptions(df_relationships)

        return df_techniques, df_tactics, df_groups, df_software, df_mitigations, df_gfr, df_relationships
    except FileNotFoundError:
        try:
            os.makedirs("data")
            updateDataFrameSources()
            return buildDataFrames()
        except FileExistsError:
            updateDataFrameSources()
            return buildDataFrames()

def getTechniquesByTactic(tactics: pd.DataFrame, techniques: pd.DataFrame) -> dict:
    """
    Returns a dictionary of all techniques grouped by tactic.
    """
    tacticsList = tactics.name.tolist()
    techniques_by_tactic = {}
    for tactic in tacticsList:
        techniques_by_tactic[tactic] = techniques[techniques.tactics.str.contains('{}'.format(tactic))].name
    return techniques_by_tactic

def getSoftwareList(software: pd.DataFrame) -> list:
    """
    Returns a list of all software names.
    """
    return software.name.tolist()

def getTechniqueList(technique: pd.DataFrame) -> list:
    return technique.name.tolist()

def filterForSelectedTechniques(df: pd.DataFrame, techniqueList: list) -> pd.DataFrame:
    """
    Returns a dataframe ofgroups that use the each of the techniques in
    the techniqueList.
    """
    # Create empty dataframe
    filtered = pd.DataFrame()

    # Iterate through techniques in techniqueList
    for technique in techniqueList:

        # Filter for groups that use the technique
        filtered = pd.concat([df[df.target_name == technique], filtered])

    # Return filtered dataframe
    return filtered

def analyzeResults(df: pd.DataFrame, techniqueList: list) -> dict:
    """
    Returns a dictionary of the groups (key) and the percentage of the
    techniques in the techniqueList they use (value).
    """
    # create empty dictionary
    percentages = {}

    # count the number of techniques in the techniqueList
    techniqueCount = len(techniqueList)

    # create a list of all groups in the dataframe
    groupList = df.source_ID.tolist()

    # Iterate through groups in groupList
    for group in groupList:

        # Calculate the percentage of techniques each group matched
        percentages[group] = math.ceil((groupList.count(group) / techniqueCount) * 100)

    # Return the dictionary
    return percentages

def getIDByName(df: pd.DataFrame, name: str) -> int:
    """
    Returns the ID of a row in a dataframe.
    """
    return df[df.name == name].ID.tolist()[0]

def getDescriptionByName(df: pd.DataFrame, name: str) -> str:
    """
    Returns the description from the associated dataframe
    based on the name.
    """
    return df[df.name == name].description.values[0]

def getDescriptionByID(df: pd.DataFrame, ID: str) -> str:
    """
    Returns the description from the associated dataframe
    based on the ID.
    """
    return df[df.ID == ID].description.values[0]

def getData(df: pd.DataFrame, ID: str, col: str) -> str:
    """
    Returns the data from the specified column in the specified dataframe
    """
    return df[df.ID == ID].iloc[0][col]

def getTechniquesByGroup(df: pd.DataFrame, GroupID: str) -> list:
    '''
    Return a list of all techniques used by a particular group
    '''
    return df[(df.source_ID == GroupID)& (df.target_type == 'technique')].target_ID.tolist()

def getSofwareByGroup(df: pd.DataFrame, GroupID: str) -> list:
    '''
    Return a list of all software used by a particular group
    '''
    return df[(df.source_ID == GroupID) & (df.target_type == 'software')].target_ID.tolist()

def mitigationsByTechnique(df: pd.DataFrame, TechniqueID: str) -> list:
    '''
    Return a list of all mitigations used by a particular technique
    '''
    return df[(df.target_ID == TechniqueID) & (df.source_type == 'mitigation')].source_ID.tolist()

######################################################################################
## Thomas's added code
######################################################################################

def get_dictionary(df):
    """
    Return a dictionary of with techniques and software associated with their ids
    """
    dictionary={}

    for target_name, target_id in zip(df.target_name, df.target_ID):
            target_name.strip()
            dictionary[target_name] = target_id
    return dictionary

def get_groups_by_ID(df, IDs: list):
    """
    Gets Groups based on their ID
    """
    groups = []
    groupList = []
    for ID in IDs:
        groups = df[df.target_ID == ID]
        tempGrouplist=groups.source_ID.tolist()
        #Chains all the lists returned by each ID in groups
        groupList = list(itertools.chain(groupList,tempGrouplist))
    return groupList

def get_possible_selection(itemDict,selection,groupsFromRelationships,percentage_num):
    IDs = []
    #returns the ID associated with each technique/software selected and appends it to array IDs
    for x in selection:
        try:
            itemID = itemDict[x]
            IDs.append(itemID)
        except:
            pass
   #get the group ID associated with each ID
    groups = get_groups_by_ID(groupsFromRelationships,IDs)

    #removes duplicate ids from the array groups
    set_groups = set(groups)
    #creates a variable that store the number of occurences of each item
    groupCount = Counter(groups)
    #variable to add up the number of selections that exceed 50%
    possibleSelections = 0
    #unneeded variable but it store the groups that exceed 50% at any given point
    selectedGroups = []
    for group in set_groups:
        num = groupCount[group]
        decimal_num = percentage_num/100
        if (num/len(selection) >= decimal_num):
            possibleSelections += 1
            selectedGroups.append(group)
        else:
            pass
    return(possibleSelections)

def update_num(groupsFromRelationships, selection, num):
    debug = False
    #debug to put a manual selection of tactics and/or Techniques
    if debug == True:
        selection = [ "BISCUIT", "External Remote Services","Malware"]
    else:
        pass
    itemDict = get_dictionary(groupsFromRelationships)
    return(get_possible_selection(itemDict, selection, groupsFromRelationships,num))

####################################
#Sanatization functions from Thomas
####################################

#main function for removing names in discriptions and replacing it with hyperlinked name
def build_new_descriptions(df):
    for descript in df.description:
        sanitized_descript=remove_citation(descript)
        APT_HTTP_LIST = find_APT_HTTP(descript)
        sanitized_descript = remove_APT_HTTP(sanitized_descript)
        #Check for the marker, find the 
        #replace {...} with the hyperlinked name
        for apt_http_entry in APT_HTTP_LIST:
             clickable_entry = (make_clickable(apt_http_entry[0], apt_http_entry[1]))
             
             sanitized_descript=sanitized_descript.replace("ADDED_ENTRY", clickable_entry, 1)
        df.description = df.description.replace([descript],sanitized_descript)
    HTML(df.to_html(escape=False))
    return df

#remove citations
def remove_citation(text):
    text = re.sub(r"\(Citation:+ [^()]*\)", "", text)
    return text
    
#removes [name](link)
def remove_APT_HTTP(text):
    text=re.sub(r"\[(.*?)\]\(https?://[^()]*\)", "ADDED_ENTRY", text)
    return text

#finds [name](link)
def find_APT_HTTP(text):
    text=re.findall(f"\[(.*?)\]\((https?://[^()]*)\)",  text)
    return text

#makes a http link clickable
def make_clickable(text: str, link: str) -> str:
    return ('[<a href="{}">{}</a>]'.format(link, text))

def fix_pdf_description(text: str)-> str:
    text = re.sub(r'\<a href=\"https?://[^()]*?>', '', text)
    text = re.sub(r"</a>", '', text)

    return text