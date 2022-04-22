from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QPushButton, QPlainTextEdit, QCompleter, QListWidget, QAction, QLabel, QSlider, QTextBrowser
from PyQt5 import uic, Qt, QtCore
from PyQt5.QtCore import QCoreApplication
import sys
import json
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QMovie, QIcon, QTextCursor
import RAPTORFunctions as apt
import RAPTORReport as report
import webbrowser
import os


techniques_df, tactics_df, groups_df, software_df, mitigations_df, gfr_df, relationships_df = apt.buildDataFrames()
apt.getTechniquesByTactic(tactics_df, techniques_df)
apt.getSoftwareList(software_df)
TacticCombo = apt.getTechniquesByTactic(tactics_df, techniques_df)
Techniques = apt.getTechniqueList(techniques_df)
Malware = apt.getSoftwareList(software_df)
Backend_list = []

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui File
        uic.loadUi("GUIFiles/GUI.ui", self)
        self.setWindowTitle("RAPTOR")
        self.setWindowIcon(QIcon('GUIFiles/raptor.png'))
        self.setStyleSheet("background-color: #282C2E; color: white; font-size : 12 pt;")
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
        self.evaluate_btn.hide()
        self.reset_btn = self.findChild(QPushButton, "ResetButton")
        self.reset_btn.setStyleSheet('QPushButton {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.reset_btn.hide()

        self.added_techniques_box = self.findChild(QListWidget, "AddedTechniquesBox")
        self.added_techniques_box.setStyleSheet('QListWidget {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.added_software_box = self.findChild(QListWidget, "AddedSoftwareBox")
        self.added_software_box.setStyleSheet('QListWidget {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.description_box = self.findChild(QTextBrowser, "DescriptionBox")
        self.description_box.setStyleSheet('QTextBrowser {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.description_box.setOpenExternalLinks(True)
        #self.description_box.setAcceptRichText(True)
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

        self.slider = self.findChild(QSlider, "slider_bar")
        self.slider.setStyleSheet("QSlider::handle:horizontal {background-color : green, border-color: grey}")

        self.slider_text = self.findChild(QLabel, "slider_text")
        self.slider_text.setStyleSheet('QLabel{background-color: #282C2E; color: white; font-size : 13pt;}')

        #self.tactics.setModel(self.model)
        #self.techniques.setModel(self.model)
        self.software.addItems(Malware)

        self.update_action = self.findChild(QAction, "actionUpdate")
        self.progress_label = self.findChild(QLabel, "progress")
        self.progress_label.setStyleSheet('QLabel {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.progress_label.hide()
        self.update_label = self.findChild(QLabel, "updating")
        self.update_label.setStyleSheet('QLabel {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.update_label.hide()
        self.update_label2 = self.findChild(QLabel, "updating_2")
        self.update_label2.setStyleSheet('QLabel {background-color: #282C2E; color: white; font-size : 12pt;}')
        self.update_label2.hide()
        self.movie1 = QMovie("GUIFiles/dinosaur.gif")
        self.progress_label.setMovie(self.movie1)
        self.movie2 = QMovie("GUIFiles/updating.gif")
        self.update_label.setMovie(self.movie2)
        self.movie3 = QMovie("GUIFiles/result.gif")
        self.update_label2.setMovie(self.movie3)

        self.tactics.addItem("", Techniques)
        for i in range(len(TacticCombo)):
            self.tactics.addItem(list(TacticCombo.keys())[i], list(TacticCombo.values())[i])

        self.tactics.currentIndexChanged.connect(self.indexChanged)
        self.indexChanged(self.tactics.currentIndex())

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

        self.slider.valueChanged.connect(self.sliderchange)
        self.showMaximized()

    def sliderchange(self):
        self.slider_text.setText(str(self.slider.value())+ "%")
        self.potential_matches.setPlainText("Potential Matches above " +str(self.slider.value())+ "%:  "  + str(apt.update_num(gfr_df, Backend_list, self.slider.value())))

    def indexChanged(self, index):
        self.techniques.clear()
        data = self.tactics.itemData(index)
        if data is not None:
            self.techniques.addItems(data)

    #Gets whatever is in the comboxbox
    def tactic_text(self, text):
        self.description_box.moveCursor(QTextCursor.Start)
        self.description_box.setOpenExternalLinks(True)
        self.tactic_selected = self.tactics.currentText()
        #self.description_box.setPlainText(self.tactic_selected)
        if (self.tactic_selected != ""):
            self.description_box.setHtml("{}<p>{}</p>".format(self.tactic_selected, apt.getDescriptionByName(tactics_df,self.tactic_selected)))
    def technique_text(self,text):
        self.description_box.moveCursor(QTextCursor.Start)
        self.description_box.setOpenExternalLinks(True)
        self.technique_selected = self.techniques.currentText()
        self.description_box.setHtml(apt.getDescriptionByName(techniques_df,self.technique_selected))
        #self.description_box.setHtml("{}...\n\n{}".format(self.technique_selected, apt.getDescriptionByName(techniques_df,self.technique_selected)))

    def software_text(self,text):
        self.description_box.moveCursor(QTextCursor.Start)
        self.description_box.setOpenExternalLinks(True)
        self.software_selected = self.software.currentText()
        #self.description_box.setText(self.software_selected)
        self.description_box.setHtml(apt.getDescriptionByName(software_df, self.software_selected))

    def add_technique(self):
        self.description_box.setOpenExternalLinks(False)
        self.description_box.setAcceptRichText(False)
        self.description_box.moveCursor(QTextCursor.Start)

        if(self.technique_selected != ""):
            if (self.technique_selected in Backend_list):
                self.description_box.setHtml("Technique already added, please select another.")
            else:
                self.added_techniques_box.addItem(self.technique_selected)
                self.description_box.setHtml("Technique: " + self.technique_selected+ " has been added to the technique list." )
                Backend_list.append(self.technique_selected)
                self.technique_selected = ""
                self.potential_matches.setPlainText("Potential Matches above " +str(self.slider.value())+ "%:  "  + str(apt.update_num(gfr_df, Backend_list, self.slider.value())))
                if(apt.update_num(gfr_df, Backend_list, self.slider.value()) >= 1):
                    self.evaluate_btn.show()
                else:
                    self.evaluate_btn.hide()

    def add_software(self):
        self.description_box.setOpenExternalLinks(False)
        self.description_box.setAcceptRichText(False)

        if(self.software_selected != ""):
            if (self.software_selected in Backend_list):
                self.description_box.setHtml("Software already added, please select another.")
            else:
                self.added_software_box.addItem(self.software_selected)
                self.description_box.setHtml("Software " + self.software_selected+ " has been added to the software list." )
                Backend_list.append(self.software_selected)
                self.software_selected = ""
                self.potential_matches.setPlainText("Potential Matches above " +str(self.slider.value())+ "%:  "  + str(apt.update_num(gfr_df, Backend_list, self.slider.value())))
                if(apt.update_num(gfr_df, Backend_list, self.slider.value()) >= 1):
                    self.evaluate_btn.show()
                else:
                    self.evaluate_btn.hide()

    def delete_technique(self):
        listItems=self.added_techniques_box.selectedItems()
        if not listItems: return
        for item in listItems:
            self.added_techniques_box.takeItem(self.added_techniques_box.row(item))
            self.description_box.setHtml("Technique " + item.text()+ " has been removed from the technique list." )
            Backend_list.remove(item.text())
            self.potential_matches.setPlainText("Potential Matches above " +str(self.slider.value())+ "%:  "  + str(apt.update_num(gfr_df, Backend_list, self.slider.value())))
            if(apt.update_num(gfr_df, Backend_list, self.slider.value()) >= 1):
                self.evaluate_btn.show()
            else:
                self.evaluate_btn.hide()
    def delete_software(self):
        listItems=self.added_software_box.selectedItems()
        if not listItems: return
        for item in listItems:
            self.added_software_box.takeItem(self.added_software_box.row(item))
            self.description_box.setHtml("Software " + item.text()+ " has been removed from the software list." )
            Backend_list.remove(item.text())
            self.potential_matches.setPlainText("Potential Matches above " +str(self.slider.value())+ "%:  "  + str(apt.update_num(gfr_df, Backend_list, self.slider.value())))
            if(apt.update_num(gfr_df, Backend_list, self.slider.value()) >= 1):
                self.evaluate_btn.show()
            else:
                self.evaluate_btn.hide()
    def clear_all(self):
        self.evaluate_btn.hide()
        self.added_techniques_box.clear()
        self.added_software_box.clear()
        self.description_box.setHtml("All techniques and software have been cleared from added techniques and added software lists.")
        Backend_list.clear()
        self.potential_matches.setPlainText("Potential Matches above " +str(self.slider.value())+ "%:  "  + str(apt.update_num(gfr_df, Backend_list, self.slider.value())))

    def evaluate(self):
        self.temp_thread2 = StringThread2("Report")
        if ((self.added_techniques_box.count() == 0) and (self.added_software_box.count() == 0)):
            self.description_box.setHtml("Please add at least 1 technique or 1 software before evaluating.")
        else:
            Backend_list.clear()
            for i in range(self.added_techniques_box.count()):
                Backend_list.append(self.added_techniques_box.item(i).text())
            for i in range(self.added_software_box.count()):
                Backend_list.append(self.added_software_box.item(i).text())
            self.description_box.clear()
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
            self.reset_btn.hide()
            self.progress_label.show()
            self.update_label2.show()
            self.movie1.start()
            self.movie3.start()
            self.temp_thread2.start()
            self.temp_thread2.finished.connect(self.thread_finished)


    def thread_finished(self):
        self.description_box.clear()
        self.progress_label.hide()
        self.update_label2.hide()
        self.reset_btn.show()
        self.reset_btn.setEnabled(True)
        self.description_box.setHtml("PLEASE PRESS RESET BUTTON TO CONTINUE WORKING.")


    def reset(self):
        Backend_list.clear()
        self.progress_label.hide()
        self.update_label2.hide()
        self.description_box.setOpenExternalLinks(True)
        self.evaluate_btn.setEnabled(True)
        self.slider_bar.setEnabled(True)
        self.potential_matches.setPlainText("Potential Matches above 0%: ")
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
        self.evaluate_btn.hide()
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
        self.description_box.setHtml("<p>PLEASE WAIT...</p><p>THE STORED DATA IS BEING UPDATED...</p><p>APPLICATION WILL RESTART ONCE DONE...</p>")
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

class StringThread2(QtCore.QThread):

    str_signal = QtCore.pyqtSignal(str)
    _name = ''

    def __init__(self, name):
        QtCore.QThread.__init__(self)
        self._name = name

    def run(self):
        test_df = apt.filterForSelectedTechniques(gfr_df, Backend_list)
        report.htmlReport(apt.analyzeResults(test_df, Backend_list))
#Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
