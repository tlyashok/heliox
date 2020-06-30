import os
import sys

import pyqtgraph
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QTextEdit
from fpdf import FPDF
from datetime import datetime
from pyqtgraph.exporters import ImageExporter

import Heliocs
import график

class MainWindow(Heliocs.Ui_MainWindow, QtWidgets.QMainWindow):
    commonList= []
    file = ""
    graphic = ''
    def __init__(self):
        super(MainWindow, self).__init__()
        self.graphic = график.Ui_Form()
        self.setupUi(self)
        self.davl_gr = self.graphic.graph.plot([],[])
        self.konc_gr = self.graphic.graph.plot([],[])
        self.temp_gr = self.graphic.graph.plot([],[])
        self.obiem_gr = self.graphic.graph.plot([],[])
        self.chastota_gr = self.graphic.graph.plot([],[])
        self.potok_gr = self.graphic.graph.plot([],[])
        self.minutni_gr = self.graphic.graph.plot([],[])
        self.spo2_gr= self.graphic.graph.plot([],[])
        self.pulse_gr = self.graphic.graph.plot([],[])
        self.patientButton.clicked.connect(self.patientButtonClicked)
        self.inh_1.clicked.connect(self.inhGraph)
        self.inhTable.itemClicked.connect(self.tableClicked)
        self.graphic.pechat_aktivnih_grafikov.clicked.connect(self.printActive)

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



    def clear(self):
        self.id_w.setText("---")
        self.surname_w.setText("---")
        self.name_w.setText("---")
        self.patronymic_w.setText("---")
        self.birhday_w.setText("---")
        self.gender_w.setText("---")
        self.weight_w.setText("---")
        self.heigh_w.setText("---")

    def clearArr(self):
        self.pulse_g = [[],[]]
        self.SpO2_g = [[],[]]
        self.minutni_obiem_g = [[],[]]
        self.potok_g =[[],[]]
        self.chastota_dihaniya_g =[[],[]]
        self.obiem_g =[[],[]]
        self.temperatura_vdihaemoi_smesi_g =[[],[]]
        self.koncetracia_O2_g = [[],[]]
        self.Davlenie_v_maske_g = [[],[]]


    def tableClicked(self):
        self.clearArr()
        self.graphic.Date_inhalation_w.setText(self.inhTable.item(self.inhTable.currentRow(), 0).text())
        self.graphic.dlitelnost_inh_w.setText(self.inhTable.item(self.inhTable.currentRow(),1).text())
        if os.path.exists(os.path.join(self.file, self.commonList[self.patientList.currentRow()],
                                   self.inhTable.item(self.inhTable.currentRow(), 7).text())):
            with open(os.path.join(self.file, self.commonList[self.patientList.currentRow()],
                                   self.inhTable.item(self.inhTable.currentRow(), 7).text()), 'r', encoding="UTF-8") as currentlog:
                logfile = currentlog.read().split('\n')
                for i in logfile:
                    i = i[0:len(i)-2]
                    i = i.split(';')
                    if len(i) > 20 and i[0] != '#':
                        self.Davlenie_v_maske_g[0].append(int(i[0])/100)
                        self.koncetracia_O2_g[0].append(int(i[0])/100)
                        self.temperatura_vdihaemoi_smesi_g[0].append(int(i[0])/100)
                        self.obiem_g[0].append(int(i[0])/100)
                        self.chastota_dihaniya_g[0].append(int(i[0])/100)
                        self.potok_g[0].append(int(i[0])/100)
                        self.minutni_obiem_g[0].append(int(i[0])/100)
                        self.SpO2_g[0].append(int(i[0])/100)
                        self.pulse_g[0].append(int(i[0])/100)
                        self.Davlenie_v_maske_g[1].append(int(i[4]) / 100)
                        self.koncetracia_O2_g[1].append(int(i[5]))
                        self.temperatura_vdihaemoi_smesi_g[1].append(int(i[6]))
                        self.obiem_g[1].append(int(i[7]))
                        self.chastota_dihaniya_g[1].append(int(i[8]))
                        self.potok_g[1].append(int(i[9])/10)
                        self.minutni_obiem_g[1].append(int(i[14]))
                        self.SpO2_g[1].append(int(i[19]))
                        self.pulse_g[1].append(int(i[20]))
                self.Davl()
                self.Konc()
                self.Temp()
                self.Obiem()
                self.Chastota()
                self.Potok()
                self.Minutni()
                self.SpO2()
                self.Pulse()
                self.graphic.Davlenie_v_maske.toggled.connect(self.Davl)
                self.graphic.koncetracia_O2.toggled.connect(self.Konc)
                self.graphic.temperatura_vdihaemoi_smesi.toggled.connect(self.Temp)
                self.graphic.obiem.toggled.connect(self.Obiem)
                self.graphic.chastota_dihaniya.toggled.connect(self.Chastota)
                self.graphic.potok.toggled.connect(self.Potok)
                self.graphic.minutni_obiem.toggled.connect(self.Minutni)
                self.graphic.SpO2.toggled.connect(self.SpO2)
                self.graphic.pulse.toggled.connect(self.Pulse)






    def Davl(self):
        if self.graphic.Davlenie_v_maske.isChecked():
            pen = pyqtgraph.mkPen(color=(255,0,0), width=1, style=QtCore.Qt.SolidLine)
            self.davl_gr.setData(self.Davlenie_v_maske_g[0], self.Davlenie_v_maske_g[1], pen=pen)
        else:
            self.davl_gr.setData([],[])

    def Konc(self):
        if self.graphic.koncetracia_O2.isChecked():
            pen = pyqtgraph.mkPen(color=(0,255,0), width=1, style=QtCore.Qt.SolidLine)
            self.konc_gr.setData(self.koncetracia_O2_g[0], self.koncetracia_O2_g[1], pen=pen)
        else:
            self.konc_gr.setData([],[])

    def Temp(self):
        if self.graphic.temperatura_vdihaemoi_smesi.isChecked():
            pen = pyqtgraph.mkPen(color=(0,0,255), width=1, style=QtCore.Qt.SolidLine)
            self.temp_gr.setData(self.temperatura_vdihaemoi_smesi_g[0], self.temperatura_vdihaemoi_smesi_g[1], pen=pen)
        else:
            self.temp_gr.setData([],[])

    def Obiem(self):
        if self.graphic.obiem.isChecked():
            pen = pyqtgraph.mkPen(color=(100,30,100), width=1, style=QtCore.Qt.SolidLine)
            self.obiem_gr.setData(self.obiem_g[0], self.obiem_g[1], pen=pen)
        else:
            self.obiem_gr.setData([],[])

    def Chastota(self):
        if self.graphic.chastota_dihaniya.isChecked():
            pen = pyqtgraph.mkPen(color=(0,255,255), width=1, style=QtCore.Qt.SolidLine)
            self.chastota_gr.setData(self.chastota_dihaniya_g[0], self.chastota_dihaniya_g[1], pen=pen)
        else:
            self.chastota_gr.setData([],[])

    def Potok(self):
        if self.graphic.potok.isChecked():
            pen = pyqtgraph.mkPen(color=(255,0,255), width=1, style=QtCore.Qt.SolidLine)
            self.potok_gr.setData(self.potok_g[0], self.potok_g[1], pen=pen)
        else:
            self.potok_gr.setData([],[])

    def Minutni(self):
        if self.graphic.minutni_obiem.isChecked():
            pen = pyqtgraph.mkPen(color=(100,200,100), width=1, style=QtCore.Qt.SolidLine)
            self.minutni_gr.setData(self.minutni_obiem_g[0], self.minutni_obiem_g[1], pen=pen)
        else:
            self.minutni_gr.setData([], [])

    def SpO2(self):
        if self.graphic.SpO2.isChecked():
            pen = pyqtgraph.mkPen(color=(100,50,100), width=1, style=QtCore.Qt.SolidLine)
            self.spo2_gr.setData(self.SpO2_g[0], self.SpO2_g[1], pen=pen)
        else:
            self.spo2_gr.setData([], [])

    def Pulse(self):
        if self.graphic.pulse.isChecked():
            pen = pyqtgraph.mkPen(color=(0,100,0), width=1, style=QtCore.Qt.SolidLine)
            self.pulse_gr.setData(self.pulse_g[0], self.pulse_g[1], pen=pen)
        else:
            self.pulse_gr.setData([], [])

    def printActive(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.add_font('DejaVuSansBold', '', 'DejaVuSans-Bold.ttf', uni=True)
        pdf.add_font('DejaVuSans', '', 'DejaVuSans.ttf', uni=True)
        pdf.set_font('DejaVuSansBold', '', 20)
        pdf.cell(190, 20, txt='Аппарат ГелиОкс', align='C', ln = 1)
        pdf.set_font('DejaVuSans', '', 12)
        pdf.cell(150, 10, txt='ID пациента:{}'.format(self.graphic.id_patient_w.text()), ln = 1)
        pdf.cell(150, 10, txt='ФИО пациента:{}'.format(self.graphic.Patientl_w.text()), ln = 1)

        now = datetime.now() #Высчитывание возраста
        temp = self.birhday_w.text().split('.')
        temp = [int(i) for i in temp]
        year = now.year - temp[2] - 1
        if now.month > temp[1]:
            year += 1
        elif now.month == temp[1] and now.day >= temp[0]:
            year += 1

        pdf.cell(150, 10, txt='Возраст: {}                    '
                              'Вес: {}                    '
                              'Рост: {}'.format(year, self.weight_w.text(), self.heigh_w.text()), ln = 1)
        pdf.multi_cell(150, 10, txt='Комментарий: {}'.format(self.commText.toPlainText()))
        pdf.cell(150, 10, txt='Средняя концетрация O2, %: {}'.format(self.inhTable.item(self.inhTable.currentRow(), 3).text()), ln=1)
        pdf.cell(150, 10, txt='Средняя температура, град. C: {}'.format(self.inhTable.item(self.inhTable.currentRow(), 6).text()), ln=1)
        pdf.cell(150, 10, txt='Дата проведения ингаляции: {}'.format(self.inhTable.item(self.inhTable.currentRow(), 0).text() + " " +
                                                                     self.inhTable.item(self.inhTable.currentRow(), 1).text()), ln=1)
        if not os.path.exists('\\Heliox_temp'):
            os.mkdir('\\Heliox_temp')
        exporter = ImageExporter(self.graphic.graph.getPlotItem())
        exporter.export('\\Heliox_temp\\temp_image.png')
        pdf.image('\\Heliox_temp\\temp_image.png', w=180,h=110)
        os.system('\\Heliox_temp\\temp_pdf.pdf')


        pdf.output('\\Heliox_temp\\temp_pdf.pdf', 'F')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()