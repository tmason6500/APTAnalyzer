from pyattck import Attck
import json

attack = Attck()

#Test cases
techniquesid_list = ['T1221', 'S0161'] #test case 1
#techniquesid_list = ['S0496', 'T1059.001', 'T1113'] #test case 2 

#Also test case with Group DarkHydrus
'''for actor in attack.enterprise.actors:
     if 'DarkHydrus' in actor.name:
         for technique in actor.techniques:
             # print (technique.id)
              techniquesid_list.append(technique.id)'''

print ("These techniques and software were inputted: " + str(techniquesid_list))

attackers = {}

#Instead of updating the dictionary everytime this code is run, DictionaryCreate.py helps speed up the process by creating a file
#That file can be updated periodically as needed
'''temp = []
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
                    attackers[malware.id] = temp'''

#opens the data.json file created using DictionaryCreate.py
with open('data.json') as d:
     #enters the contents of the data.json file into dictionary attackers
    attackers = json.load(d)

list2=[]
counter=0
#Compares test case with contents of the dictionary
#Adds groupname to list2 if technique/software from test case match with dictionary key
for x in techniquesid_list:
     if (counter == 0):
          list2 = attackers[x]
     else:
          list1= list2
          list2 = attackers[x]
          list2 = list(set(list1).intersection(list2))
     counter+=1

print ("Based on these techniques, these group(s) were possible threat actors: " + str(list2))

