# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createpointanomalymodule.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 211, 41))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(250, 150, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 160, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 220, 81, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 310, 81, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 590, 141, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 100, 101, 20))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 100, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(250, 220, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 100, 121, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(560, 90, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 150, 81, 20))
        self.label_6.setObjectName("label_6")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(560, 140, 104, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(470, 200, 81, 20))
        self.label_7.setObjectName("label_7")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(560, 190, 104, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(880, 190, 104, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(880, 140, 104, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(820, 100, 51, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(790, 200, 81, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(750, 150, 121, 20))
        self.label_10.setObjectName("label_10")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(880, 90, 104, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Create Point Anomaly Module"))
        self.label_2.setText(_translate("MainWindow", "Percentage"))
        self.label_4.setText(_translate("MainWindow", "Distribution"))
        self.pushButton.setText(_translate("MainWindow", "Preview"))
        self.pushButton_2.setText(_translate("MainWindow", "Create this Module"))
        self.label_3.setText(_translate("MainWindow", "Module Name"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Uniform "))
        self.comboBox.setItemText(1, _translate("MainWindow", "Gaussian"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Skew"))
        self.label_5.setText(_translate("MainWindow", "Number of Values"))
        self.label_6.setText(_translate("MainWindow", "Lowerbound"))
        self.label_7.setText(_translate("MainWindow", "Upperbound"))
        self.label_8.setText(_translate("MainWindow", "Mean "))
        self.label_9.setText(_translate("MainWindow", "Skew Factor"))
        self.label_10.setText(_translate("MainWindow", "Standard Deviation"))
