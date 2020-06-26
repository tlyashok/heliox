import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

import Heliocs
import график

class MainWindow(Heliocs.Ui_MainWindow, QtWidgets.QMainWindow):
    commonList= []
    file = ""
    graphic = ''
    logfile = ''
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.graphic = график.Ui_Form()
        self.patientButton.clicked.connect(self.patientButtonClicked)
        self.inh_1.clicked.connect(self.inhGraph)
        self.inhTable.itemClicked.connect(self.tableClicked)

    def patientButtonClicked(self):
        self.file = str(QFileDialog.getExistingDirectory(self, 'Выбор папки...'))
        self.commonList = []
        if len(list(os.walk(self.file))) != 0:
            for i in list(os.walk(self.file))[0][1]:
                self.commonList.append(i)
            self.patientListTunning()


    def patientListTunning(self):
        lenPatientList = len(self.commonList)
        self.patientList.clear()
        i = 0
        if lenPatientList > 0:
            while i < len(self.commonList):
                if "patientData" in list(os.listdir(os.path.join(self.file, self.commonList[i]))):
                    self.patientList.addItem(self.commonList[i])
                    i += 1
                else:
                    self.commonList.remove(self.commonList[i])
        self.patientList.setMinimumWidth(self.patientList.sizeHintForColumn(0) + 30)
        self.patientList.itemClicked.connect(self.selectPatient)


    def selectPatient(self):
        self.clear()
        if os.path.isfile(os.path.join(self.file, self.commonList[self.patientList.currentRow()], 'patientData')):
            with open(os.path.join(self.file, self.commonList[self.patientList.currentRow()], 'patientData'), 'r', encoding='UTF-8') as patientData:
                data = list(patientData.read().split(';'))
                if len(data) >= 6:
                    self.id_w.setText(data[0])
                    if len(data[1].split(" ")) >= 1:
                        self.surname_w.setText(data[1].split(" ")[0])
                        if len(data[1].split(" ")) >= 2:
                            self.name_w.setText(data[1].split(" ")[1])
                            if len(data[1].split(" ")) >= 3:
                                self.patronymic_w.setText(data[1].split(" ")[2])

                    self.birhday_w.setText(data[2])
                    self.gender_w.setText(data[3])
                    self.weight_w.setText(data[4])
                    self.heigh_w.setText(data[5])
                else:
                    self.clear()
        else:
            self.clear()
        temp_row = 1
        self.inhTable.setRowCount(1)
        for i in os.listdir(os.path.join(self.file, self.commonList[self.patientList.currentRow()])):
            if i.endswith('.csv'):
                with open(os.path.join(self.file, self.commonList[self.patientList.currentRow()], i), 'r', encoding='UTF-8') as filedata:
                    fullinfo = list(filedata.read().split("\n"))
                    info = fullinfo[len(fullinfo)-2]
                    self.inhTable.setRowCount(temp_row)
                    if info[0] == '#':
                        info = list(info.split(';'))
                        info = info[2:9]
                        for y in range(0,7):
                            self.inhTable.setItem(temp_row-1, y, QtWidgets.QTableWidgetItem(info[y]))
                        self.inhTable.setItem(temp_row-1, 7, QtWidgets.QTableWidgetItem(i))
                    else:
                        for y in range(0,8):
                            self.inhTable.setItem(temp_row-1, y, QtWidgets.QTableWidgetItem('---'))
                    temp_row += 1
        self.graphic.id_patient_w.setText(self.id_w.text())
        temp_string = ""
        if self.patronymic_w.text() != '---':
            temp_string = self.patronymic_w.text() + ' '
        if self.name_w.text() != '---':
            temp_string = temp_string + self.name_w.text() + ' '
        if self.surname_w.text() != '---':
            temp_string = temp_string + self.surname_w.text() + ' '
        self.graphic.Patientl_w.setText(temp_string)

    def inhGraph(self):
        self.graphic.graph.setBackground('w')
        self.graphic.show()
        self.graphic.Davlenie_v_maske.isChecked()


    def clear(self):
        self.id_w.setText("---")
        self.surname_w.setText("---")
        self.name_w.setText("---")
        self.patronymic_w.setText("---")
        self.birhday_w.setText("---")
        self.gender_w.setText("---")
        self.weight_w.setText("---")
        self.heigh_w.setText("---")


    def tableClicked(self):
        self.graphic.Date_inhalation_w.setText(self.inhTable.item(self.inhTable.currentRow(), 0).text())
        self.graphic.Davlenie_v_maske.setChecked(False)
        self.graphic.koncetracia_O2.setChecked(False)
        self.graphic.temperatura_vdihaemoi_smesi.setChecked(False)
        self.graphic.obiem.setChecked(False)
        self.graphic.chastota_dihaniya.setChecked(False)
        self.graphic.potok.setChecked(False)
        self.graphic.minutni_obiem.setChecked(False)
        self.graphic.SpO2.setChecked(False)
        self.graphic.pulse.setChecked(False)
        if os.path.exists(os.path.join(self.file, self.commonList[self.patientList.currentRow()],
                                   self.inhTable.item(self.inhTable.currentRow(), 7).text())):
            with open(os.path.join(self.file, self.commonList[self.patientList.currentRow()],
                                   self.inhTable.item(self.inhTable.currentRow(), 7).text()), 'r', encoding="UTF-8") as currentlog:
                pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()