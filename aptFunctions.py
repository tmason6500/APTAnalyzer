import mitreattack.attackToExcel.attackToExcel as attackToExcel
import mitreattack.attackToExcel.stixToDf as stixToDf
import pandas as pd


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
    df_techniques = pd.read_csv("data/techniques.csv")
    df_tactics = pd.read_csv("data/tactics.csv")
    df_groups = pd.read_csv("data/groups.csv")
    df_software = pd.read_csv("data/software.csv")
    df_mitigations = pd.read_csv("data/mitigations.csv")
    df_gfr = pd.read_csv("data/df_gfr.csv")
    df_relationships = pd.read_csv("data/relationships.csv")

    return df_techniques, df_tactics, df_groups, df_software, df_mitigations, df_gfr, df_relationships

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

def filterForSelectedTechniques(df: pd.DataFrame, techniqueList: list) -> pd.DataFrame:
    """
    Returns a dataframe groups that use the each of the techniques in 
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
        percentages[group] = (groupList.count(group) / techniqueCount)
    
    # Return the dictionary
    return percentages

def getDescription(df: pd.DataFrame, name: str) -> str:
    """
    Returns the description of the group, technique, or software
    from the associated dataframe.
 """
       
    return df[df.name == name].description.values[0]