from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1602, 926)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")

        # Buttons
        self.real_time_detection_button = QtWidgets.QPushButton(self.central_widget)
        self.real_time_detection_button.setGeometry(QtCore.QRect(70, 100, 191, 51))
        self.real_time_detection_button.setStyleSheet(
            "font: 18pt \"Microsoft YaHei UI\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(105, 154, 214);"
        )
        self.real_time_detection_button.setObjectName("real_time_detection_button")

        self.camera_detection_button = QtWidgets.QPushButton(self.central_widget)
        self.camera_detection_button.setGeometry(QtCore.QRect(350, 100, 191, 51))
        self.camera_detection_button.setStyleSheet(
            "font: 18pt \"Microsoft YaHei UI\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(105, 154, 214);"
        )
        self.camera_detection_button.setObjectName("camera_detection_button")

        self.image_detection_button = QtWidgets.QPushButton(self.central_widget)
        self.image_detection_button.setGeometry(QtCore.QRect(620, 100, 191, 51))
        self.image_detection_button.setStyleSheet(
            "font: 18pt \"Microsoft YaHei UI\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(105, 154, 214);"
        )
        self.image_detection_button.setObjectName("image_detection_button")

        self.video_detection_button = QtWidgets.QPushButton(self.central_widget)
        self.video_detection_button.setGeometry(QtCore.QRect(890, 100, 191, 51))
        self.video_detection_button.setStyleSheet(
            "font: 18pt \"Microsoft YaHei UI\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(105, 154, 214);"
        )
        self.video_detection_button.setObjectName("video_detection_button")

        self.switch_model_button = QtWidgets.QPushButton(self.central_widget)
        self.switch_model_button.setGeometry(QtCore.QRect(1170, 30, 191, 51))
        self.switch_model_button.setStyleSheet(
            "font: 18pt \"Microsoft YaHei UI\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(200, 200, 0);"
        )
        self.switch_model_button.setObjectName("switch_model_button")

        self.exit_button = QtWidgets.QPushButton(self.central_widget)
        self.exit_button.setGeometry(QtCore.QRect(1170, 100, 191, 51))
        self.exit_button.setStyleSheet(
            "font: 18pt \"Microsoft YaHei UI\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(255, 0, 0);"
        )
        self.exit_button.setObjectName("exit_button")

        # Labels and display areas
        self.result_frame = QtWidgets.QLabel(self.central_widget)
        self.result_frame.setGeometry(QtCore.QRect(50, 190, 1111, 661))
        self.result_frame.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.result_frame.setText("")
        self.result_frame.setObjectName("result_frame")

        self.log_text_browser = QtWidgets.QTextBrowser(self.central_widget)
        self.log_text_browser.setGeometry(QtCore.QRect(1160, 190, 361, 661))
        self.log_text_browser.setStyleSheet(
            "background-color: rgba(100, 100, 100, 100);\n"
            "font: 18pt \"Microsoft YaHei UI\";"
        )
        self.log_text_browser.setObjectName("log_text_browser")

        self.background_list_widget = QtWidgets.QListWidget(self.central_widget)
        self.background_list_widget.setGeometry(QtCore.QRect(0, 0, 1601, 901))
        self.background_list_widget.setStyleSheet(
            "background-color: rgba(100, 100, 100, 100);\n"
            "font: 18pt \"Microsoft YaHei UI\";"
        )
        self.background_list_widget.setObjectName("background_list_widget")

        self.title_label = QtWidgets.QLabel(self.central_widget)
        self.title_label.setGeometry(QtCore.QRect(220, 10, 605, 81))
        self.title_label.setStyleSheet(
            "font: 30pt \"华文琥珀\";\n"
            "background-color: rgba(255, 255, 255, 187);"
        )
        self.title_label.setObjectName("title_label")

        # Adjust z-order to ensure correct stacking
        self.background_list_widget.raise_()
        self.image_detection_button.raise_()
        self.camera_detection_button.raise_()
        self.video_detection_button.raise_()
        self.real_time_detection_button.raise_()
        self.switch_model_button.raise_()
        self.result_frame.raise_()
        self.exit_button.raise_()
        self.log_text_browser.raise_()
        self.title_label.raise_()

        MainWindow.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1602, 22))
        self.menu_bar.setObjectName("menu_bar")
        MainWindow.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)
        self.image_detection_button.clicked.connect(self.result_frame.clear)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_detection_button.setText(_translate("MainWindow", "图片检测"))
        self.camera_detection_button.setText(_translate("MainWindow", "摄像头检测"))
        self.video_detection_button.setText(_translate("MainWindow", "视频检测"))
        self.real_time_detection_button.setText(_translate("MainWindow", "共享屏幕检测"))
        self.switch_model_button.setText(_translate("MainWindow", "切换模型"))
        self.exit_button.setText(_translate("MainWindow", "退出"))
        self.title_label.setText(_translate("MainWindow", "基于YOLOX的人物检测系统"))
