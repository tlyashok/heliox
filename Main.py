import os
import sys

import pyqtgraph
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableWidgetItem
from fpdf import FPDF
from datetime import datetime
from pyqtgraph.exporters import ImageExporter
from pyqtgraph.graphicsItems.ScatterPlotItem import tr

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
        self.graphic.graph.addLegend(offset=[0,-300])
        self.davl_gr = self.graphic.graph.plot([],[], name='Давление в маске (см.вод.ст.)')
        self.konc_gr = self.graphic.graph.plot([],[], name='Концентрация O2 (%)')
        self.temp_gr = self.graphic.graph.plot([],[], name='Температура вдыхаемой смеси (град.)')
        self.obiem_gr = self.graphic.graph.plot([],[], name='Объём (мл)')
        self.chastota_gr = self.graphic.graph.plot([],[], name='Частота дыхания (1/мин)')
        self.potok_gr = self.graphic.graph.plot([],[], name='Поток (л/мин)')
        self.minutni_gr = self.graphic.graph.plot([],[], name='Минутный объём (л/мин)')
        self.spo2_gr= self.graphic.graph.plot([],[], name='SpO2 (%)')
        self.pulse_gr = self.graphic.graph.plot([],[], name='Пульс (1/мин)')
        self.FiO2_sr_gr = self.graphic.graph.plot([],[], name='FiO2 сред (%)')
        self.V_sr_gr = self.graphic.graph.plot([],[], name='V сред (мл)')
        self.F_sr_gr = self.graphic.graph.plot([],[], name='F сред (1/мин)')
        self.T_sr_gr = self.graphic.graph.plot([],[], name='T сред (град)')
        self.patientButton.clicked.connect(self.patientButtonClicked)
        self.inh_1.clicked.connect(self.inhGraph)
        self.inhTable.itemClicked.connect(self.tableClicked)
        self.graphic.pechat_aktivnih_grafikov.clicked.connect(self.printActive)
        self.graphic.pechat_grafikov_dihatelnogo_obiema.clicked.connect(self.printActive2)
        self.graphic.save_button.clicked.connect(self.save_graph)
        self.inh_3.clicked.connect(self.spisokInh)
        self.inh_2.clicked.connect(self.othergraphic)


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
        self.FiO2_gr = []
        self.V_gr = []
        self.F_gr = []
        self.T_gr = []
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
                            if y == 3 and info[3] != '---':
                                temp = []
                                temp.append(info[0])
                                temp.append(info[1])
                                temp.append(info[y])
                                self.FiO2_gr.append(temp)

                            if y == 4 and info[4] != '---':
                                temp = []
                                temp.append(info[0])
                                temp.append(info[1])
                                temp.append(info[y])
                                self.V_gr.append(temp)
                            if y == 5 and info[5] != '---':
                                temp = []
                                temp.append(info[0])
                                temp.append(info[1])
                                temp.append(info[y])
                                self.F_gr.append(temp)
                            if y == 6 and info[6] != '---':
                                temp = []
                                temp.append(info[0])
                                temp.append(info[1])
                                temp.append(info[y])
                                self.T_gr.append(temp)
                            temp_item = QtWidgets.QTableWidgetItem(info[y])
                            temp_item.setFlags(
                                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                            )
                            self.inhTable.setItem(temp_row-1, y, temp_item)
                        temp_item = QtWidgets.QTableWidgetItem(i)
                        temp_item.setFlags(
                            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                        )
                        self.inhTable.setItem(temp_row-1, 7, temp_item)
                    else:
                        for y in range(0,8):
                            temp_item = QtWidgets.QTableWidgetItem('---')
                            temp_item.setFlags(
                                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                            )
                            self.inhTable.setItem(temp_row-1, y, temp_item)
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
        self.graphic.FiO2.toggled.connect(self.FiO2)
        self.graphic.V.toggled.connect(self.V)
        self.graphic.F.toggled.connect(self.F)
        self.graphic.T.toggled.connect(self.T)

    def inhGraph(self):
        self.graphic.FiO2.setChecked(False)
        self.graphic.F.setChecked(False)
        self.graphic.V.setChecked(False)
        self.graphic.T.setChecked(False)
        self.FiO2()
        self.F()
        self.V()
        self.T()
        self.graphic.FiO2.hide()
        self.graphic.V.hide()
        self.graphic.F.hide()
        self.graphic.T.hide()
        self.graphic.FiO2_l.hide()
        self.graphic.V_l.hide()
        self.graphic.F_l.hide()
        self.graphic.T_l.hide()
        self.graphic.graph.setBackground('w')
        self.graphic.pechat_grafikov_dihatelnogo_obiema.show()
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.LabelRole, self.graphic.FiO2)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.FiO2_l)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.LabelRole, self.graphic.V)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.V_l)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.LabelRole, self.graphic.F)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.F_l)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.LabelRole, self.graphic.T)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.T_l)
        self.graphic.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.graphic.Davlenie_v_maske)
        self.graphic.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.graphic.koncetracia_O2)
        self.graphic.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.graphic.temperatura_vdihaemoi_smesi)
        self.graphic.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.graphic.obiem)
        self.graphic.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.graphic.chastota_dihaniya)
        self.graphic.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.graphic.potok)
        self.graphic.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.graphic.minutni_obiem)
        self.graphic.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.graphic.SpO2)
        self.graphic.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.graphic.pulse)
        self.graphic.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.graphic.label)
        self.graphic.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_2)
        self.graphic.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.graphic.label_3)
        self.graphic.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.graphic.label_4)
        self.graphic.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.graphic.label_5)
        self.graphic.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.graphic.label_6)
        self.graphic.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.graphic.label_7)
        self.graphic.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.graphic.label_8)
        self.graphic.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.graphic.label_9)
        self.graphic.Davlenie_v_maske.show()
        self.graphic.koncetracia_O2.show()
        self.graphic.temperatura_vdihaemoi_smesi.show()
        self.graphic.obiem.show()
        self.graphic.chastota_dihaniya.show()
        self.graphic.potok.show()
        self.graphic.minutni_obiem.show()
        self.graphic.SpO2.show()
        self.graphic.pulse.show()
        self.graphic.label.show()
        self.graphic.label_2.show()
        self.graphic.label_3.show()
        self.graphic.label_4.show()
        self.graphic.label_5.show()
        self.graphic.label_6.show()
        self.graphic.label_7.show()
        self.graphic.label_8.show()
        self.graphic.label_9.show()
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
            self.davl_gr.setData([], [], pen=pyqtgraph.mkPen())

    def Konc(self):
        if self.graphic.koncetracia_O2.isChecked():
            pen = pyqtgraph.mkPen(color=(0,255,0), width=1, style=QtCore.Qt.SolidLine)
            self.konc_gr.setData(self.koncetracia_O2_g[0], self.koncetracia_O2_g[1], pen=pen)
        else:
            self.konc_gr.setData([], [], pen=pyqtgraph.mkPen())

    def Temp(self):
        if self.graphic.temperatura_vdihaemoi_smesi.isChecked():
            pen = pyqtgraph.mkPen(color=(0,0,255), width=1, style=QtCore.Qt.SolidLine)
            self.temp_gr.setData(self.temperatura_vdihaemoi_smesi_g[0], self.temperatura_vdihaemoi_smesi_g[1], pen=pen)
        else:
            self.temp_gr.setData([], [], pen=pyqtgraph.mkPen())

    def Obiem(self):
        if self.graphic.obiem.isChecked():
            pen = pyqtgraph.mkPen(color=(100,30,100), width=1, style=QtCore.Qt.SolidLine)
            self.obiem_gr.setData(self.obiem_g[0], self.obiem_g[1], pen=pen)
        else:
            self.obiem_gr.setData([], [], pen=pyqtgraph.mkPen())

    def Chastota(self):
        if self.graphic.chastota_dihaniya.isChecked():
            pen = pyqtgraph.mkPen(color=(0,255,255), width=1, style=QtCore.Qt.SolidLine)
            self.chastota_gr.setData(self.chastota_dihaniya_g[0], self.chastota_dihaniya_g[1], pen=pen)
        else:
            self.chastota_gr.setData([], [], pen=pyqtgraph.mkPen())

    def Potok(self):
        if self.graphic.potok.isChecked():
            pen = pyqtgraph.mkPen(color=(255,0,255), width=1, style=QtCore.Qt.SolidLine)
            self.potok_gr.setData(self.potok_g[0], self.potok_g[1], pen=pen)
        else:
            self.potok_gr.setData([], [], pen=pyqtgraph.mkPen())

    def Minutni(self):
        if self.graphic.minutni_obiem.isChecked():
            pen = pyqtgraph.mkPen(color=(100,200,100), width=1, style=QtCore.Qt.SolidLine)
            self.minutni_gr.setData(self.minutni_obiem_g[0], self.minutni_obiem_g[1], pen=pen)
        else:
            self.minutni_gr.setData([], [], pen=pyqtgraph.mkPen())

    def SpO2(self):
        if self.graphic.SpO2.isChecked():
            pen = pyqtgraph.mkPen(color=(100,50,100), width=1, style=QtCore.Qt.SolidLine)
            self.spo2_gr.setData(self.SpO2_g[0], self.SpO2_g[1], pen=pen)
        else:
            self.spo2_gr.setData([], [], pen=pyqtgraph.mkPen())

    def Pulse(self):
        if self.graphic.pulse.isChecked():
            pen = pyqtgraph.mkPen(color=(0,100,0), width=1, style=QtCore.Qt.SolidLine)
            self.pulse_gr.setData(self.pulse_g[0], self.pulse_g[1], pen=pen)
        else:
            self.pulse_gr.setData([], [], pen=pyqtgraph.mkPen())


    def FiO2(self):
        if self.graphic.FiO2.isChecked():
            pen = pyqtgraph.mkPen(color=(255,0,0), width=1, style=QtCore.Qt.SolidLine)
            FiO2_gr = [[[int(i) for i in y[0].split('.')[::-1]], [int(i) for i in y[1].split(':')], int(y[2])] for y in self.FiO2_gr]
            FiO2_gr = [i[0] + i[1] + [i[2]] for i in FiO2_gr]
            FiO2_gr.sort()
            FiO2_gr_2 = [[FiO2_gr[i][5] for i in range(0,len(FiO2_gr))], [i for i in range(0,len(FiO2_gr))]]
            self.FiO2_sr_gr.setData(FiO2_gr_2[1], FiO2_gr_2[0], pen=pen)
        else:
            self.FiO2_sr_gr.setData([], [], pen=pyqtgraph.mkPen())

    def V(self):
        if self.graphic.V.isChecked():
            pen = pyqtgraph.mkPen(color=(0,255,0), width=1, style=QtCore.Qt.SolidLine)
            V_gr = [[[int(i) for i in y[0].split('.')[::-1]], [int(i) for i in y[1].split(':')], int(y[2])] for y in
                       self.V_gr]
            V_gr = [i[0] + i[1] + [i[2]] for i in V_gr]
            V_gr.sort()
            V_gr_2 = [[V_gr[i][5] for i in range(0, len(V_gr))], [i for i in range(0, len(V_gr))]]
            self.V_sr_gr.setData(V_gr_2[1], V_gr_2[0], pen=pen)
        else:
            self.V_sr_gr.setData([], [], pen=pyqtgraph.mkPen())

    def F(self):
        if self.graphic.F.isChecked():
            pen = pyqtgraph.mkPen(color=(0,0,255), width=1, style=QtCore.Qt.SolidLine)
            F_gr = [[[int(i) for i in y[0].split('.')[::-1]], [int(i) for i in y[1].split(':')], int(y[2])] for y in
                       self.F_gr]
            F_gr = [i[0] + i[1] + [i[2]] for i in F_gr]
            F_gr.sort()
            F_gr_2 = [[F_gr[i][5] for i in range(0, len(F_gr))], [i for i in range(0, len(F_gr))]]
            self.F_sr_gr.setData(F_gr_2[1], F_gr_2[0], pen=pen)
        else:
            self.F_sr_gr.setData([], [], pen=pyqtgraph.mkPen())

    def T(self):
        if self.graphic.T.isChecked():
            pen = pyqtgraph.mkPen(color=(100,30,100), width=1, style=QtCore.Qt.SolidLine)
            T_gr = [[[int(i) for i in y[0].split('.')[::-1]], [int(i) for i in y[1].split(':')], int(y[2])] for y in
                    self.T_gr]
            T_gr = [i[0] + i[1] + [i[2]] for i in T_gr]
            T_gr.sort()
            T_gr_2 = [[T_gr[i][5] for i in range(0, len(T_gr))], [i for i in range(0, len(T_gr))]]
            self.T_sr_gr.setData(T_gr_2[1], T_gr_2[0], pen=pen)
        else:
            self.T_sr_gr.setData([], [], pen=pyqtgraph.mkPen())

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
        if self.inhTable.currentRow() != -1:
            pdf.cell(150, 10, txt='Средняя концетрация O2, %: {}'.format(self.inhTable.item(self.inhTable.currentRow(), 3).text()), ln=1)
            pdf.cell(150, 10, txt='Средняя температура, град. C: {}'.format(self.inhTable.item(self.inhTable.currentRow(), 6).text()), ln=1)
            pdf.cell(150, 10, txt='Дата проведения ингаляции: {}'.format(self.inhTable.item(self.inhTable.currentRow(), 0).text() + " " +
                                                                         self.inhTable.item(self.inhTable.currentRow(), 1).text()), ln=1)
        if not os.path.exists('\\Heliox_temp'):
            os.mkdir('\\Heliox_temp')
        exporter = ImageExporter(self.graphic.graph.getPlotItem())
        exporter.export('\\Heliox_temp\\temp_image.png')
        pdf.image('\\Heliox_temp\\temp_image.png', w=180,h=110)
        pdf.output('\\Heliox_temp\\temp_pdf.pdf', 'F')
        os.system('\\Heliox_temp\\temp_pdf.pdf')

    def printActive2(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.add_font('DejaVuSansBold', '', 'DejaVuSans-Bold.ttf', uni=True)
        pdf.add_font('DejaVuSans', '', 'DejaVuSans.ttf', uni=True)
        pdf.set_font('DejaVuSansBold', '', 20)
        pdf.cell(190, 20, txt='Аппарат ГелиОкс', align='C', ln=1)
        pdf.set_font('DejaVuSans', '', 12)
        pdf.cell(150, 10, txt='ID пациента:{}'.format(self.graphic.id_patient_w.text()), ln=1)
        pdf.cell(150, 10, txt='ФИО пациента:{}'.format(self.graphic.Patientl_w.text()), ln=1)

        now = datetime.now()  # Высчитывание возраста
        temp = self.birhday_w.text().split('.')
        if not temp == '---':
            temp = [int(i) for i in temp]
            year = now.year - temp[2] - 1
            if now.month > temp[1]:
                year += 1
            elif now.month == temp[1] and now.day >= temp[0]:
                year += 1
        else:
            year = '---'

        pdf.cell(150, 10, txt='Возраст: {}                    '
                              'Вес: {}                    '
                              'Рост: {}'.format(year, self.weight_w.text(), self.heigh_w.text()), ln=1)
        pdf.multi_cell(150, 10, txt='Комментарий: {}'.format(self.commText.toPlainText()))
        if self.inhTable.currentRow() != -1:
            pdf.cell(150, 10, txt='Средняя концетрация O2, %: {}'.format(
                self.inhTable.item(self.inhTable.currentRow(), 3).text()), ln=1)
            pdf.cell(150, 10, txt='Средняя температура, град. C: {}'.format(
                self.inhTable.item(self.inhTable.currentRow(), 6).text()), ln=1)
            pdf.cell(150, 10, txt='Дата проведения ингаляции: {}'.format(
                self.inhTable.item(self.inhTable.currentRow(), 0).text() + " " +
                self.inhTable.item(self.inhTable.currentRow(), 1).text()), ln=1)
        if not os.path.exists('\\Heliox_temp'):
            os.mkdir('\\Heliox_temp')
        pen1 = pyqtgraph.mkPen(color=(100,30,100), width=1, style=QtCore.Qt.SolidLine)
        pen2 = pyqtgraph.mkPen(color=(0, 255, 255), width=1, style=QtCore.Qt.SolidLine)
        view_graph = pyqtgraph.PlotWidget()
        view_graph.setBackground('w')
        view_graph.addLegend(offset=[400,-370])
        temp_obiem = view_graph.plot(self.obiem_g[0], self.obiem_g[1], pen=pen1, name='Объём (мл)')
        temp_chastota = view_graph.plot(self.chastota_dihaniya_g[0], self.chastota_dihaniya_g[1], pen=pen2, name='Частота дыхания (1/мин)')
        exporter = ImageExporter(view_graph.getPlotItem())
        exporter.export('\\Heliox_temp\\temp_image2.png')
        pdf.image('\\Heliox_temp\\temp_image2.png', w=180, h=110)
        pdf.output('\\Heliox_temp\\temp_pdf2.pdf', 'F')
        os.system('\\Heliox_temp\\temp_pdf2.pdf')

    def save_graph(self):
        exporter = ImageExporter(self.graphic.graph.getPlotItem())
        exporter.export(QFileDialog.getSaveFileName(self, 'Сохранить график', r'C:\Users\Comp2\Desktop\График.png', filter="Images (*.png)")[0])

    def spisokInh(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.add_font('DejaVuSansBold', '', 'DejaVuSans-Bold.ttf', uni=True)
        pdf.add_font('DejaVuSans', '', 'DejaVuSans.ttf', uni=True)
        pdf.set_font('DejaVuSansBold', '', 20)
        pdf.cell(190, 20, txt='Аппарат ГелиОкс', align='C', ln=1)
        pdf.set_font('DejaVuSans', '', 12)
        pdf.cell(150, 10, txt='ID пациента:{}'.format(self.graphic.id_patient_w.text()), ln=1)
        pdf.cell(150, 10, txt='ФИО пациента:{}'.format(self.graphic.Patientl_w.text()), ln=1)

        now = datetime.now()  # Высчитывание возраста
        temp = self.birhday_w.text().split('.')
        if not temp == ['---']:
            temp = [int(i) for i in temp]
            year = now.year - temp[2] - 1
            if now.month > temp[1]:
                year += 1
            elif now.month == temp[1] and now.day >= temp[0]:
                year += 1
        else:
            year = '---'

        pdf.cell(150, 10, txt='Возраст: {}                    '
                              'Вес: {}                    '
                              'Рост: {}'.format(year, self.weight_w.text(), self.heigh_w.text()), ln=1)
        pdf.multi_cell(150, 10, txt='Комментарий: {}'.format(self.commText.toPlainText()))
        if not os.path.exists('\\Heliox_temp'):
            os.mkdir('\\Heliox_temp')
        pdf.set_font('DejaVuSansBold', '', 15)
        pdf.cell(150, 10, txt='Список ингаляций:', ln=1)
        pdf.set_font('DejaVuSans', '', 11)

        col_width = pdf.w / 7.5
        row_height = pdf.font_size
        spacing = 3
        temp_arr = ['Дата', 'Время', 'Длит,мин', 'FiO2 сред,%','V сред,мл','F сред,1/мин','T сред,град']
        for x in temp_arr:
            pdf.cell(col_width, row_height * spacing,
                     txt=x, border=1)
        pdf.ln(row_height * spacing)
        for y in range(0, self.inhTable.rowCount()):
            for x in range(0, self.inhTable.columnCount()-1):
                pdf.cell(col_width, row_height * spacing,
                         txt=self.inhTable.item(y,x).text(), border=1)
            pdf.ln(row_height * spacing)
        pdf.output('\\Heliox_temp\\temp_pdf3.pdf', 'F')
        os.system('\\Heliox_temp\\temp_pdf3.pdf')

    def othergraphic(self):
        self.graphic.graph.setBackground('w')
        self.graphic.Davlenie_v_maske.setChecked(False)
        self.graphic.koncetracia_O2.setChecked(False)
        self.graphic.temperatura_vdihaemoi_smesi.setChecked(False)
        self.graphic.obiem.setChecked(False)
        self.graphic.chastota_dihaniya.setChecked(False)
        self.graphic.potok.setChecked(False)
        self.graphic.minutni_obiem.setChecked(False)
        self.graphic.SpO2.setChecked(False)
        self.graphic.pulse.setChecked(False)
        self.Davl()
        self.Konc()
        self.Temp()
        self.Obiem()
        self.Chastota()
        self.Potok()
        self.Minutni()
        self.SpO2()
        self.Pulse()
        self.graphic.Davlenie_v_maske.hide()
        self.graphic.koncetracia_O2.hide()
        self.graphic.temperatura_vdihaemoi_smesi.hide()
        self.graphic.obiem.hide()
        self.graphic.chastota_dihaniya.hide()
        self.graphic.potok.hide()
        self.graphic.minutni_obiem.hide()
        self.graphic.SpO2.hide()
        self.graphic.pulse.hide()
        self.graphic.label.hide()
        self.graphic.label_2.hide()
        self.graphic.label_3.hide()
        self.graphic.label_4.hide()
        self.graphic.label_5.hide()
        self.graphic.label_6.hide()
        self.graphic.label_7.hide()
        self.graphic.label_8.hide()
        self.graphic.label_9.hide()
        self.graphic.pechat_grafikov_dihatelnogo_obiema.hide()
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.Davlenie_v_maske)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.koncetracia_O2)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.temperatura_vdihaemoi_smesi)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.obiem)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.chastota_dihaniya)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.potok)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.minutni_obiem)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.SpO2)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.pulse)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_2)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_3)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_4)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_5)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_6)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_7)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_8)
        self.graphic.formLayout.setWidget(-1, QtWidgets.QFormLayout.FieldRole, self.graphic.label_9)
        self.graphic.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.graphic.FiO2)
        self.graphic.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.graphic.FiO2_l)
        self.graphic.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.graphic.V)
        self.graphic.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.graphic.V_l)
        self.graphic.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.graphic.F)
        self.graphic.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.graphic.F_l)
        self.graphic.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.graphic.T)
        self.graphic.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.graphic.T_l)
        self.graphic.FiO2.show()
        self.graphic.V.show()
        self.graphic.F.show()
        self.graphic.T.show()
        self.graphic.FiO2_l.show()
        self.graphic.V_l.show()
        self.graphic.F_l.show()
        self.graphic.T_l.show()
        self.graphic.show()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()