from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox
from PyQt5 import uic
import sys
from pyattck import Attck
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont

attack = Attck()

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

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui File
        uic.loadUi("GUI.ui", self)
        self.model = QStandardItemModel()


        #Define our QtWidgets
        self.tactics = self.findChild(QComboBox, "Tactics")
        self.techniques = self.findChild(QComboBox, "Techniques")
        self.software = self.findChild(QComboBox, "Software")
        self.tactics.setModel(self.model)
        self.techniques.setModel(self.model)

        self.software.addItems(malwares)

        for k, v in tactics.items():
            state = QStandardItem(k)
            self.model.appendRow(state)
            for value in v:
                city = QStandardItem(value)
                state.appendRow(city)

        self.tactics.currentIndexChanged.connect(self.updateStateCombo)
        self.updateStateCombo(0)

        self.show()

    def updateStateCombo(self, index):
        indx = self.model.index(index, 0, self.tactics.rootModelIndex())
        self.techniques.setRootModelIndex(indx)
        self.techniques.setCurrentIndex(0)





#Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
