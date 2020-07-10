# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Гелиокс.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHeaderView, QFormLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1.5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.patientButton = QtWidgets.QPushButton(self.groupBox)
        self.patientButton.setObjectName("patientButton")
        self.verticalLayout_4.addWidget(self.patientButton)
        self.patientList = QtWidgets.QListWidget(self.groupBox)
        self.patientList.setObjectName("patientList")
        self.verticalLayout_4.addWidget(self.patientList)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3.5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        QtGui.QFontDatabase.addApplicationFont(os.getcwd() + '\\' + 'custom_font' + '\\' + 'Zamenhof Plain.otf')
        font = QFont("Zamenhof Plain", 15)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.height = QtWidgets.QLabel(self.groupBox_3)
        self.height.setFont(font)
        self.height.setObjectName("height")
        self.height.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.height)
        self.name = QtWidgets.QLabel(self.groupBox_3)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.name.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.name)
        self.surname = QtWidgets.QLabel(self.groupBox_3)
        self.surname.setFont(font)
        self.surname.setObjectName("surname")
        self.surname.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.surname)
        self.id = QtWidgets.QLabel(self.groupBox_3)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.id.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.id)
        self.patronymic = QtWidgets.QLabel(self.groupBox_3)
        self.patronymic.setFont(font)
        self.patronymic.setObjectName("patronymic")
        self.patronymic.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.patronymic)
        self.weight = QtWidgets.QLabel(self.groupBox_3)
        self.weight.setFont(font)
        self.weight.setObjectName("weight")
        self.weight.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.weight)
        self.birthday = QtWidgets.QLabel(self.groupBox_3)
        self.birthday.setFont(font)
        self.birthday.setObjectName("birthday")
        self.birthday.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.birthday)
        self.gender = QtWidgets.QLabel(self.groupBox_3)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.gender.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.gender)
        self.id_w = QtWidgets.QLabel(self.groupBox_3)
        self.id_w.setFont(font)
        self.id_w.setObjectName("id_w")
        self.id_w.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_w)
        self.name_w = QtWidgets.QLabel(self.groupBox_3)
        self.name_w.setFont(font)
        self.name_w.setObjectName("name_w")
        self.name_w.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_w)
        self.surname_w = QtWidgets.QLabel(self.groupBox_3)
        self.surname_w.setFont(font)
        self.surname_w.setObjectName("surname_w")
        self.surname_w.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.surname_w)
        self.patronymic_w = QtWidgets.QLabel(self.groupBox_3)
        self.patronymic_w.setFont(font)
        self.patronymic_w.setObjectName("patronymic_w")
        self.patronymic_w.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.patronymic_w)
        self.heigh_w = QtWidgets.QLabel(self.groupBox_3)
        self.heigh_w.setFont(font)
        self.heigh_w.setObjectName("height_w")
        self.heigh_w.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.heigh_w)
        self.weight_w = QtWidgets.QLabel(self.groupBox_3)
        self.weight_w.setFont(font)
        self.weight_w.setObjectName("weight_w")
        self.weight_w.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.weight_w)
        self.birhday_w = QtWidgets.QLabel(self.groupBox_3)
        self.birhday_w.setFont(font)
        self.birhday_w.setObjectName("birhday_w")
        self.birhday_w.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.birhday_w)
        self.gender_w = QtWidgets.QLabel(self.groupBox_3)
        self.gender_w.setFont(font)
        self.gender_w.setObjectName("gender_w")
        self.gender_w.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.gender_w)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.commText = QtWidgets.QTextEdit(self.groupBox_2)
        self.commText.setObjectName("commText")
        self.verticalLayout_6.addWidget(self.commText)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.inh_1 = QtWidgets.QPushButton(self.widget_5)
        self.inh_1.setObjectName("inh_1")
        self.horizontalLayout_3.addWidget(self.inh_1)
        self.inh_2 = QtWidgets.QPushButton(self.widget_5)
        self.inh_2.setObjectName("inh_2")
        self.horizontalLayout_3.addWidget(self.inh_2)
        self.inh_3 = QtWidgets.QPushButton(self.widget_5)
        self.inh_3.setObjectName("inh_3")
        self.horizontalLayout_3.addWidget(self.inh_3)
        self.inh_4 = QtWidgets.QPushButton(self.widget_5)
        self.inh_4.setObjectName("inh_4")
        self.horizontalLayout_3.addWidget(self.inh_4)
        self.verticalLayout_7.addWidget(self.widget_5)

        self.inhTable = QtWidgets.QTableWidget(self.groupBox_4)
        self.inhTable.setObjectName("inhTable")
        self.inhTable.setColumnCount(11)
        self.inhTable.setHorizontalHeaderLabels(["Дата", "Время", "Длит, мин", "FiO2 сред", "T сред, град", "V сред, мл", "V в начале инг, мл", "V в конце инг, мл", "F сред, 1/мин", "SpO2, %", "Имя файла"])
        self.inhTable.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.inhTable.horizontalHeader().setMinimumSectionSize(110)


        font_button = QFont("Arial Narrow", 12, QFont.Bold)
        self.patientButton.setFont(font_button)
        font_button = QFont("Arial Narrow", 10, QFont.Bold)
        self.inh_1.setFont(font_button)
        self.inh_2.setFont(font_button)
        self.inh_3.setFont(font_button)
        self.inh_4.setFont(font_button)

        font_box = QFont("Arial Narrow", 10)

        self.groupBox.setFont(font_box)
        self.groupBox_2.setFont(font_box)
        self.groupBox_3.setFont(font_box)
        self.groupBox_4.setFont(font_box)

        self.verticalLayout_7.addWidget(self.inhTable)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Гелиокс"))
        self.groupBox.setTitle(_translate("MainWindow", "Список пациентов"))
        self.patientButton.setText(_translate("MainWindow", "Выбрать список пациентов"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Данные пациента"))
        self.height.setText(_translate("MainWindow", "Рост:"))
        self.name.setText(_translate("MainWindow", "Имя:"))
        self.surname.setText(_translate("MainWindow", "Фамилия:"))
        self.id.setText(_translate("MainWindow", "ID:"))
        self.patronymic.setText(_translate("MainWindow", "Отчество"))
        self.weight.setText(_translate("MainWindow", "Вес:"))
        self.birthday.setText(_translate("MainWindow", "Дата рождения:"))
        self.gender.setText(_translate("MainWindow", "Пол:"))
        self.id_w.setText(_translate("MainWindow", "---"))
        self.name_w.setText(_translate("MainWindow", "---"))
        self.surname_w.setText(_translate("MainWindow", "---"))
        self.patronymic_w.setText(_translate("MainWindow", "---"))
        self.heigh_w.setText(_translate("MainWindow", "---"))
        self.weight_w.setText(_translate("MainWindow", "---"))
        self.birhday_w.setText(_translate("MainWindow", "---"))
        self.gender_w.setText(_translate("MainWindow", "---"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Комментарий"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Данные ингаляций"))
        self.inh_1.setText(_translate("MainWindow", "Показать график ингаляции"))
        self.inh_2.setText(_translate("MainWindow", "Показать все ингаляции"))
        self.inh_3.setText(_translate("MainWindow", "Печать списка всех ингаляций"))
        self.inh_4.setText(_translate("MainWindow", "Детализация ингаляции"))
