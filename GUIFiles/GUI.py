from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QPushButton, QPlainTextEdit, QCompleter, QListWidget, QAction, QLabel
from PyQt5 import uic, Qt, QtCore
from PyQt5.QtCore import QCoreApplication
import sys
import json
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QMovie, QIcon
import aptFunctions as apt
import webbrowser
import os


techniques_df, tactics_df, groups_df, software_df, mitigations_df, gfr_df, relationships_df = apt.buildDataFrames()
apt.getTechniquesByTactic(tactics_df, techniques_df)
apt.getSoftwareList(software_df)
TacticCombo = apt.getTechniquesByTactic(tactics_df, techniques_df)
Malware = apt.getSoftwareList(software_df)
Backend_list = []

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui File
        uic.loadUi("GUI.ui", self)
        self.setWindowTitle("RAPTOR")
        self.setWindowIcon(QIcon('raptor.png'))

        self.model = QStandardItemModel()

        #Define our QtWidgets
        self.tactics = self.findChild(QComboBox, "Tactics")
        self.tactics.setEditable(True)
        self.tactics.setStyleSheet('QComboBox {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.tactics.setInsertPolicy(QComboBox.NoInsert)
        self.tactics.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.techniques = self.findChild(QComboBox, "Techniques")
        self.techniques.setEditable(True)
        self.techniques.setStyleSheet('QComboBox {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.techniques.setInsertPolicy(QComboBox.NoInsert)
        self.techniques.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.software = self.findChild(QComboBox, "Software")
        self.software.setEditable(True)
        self.software.setStyleSheet('QComboBox {background-color: #282C2E; color: white; font-size : 12pt;}')
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
        self.evaluate_btn = self.findChild(QPushButton, "Evaluate")
        self.evaluate_btn.setStyleSheet('QPushButton {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.reset_btn = self.findChild(QPushButton, "ResetButton")
        self.reset_btn.setStyleSheet('QPushButton {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.reset_btn.hide()

        self.added_techniques_box = self.findChild(QListWidget, "AddedTechniquesBox")
        self.added_techniques_box.setStyleSheet('QListWidget {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.added_software_box = self.findChild(QListWidget, "AddedSoftwareBox")
        self.added_software_box.setStyleSheet('QListWidget {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.description_box = self.findChild(QPlainTextEdit, "DescriptionBox")
        self.description_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.description_box.setReadOnly(True)
        self.added_techniques_text = self.findChild(QPlainTextEdit, "AddedTechniquesText")
        self.added_techniques_text.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 13pt;}')
        self.added_techniques_text.setReadOnly(True)
        self.added_sofware_text = self.findChild(QPlainTextEdit, "AddedSoftwareText")
        self.added_sofware_text.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 13pt;}')
        self.added_sofware_text.setReadOnly(True)
        self.potential_matches = self.findChild(QPlainTextEdit, "PotentialMatches")
        self.potential_matches.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 13pt;}')
        self.potential_matches.setReadOnly(True)
        self.tactic_box = self.findChild(QPlainTextEdit, "TacticsBox")
        self.tactic_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 13pt;}')
        self.tactic_box.setReadOnly(True)
        self.technique_box = self.findChild(QPlainTextEdit, "TechniquesBox")
        self.technique_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 13pt;}')
        self.technique_box.setReadOnly(True)
        self.software_box = self.findChild(QPlainTextEdit, "SoftwareBox")
        self.software_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 13pt;}')
        self.software_box.setReadOnly(True)

        self.tactics.setModel(self.model)
        self.techniques.setModel(self.model)
        self.software.addItems(Malware)

        self.update_action = self.findChild(QAction, "actionUpdate")
        self.progress_label = self.findChild(QLabel, "progress")
        self.progress_label.setStyleSheet('QLabel {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.progress_label.hide()
        self.update_label = self.findChild(QLabel, "updating")
        self.update_label.setStyleSheet('QLabel {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.update_label.hide()
        self.movie1 = QMovie("dinosaur.gif")
        self.progress_label.setMovie(self.movie1)
        self.movie2 = QMovie("updating.gif")
        self.update_label.setMovie(self.movie2)

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
        self.evaluate_btn.pressed.connect(self.evaluate)
        self.reset_btn.pressed.connect(self.reset)
        self.update_action.triggered.connect(self.update_data)
        self.showMaximized()

    def updateTacticCombo(self, index):
          indx = self.model.index(index, 0, self.tactics.rootModelIndex())
          self.techniques.setRootModelIndex(indx)
          self.techniques.setCurrentIndex(0)

    #Gets whatever is in the comboxbox
    def tactic_text(self, text):
        self.tactic_selected = self.tactics.currentText()
        #self.description_box.setPlainText(self.tactic_selected)
        self.description_box.setPlainText(apt.getDescription(tactics_df, self.tactic_selected))
    def technique_text(self,text):
        self.technique_selected = self.techniques.currentText()
        self.description_box.setPlainText(self.technique_selected)
        self.description_box.setPlainText(apt.getDescription(techniques_df, self.technique_selected))

    def software_text(self,text):
        self.software_selected = self.software.currentText()
        self.description_box.setPlainText(self.software_selected)
        self.description_box.setPlainText(apt.getDescription(software_df, self.software_selected))


    def add_technique(self):
        if(self.technique_selected != ""):
            if (self.technique_selected in Backend_list):
                self.description_box.setPlainText("Technique already added, please select another.")
            else:
                self.added_techniques_box.addItem(self.technique_selected)
                self.description_box.setPlainText("Technique: " + self.technique_selected+ " has been added to the technique list." )
                Backend_list.append(self.technique_selected)
                self.technique_selected = ""
                self.potential_matches.setPlainText("Possible Matches above 50%: " + str(apt.update_num(gfr_df, Backend_list)))

    def add_software(self):
        if(self.software_selected != ""):
            if (self.software_selected in Backend_list):
                self.description_box.setPlainText("Software already added, please select another.")
            else:
                self.added_software_box.addItem(self.software_selected)
                self.description_box.setPlainText("Software " + self.software_selected+ " has been added to the software list." )
                Backend_list.append(self.software_selected)
                self.software_selected = ""
                self.potential_matches.setPlainText("Possible Matches above 50%: " + str(apt.update_num(gfr_df, Backend_list)))

    def delete_technique(self):
        listItems=self.added_techniques_box.selectedItems()
        if not listItems: return
        for item in listItems:
            self.added_techniques_box.takeItem(self.added_techniques_box.row(item))
            self.description_box.setPlainText("Technique " + item.text()+ " has been removed from the technique list." )
            Backend_list.remove(item.text())
            self.potential_matches.setPlainText("Possible Matches above 50%: " + str(apt.update_num(gfr_df, Backend_list)))

    def delete_software(self):
        listItems=self.added_software_box.selectedItems()
        if not listItems: return
        for item in listItems:
            self.added_software_box.takeItem(self.added_software_box.row(item))
            self.description_box.setPlainText("Software " + item.text()+ " has been removed from the software list." )
            Backend_list.remove(item.text())
            self.potential_matches.setPlainText("Possible Matches above 50%: " + str(apt.update_num(gfr_df, Backend_list)))

    def clear_all(self):
        self.added_techniques_box.clear()
        self.added_software_box.clear()
        self.description_box.setPlainText("All techniques and software have been cleared from added techniques and added software lists.")
        Backend_list.clear()
        self.potential_matches.setPlainText("Possible Matches above 50%: " + str(apt.update_num(gfr_df, Backend_list)))

    def evaluate(self):
        if ((self.added_techniques_box.count() == 0) and (self.added_software_box.count() == 0)):
            self.description_box.setPlainText("Please add at least 1 technique or 1 software before evaluating.")
        else:
            Backend_list.clear()
            for i in range(self.added_techniques_box.count()):
                Backend_list.append(self.added_techniques_box.item(i).text())
            for i in range(self.added_software_box.count()):
                Backend_list.append(self.added_software_box.item(i).text())
            self.reset_btn.show()
            self.tactics.setEnabled(False)
            self.techniques.setEnabled(False)
            self.software.setEnabled(False)
            self.add_technique_btn.setEnabled(False)
            self.add_software_btn.setEnabled(False)
            self.delete_technique_btn.setEnabled(False)
            self.delete_software_btn.setEnabled(False)
            self.clear_all_btn.setEnabled(False)
            self.evaluate_btn.setEnabled(False)
            self.update_action.setEnabled(False)
            filename = 'file:///'+os.getcwd()+'/' + 'results.html'
            webbrowser.open_new_tab(filename)
            self.description_box.setPlainText("Results have been generated..." +"\n" + "Please press Reset button to continue working.")

    def reset(self):
        Backend_list.clear()
        self.potential_matches.setPlainText("Possible Matches above 50%: ")
        self.added_techniques_box.clear()
        self.added_software_box.clear()
        self.description_box.clear()
        self.tactics.setEnabled(True)
        self.techniques.setEnabled(True)
        self.software.setEnabled(True)
        self.add_technique_btn.setEnabled(True)
        self.add_software_btn.setEnabled(True)
        self.delete_technique_btn.setEnabled(True)
        self.delete_software_btn.setEnabled(True)
        self.clear_all_btn.setEnabled(True)
        self.evaluate_btn.setEnabled(True)
        self.update_action.setEnabled(True)
        self.reset_btn.hide()

    def update_data(self):
        self.temp_thread = StringThread("RAPTOR")
        self.tactics.clear()
        self.software.clear()
        self.potential_matches.clear()
        self.description_box.clear()
        self.added_software_box.clear()
        self.added_techniques_box.clear()
        self.description_box.setStyleSheet('QPlainTextEdit {background-color: #282C2E; color: white; font-size : 14pt;}')
        self.description_box.insertPlainText("PLEASE WAIT..." + "\n" + "THE STORED DATA IS BEING UPDATED..." + "\n" + "APPLICATION WILL RESTART ONCE DONE...")
        self.progress_label.show()
        self.update_label.show()
        self.movie1.start()
        self.movie2.start()
        self.setEnabled(False)
        self.temp_thread.start()

class StringThread(QtCore.QThread):

    str_signal = QtCore.pyqtSignal(str)
    _name = ''

    def __init__(self, name):
        QtCore.QThread.__init__(self)
        self._name = name

    def run(self):
        apt.updateDataFrameSources()
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)

#Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
