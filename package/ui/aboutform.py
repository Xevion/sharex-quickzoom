# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/aboutform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.resize(428, 138)
        self.label = QtWidgets.QLabel(AboutForm)
        self.label.setGeometry(QtCore.QRect(50, 30, 351, 61))
        self.label.setObjectName("label")

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "About"))
        self.label.setText(_translate("AboutForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Made by <span style=\" font-weight:600;\">Xevion</span> using PyQt, Qt Designer, ImageMagick and more.</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Source on Github | <a href=\"https://github.com/Xevion/sharex-quickzoom\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Xevion/sharex-quickzoom</span></a></p></body></html>"))

from . import resourcefile_rc