# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 540)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/images/sharex.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 571, 400))
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName("graphicsView")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(220, 420, 141, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(220, 440, 131, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(350, 420, 241, 61))
        self.submitButton.setObjectName("submitButton")
        self.spinTypeComboxBox = QtWidgets.QComboBox(self.centralwidget)
        self.spinTypeComboxBox.setGeometry(QtCore.QRect(20, 420, 191, 22))
        self.spinTypeComboxBox.setObjectName("spinTypeComboxBox")
        self.spinTypeComboxBox.addItem("")
        self.spinTypeComboxBox.addItem("")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 450, 181, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 470, 71, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        self.menuShareX_Quick_ZOom = QtWidgets.QMenu(self.menubar)
        self.menuShareX_Quick_ZOom.setObjectName("menuShareX_Quick_ZOom")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuShareX_Quick_ZOom.addAction(self.actionAbout)
        self.menubar.addAction(self.menuShareX_Quick_ZOom.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ShareX Quick Zoom"))
        self.graphicsView.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click somewhere to center the zoom or radial blur</p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Overwrite Original File"))
        self.checkBox_2.setText(_translate("MainWindow", "Copy to clipboard"))
        self.submitButton.setText(_translate("MainWindow", "Save and Exit"))
        self.spinTypeComboxBox.setItemText(0, _translate("MainWindow", "Centered Radial / Zoom Blur"))
        self.spinTypeComboxBox.setItemText(1, _translate("MainWindow", "Radial Spin Blur"))
        self.label.setText(_translate("MainWindow", "Threshold"))
        self.menuShareX_Quick_ZOom.setTitle(_translate("MainWindow", "ShareX Quick Zoom"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

from . import resourcefile_rc
