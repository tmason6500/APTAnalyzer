
import mitreattack.attackToExcel.attackToExcel as attackToExcel
import mitreattack.attackToExcel.stixToDf as stixToDf
import pandas as pd
from IPython.display import HTML
import re
from string import punctuation


attackdata = attackToExcel.get_stix_data("enterprise-attack")
techniques_data = stixToDf.techniquesToDf(attackdata, "enterprise-attack")
df_techniques = techniques_data["techniques"]
df_techniques.columns = [column.replace(" ", "_") for column in df_techniques.columns]






def build_new_descriptions(descript):
    #for descript in df.description:
        sanitized_descript=remove_citation(descript)
        APT_HTTP_LIST = find_APT_HTTP(descript)
        sanitized_descript = remove_APT_HTTP(sanitized_descript)
        #Check for the marker, find the 
        #replace {...} with the hyperlinked name
        for apt_http_entry in APT_HTTP_LIST:
             clickable_entry = (make_clickable(apt_http_entry[0], apt_http_entry[1]))
             
             sanitized_descript=sanitized_descript.replace("ADDED_ENTRY", clickable_entry, 1)
        #df.description = df.description.replace([descript],sanitized_descript)
        print(sanitized_descript)
       # HTML(df.to_html(escape=False))
        #return df
    
    #for x in df['description']:
    #    print(x

def make_clickable(text: str, link: str) -> str:
    print( '<a href="{}">{}</a>'.format(link, text))
    return ('<a href="{}">{}</a>'.format(link, text))

    
def remove_APT_HTTP(text):
    text=re.sub(r"\[(.*?)\]\(https?://[^()]*\)", "ADDED_ENTRY", text)
    return text
    
def find_APT_HTTP(text):
    text=re.findall(f"\[(.*?)\]\((https?://[^()]*)\)",  text)
    return text


def remove_hyperlinks(text):
    text = re.sub(r"\(https?://[^()]*\)", "", text)
    return text

def find_hyperlinks(text):
    text = re.findall(r"\((https?://[^()]*)\)", text)
    return text

def remove_brackets(text):
    text = re.sub(r"\[(.*?)\]", "", text)
    return text

def find_brackets(text):
    text = re.findall(r"\[(.*?)\]", text)
    return text

def remove_citation(text):
    text = re.sub(r"\(Citation:+ [^()]*\)", "", text)
    return text

def remove_tabs_line_breaks_spaces(text):
    text = " ".join(text.split())
    return text

def remove_punctuation(text):
    text = re.sub(f"[{re.escape(punctuation)}]", "", text)
    return text


if __name__ == "__main__":

    debug = True
    if  debug == True:
         text = "Adversaries may use SID-History Injection to escalate privileges and bypass access controls. The Windows security identifier (SID) is a unique value that identifies a user or group account. SIDs are used by Windows security in both security descriptors and access tokens. (Citation: Microsoft SID) An account can hold additional SIDs in the SID-History Active Directory attribute (Citation: Microsoft SID-History Attribute), allowing inter-operable account migration between domains (e.g., all values in SID-History are included in access tokens). With Domain Administrator (or equivalent) rights, harvested or well-known SID values (Citation: Microsoft Well Known SIDs Jun 2017) may be inserted into SID-History to enable impersonation of arbitrary users/groups such as Enterprise Administrators. This manipulation may result in elevated access to local resources and/or access to otherwise inaccessible domains via lateral movement techniques such as [Remote Services](https://attack.mitre.org/techniques/T1021), [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002), or [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006)."
    
    build_new_descriptions(text)