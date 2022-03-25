from pyattck import Attck
import json

attack = Attck()

backend_list = []
tactics = {}
malwares = []

for tactic in attack.enterprise.tactics:
         for technique in tactic.techniques:
              if tactic.name not in tactics.keys():
                  tactics[tactic.name] = [technique.name]
              else:
                  temp = tactics[tactic.name]
                  temp.append(technique.name)
                  tactics[tactic.name] = temp

for malware in attack.enterprise.malwares:
    malwares.append(malware.name)

a_file = open("tacticscombo.json", "w")
json.dump(tactics, a_file)
a_file.close()

b_file = open("software.json", "w")
json.dump(malwares, b_file)
b_file.close()
