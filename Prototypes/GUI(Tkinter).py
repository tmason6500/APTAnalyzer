from tkinter import *
from pyattck import Attck
attack = Attck()

techniques = {}
temp = []
for tactic in attack.enterprise.tactics:
          for technique in tactic.techniques:
              if technique.subtechnique:
                  continue
              else:
                  if tactic.name not in techniques.keys():
                      techniques[tactic.name] = [technique.name]
                  else:
                      temp = techniques[tactic.name]
                      temp.append(technique.name)
                      techniques[tactic.name] = temp

#dict_of_key_length_pairs = {len(v) for k, v in techniques.items()}

root = Tk()

btn_dict = {}
row = 0
i = 0
for key, value in techniques.items():
    # pass each button's text to a function
    # create the buttons and assign to animal:button-object dict pair
    btn_dict[key] = Menubutton(root, text=key, width = 30, relief=RAISED)
    btn_dict[key].grid(row=row, column=1,pady=3)
    row += 1


# run the GUI event loop
root.mainloop()
