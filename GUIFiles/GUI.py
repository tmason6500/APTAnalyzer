from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QPushButton, QPlainTextEdit, QCompleter, QListWidget
from PyQt5 import uic
from PyQt5 import Qt
import sys
import json
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont

with open('tacticscombo.json') as d:
     #enters the contents of the data.json file into dictionary attackers
    TacticCombo = json.load(d)

with open('software.json') as d:
     #enters the contents of the data.json file into dictionary attackers
    Malware = json.load(d)

Backend_list = []

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui File
        uic.loadUi("GUI.ui", self)
        self.setStyleSheet("background-color: #33393B; color : white; font-size : 11pt;}")

        self.model = QStandardItemModel()

        #Define our QtWidgets
        self.tactics = self.findChild(QComboBox, "Tactics")
        self.tactics.setEditable(True)
        self.tactics.setStyleSheet('QComboBox {background-color: #282C2E; color: white; font-size : 11pt;}')
        self.tactics.setInsertPolicy(QComboBox.NoInsert)
        self.tactics.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.techniques = self.findChild(QComboBox, "Techniques")
        self.techniques.setEditable(True)
        self.techniques.setStyleSheet('QComboBox {background-color: #282C2E; color: white; font-size : 11pt;}')
        self.techniques.setInsertPolicy(QComboBox.NoInsert)
        self.techniques.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.software = self.findChild(QComboBox, "Software")
        self.software.setEditable(True)
        self.software.setStyleSheet('QComboBox {background-color: #282C2E; color: white; font-size : 11pt;}')
        self.software.setInsertPolicy(QComboBox.NoInsert)
        self.software.completer().setCompletionMode(QCompleter.PopupCompletion)

        self.add_technique_btn = self.findChild(QPushButton, "AddTechnique")
        self.add_technique_btn.setStyleSheet('QPushButton {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.add_software_btn = self.findChild(QPushButton, "AddSoftware")
        self.add_software_btn.setStyleSheet('QPushButton {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.delete_technique_btn = self.findChild(QPushButton, "DeleteTechnique")
        self.delete_technique_btn.setStyleSheet('QPushButton {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.delete_software_btn = self.findChild(QPushButton, "DeleteSoftware")
        self.delete_software_btn.setStyleSheet('QPushButton {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.clear_all_btn = self.findChild(QPushButton, "ClearAll")
        self.clear_all_btn.setStyleSheet('QPushButton {background-color: #282C2E; color: white; font-size : 12pt;}')

        self.added_techniques_box = self.findChild(QListWidget, "AddedTechniquesBox")
        self.added_techniques_box.setStyleSheet('QListWidget {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.added_software_box = self.findChild(QListWidget, "AddedSoftwareBox")
        self.added_software_box.setStyleSheet('QListWidget {background-color: #282C2E; color: white; font-size : 12pt;}')

        self.description_box = self.findChild(QPlainTextEdit, "DescriptionBox")
        self.description_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.description_box.setReadOnly(True)
        self.added_techniques_text = self.findChild(QPlainTextEdit, "AddedTechniquesText")
        self.added_techniques_text.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.added_techniques_text.setReadOnly(True)
        self.added_sofware_text = self.findChild(QPlainTextEdit, "AddedSoftwareText")
        self.added_sofware_text.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.added_sofware_text.setReadOnly(True)
        self.potential_matches = self.findChild(QPlainTextEdit, "PotentialMatches")
        self.potential_matches.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.potential_matches.setReadOnly(True)
        self.tactic_box = self.findChild(QPlainTextEdit, "TacticsBox")
        self.tactic_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.tactic_box.setReadOnly(True)
        self.technique_box = self.findChild(QPlainTextEdit, "TechniquesBox")
        self.technique_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.technique_box.setReadOnly(True)
        self.software_box = self.findChild(QPlainTextEdit, "SoftwareBox")
        self.software_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.software_box.setReadOnly(True)

        self.tactics.setModel(self.model)
        self.techniques.setModel(self.model)
        self.software.addItems(Malware)


        #Populate Tactics and Techniques comboboxes
        for k, v in TacticCombo.items():
            tacts = QStandardItem(k)
            self.model.appendRow(tacts)
            for value in v:
                techniques = QStandardItem(value)
                tacts.appendRow(techniques)

        self.tactics.currentIndexChanged.connect(self.updateTacticCombo)
        self.updateTacticCombo(0)

        self.tactics.activated[str].connect(self.tactic_text)
        self.techniques.activated[str].connect(self.technique_text)
        self.software.activated[str].connect(self.software_text)
        self.tactic_selected = ""
        self.technique_selected = ""
        self.software_selected = ""
        self.add_technique_btn.pressed.connect(self.add_technique)
        self.add_software_btn.pressed.connect(self.add_software)
        self.delete_technique_btn.pressed.connect(self.delete_technique)
        self.delete_software_btn.pressed.connect(self.delete_software)
        self.clear_all_btn.pressed.connect(self.clear_all)

        self.showMaximized()


    def updateTacticCombo(self, index):
        indx = self.model.index(index, 0, self.tactics.rootModelIndex())
        self.techniques.setRootModelIndex(indx)
        self.techniques.setCurrentIndex(0)

    #Gets whatever is in the comboxbox
    def tactic_text(self, text):
        self.tactic_selected = self.tactics.currentText()
        self.description_box.setPlainText(self.tactic_selected)
    def technique_text(self,text):
        self.technique_selected = self.techniques.currentText()
        self.description_box.setPlainText(self.technique_selected)

    def software_text(self,text):
        self.software_selected = self.software.currentText()
        self.description_box.setPlainText(self.software_selected)


    def add_technique(self):
        if(self.technique_selected != ""):
            self.added_techniques_box.addItem(self.technique_selected)
            self.description_box.setPlainText("Technique " + self.technique_selected+ " has been added to the technique list." )
            Backend_list.append(self.technique_selected)
            self.technique_selected = ""
            self.techniques.removeItem(self.techniques.currentIndex())
            print(Backend_list)
    def add_software(self):
        if(self.software_selected != ""):
            self.added_software_box.addItem(self.software_selected)
            self.description_box.setPlainText("Software " + self.software_selected+ " has been added to the software list." )
            Backend_list.append(self.software_selected)
            self.software_selected = ""
            self.software.removeItem(self.software.currentIndex())
            print (Backend_list)

    def delete_technique(self):
        listItems=self.added_techniques_box.selectedItems()
        if not listItems: return
        for item in listItems:
            self.added_techniques_box.takeItem(self.added_techniques_box.row(item))
            self.description_box.setPlainText("Technique " + item.text()+ " has been removed from the technique list." )
            Backend_list.remove(item.text())
            self.techniques.addItem(item.text())
            print(Backend_list)
    def delete_software(self):
        listItems=self.added_software_box.selectedItems()
        if not listItems: return
        for item in listItems:
            self.added_software_box.takeItem(self.added_software_box.row(item))
            self.description_box.setPlainText("Software " + item.text()+ " has been removed from the software list." )
            Backend_list.remove(item.text())
            self.software.addItem(item.text())
            print(Backend_list)
    def clear_all(self):
        self.added_techniques_box.clear()
        self.added_software_box.clear()
        self.description_box.setPlainText("All techniques and software have been cleared from added techniques and added software lists.")
        Backend_list.clear()
        print (Backend_list)

#Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
