# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yolo_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1602, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tupian = QtWidgets.QPushButton(self.centralwidget)
        self.tupian.setGeometry(QtCore.QRect(620, 100, 191, 51))
        self.tupian.setStyleSheet("font: 18pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 154, 214);")
        self.tupian.setObjectName("tupian")
        self.jiance = QtWidgets.QPushButton(self.centralwidget)
        self.jiance.setGeometry(QtCore.QRect(350, 100, 191, 51))
        self.jiance.setStyleSheet("font: 18pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 154, 214);")
        self.jiance.setObjectName("jiance")
        self.shipin = QtWidgets.QPushButton(self.centralwidget)
        self.shipin.setGeometry(QtCore.QRect(890, 100, 191, 51))
        self.shipin.setStyleSheet("font: 18pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 154, 214);")
        self.shipin.setObjectName("shipin")
        self.shishi = QtWidgets.QPushButton(self.centralwidget)
        self.shishi.setGeometry(QtCore.QRect(70, 100, 191, 51))
        self.shishi.setStyleSheet("font: 18pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 154, 214);")
        self.shishi.setObjectName("shishi")
        self.kuang = QtWidgets.QLabel(self.centralwidget)
        self.kuang.setGeometry(QtCore.QRect(50, 190, 1111, 661))
        self.kuang.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.kuang.setText("")
        self.kuang.setObjectName("kuang")
        self.tuichu = QtWidgets.QPushButton(self.centralwidget)
        self.tuichu.setGeometry(QtCore.QRect(1170, 100, 191, 51))
        self.tuichu.setStyleSheet("font: 18pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.tuichu.setObjectName("tuichu")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1160, 190, 361, 661))
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"font: 18pt \"Microsoft YaHei UI\";")
        self.textBrowser.setObjectName("textBrowser")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 1601, 901))
        self.listWidget.setStyleSheet("background-image: url(\"a3.jpg\")")
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 478, 81))
        self.label_2.setStyleSheet("font: 30pt \"华文琥珀\";\n"
"background-color: rgba(255, 255, 255, 187);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 20, 851, 71))
        self.label.setStyleSheet("font: 28pt \"华文琥珀\";\n"
"")
        self.label.setObjectName("label")
        self.listWidget.raise_()
        self.tupian.raise_()
        self.jiance.raise_()
        self.shipin.raise_()
        self.shishi.raise_()
        self.kuang.raise_()
        self.tuichu.raise_()
        self.textBrowser.raise_()
        self.label_2.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1602, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tupian.clicked.connect(self.kuang.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tupian.setText(_translate("MainWindow", "图片检测"))
        self.jiance.setText(_translate("MainWindow", "摄像头检测"))
        self.shipin.setText(_translate("MainWindow", "视频检测"))
        self.shishi.setText(_translate("MainWindow", "共享屏幕检测"))
        self.tuichu.setText(_translate("MainWindow", "退出"))
        self.label_2.setText(_translate("MainWindow", "原神人物检测系统1.0"))
