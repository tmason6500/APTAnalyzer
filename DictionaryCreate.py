from pyattck import Attck
import json 

attack = Attck()


attackers = {}
temp = []
for technique in attack.enterprise.techniques:
          for actor in technique.actors:
               if technique.id not in attackers.keys():
                    attackers[technique.id] = [actor.name]
               else:
                    temp = attackers[technique.id]
                    temp.append(actor.name)
                    attackers[technique.id] = temp


for technique in attack.enterprise.techniques:
     for subtechnique in technique.subtechniques:
          for actor in subtechnique.actors:
               if subtechnique.id not in attackers.keys():
                    attackers[subtechnique.id] = [actor.name]
               else:
                    temp = attackers[subtechnique.id]
                    temp.append(actor.name)
                    attackers[subtechnique.id] = temp

for malware in attack.enterprise.malwares:
          for actor in malware.actors:
               if malware.id not in attackers.keys():
                    attackers[malware.id] = [actor.name]
               else:
                    temp = attackers[malware.id]
                    temp.append(actor.name)
                    attackers[malware.id] = temp


a_file = open("data.json", "w")
json.dump(attackers, a_file)
a_file.close()

a_file = open("data.json", "r")
output = a_file.read()
print(output)
