import mitreattack.attackToExcel.attackToExcel as attackToExcel
import mitreattack.attackToExcel.stixToDf as stixToDf


def update():
    attackdata = attackToExcel.get_stix_data("enterprise-attack")
    techniques_data = stixToDf.techniquesToDf(attackdata, "enterprise-attack")
    tactics_data = stixToDf.tacticsToDf(attackdata, "enerprise-attack")
    groups_data = stixToDf.groupsToDf(attackdata, "enterprise-attack")
    software_data = stixToDf.softwareToDf(attackdata, "enterprise-attack")
    mitigations_data = stixToDf.mitigationsToDf(attackdata, "enterprise-attack")
    relationship_data = stixToDf.relationshipsToDf(attackdata)

    techniques_df = techniques_data["techniques"]
    tactics_df = tactics_data["tactics"]
    groups_df = groups_data["groups"]
    software_df = software_data["software"]
    mitigations_df = mitigations_data["mitigations"]
    relationship_df = relationship_data["relationships"]

    relationship_df.columns = [column.replace(" ", "_") for column in relationship_df.columns]
    groupsFromRelationships = relationship_df.query("source_type == 'group'")

    techniques_df.to_csv("APTAnalyzer/data/techniques.csv", index=False)
    tactics_df.to_csv("APTAnalyzer/data/tactics.csv", index=False)
    groups_df.to_csv("APTAnalyzer/data/groups.csv", index=False)
    software_df.to_csv("APTAnalyzer/data/software.csv", index=False)
    mitigations_df.to_csv("APTAnalyzer/data/mitigations.csv", index=False)
    groupsFromRelationships.to_csv("APTAnalyzer/data/groupsFromRelationships.csv", index=False)
    relationship_df.to_csv("APTAnalyzer/data/relationships.csv", index=False)

def buildDataFrames():
    techniques_df = pd.read_csv("APTAnalyzer/data/techniques.csv")
    tactics_df = pd.read_csv("APTAnalyzer/data/tactics.csv")
    groups_df = pd.read_csv("APTAnalyzer/data/groups.csv")
    software_df = pd.read_csv("APTAnalyzer/data/software.csv")
    mitigations_df = pd.read_csv("APTAnalyzer/data/mitigations.csv")
    groupsFromRelationships = pd.read_csv("APTAnalyzer/data/groupsFromRelationships.csv")
    relationships_df = pd.read_csv("APTAnalyzer/data/relationships.csv")

    return {"techniques": techniques_df, "tactics": tactics_df, "groups": groups_df, "software": software_df, "mitigations": mitigations_df, "groupsFromRelationships": groupsFromRelationships, "relationships": relationships_df}