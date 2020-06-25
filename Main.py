import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

import Heliocs


class MainWindow(Heliocs.Ui_MainWindow, QtWidgets.QMainWindow):
    commonList= []
    file = ""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.patientButton.clicked.connect(self.patientButtonClicked)
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
                    if info[0] == '#':
                        self.inhTable.setRowCount(temp_row)
                        info = list(info.split(';'))
                        info = info[2:9]
                        for y in range(0,7):
                            self.inhTable.setItem(temp_row-1, y, QtWidgets.QTableWidgetItem(info[y]))
                        self.inhTable.setItem(temp_row-1, 9, QtWidgets.QTableWidgetItem(info[1]))
                        temp_row += 1



    def clear(self):
        self.id_w.setText("---")
        self.surname_w.setText("---")
        self.name_w.setText("---")
        self.patronymic_w.setText("---")
        self.birhday_w.setText("---")
        self.gender_w.setText("---")
        self.weight_w.setText("---")
        self.heigh_w.setText("---")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
