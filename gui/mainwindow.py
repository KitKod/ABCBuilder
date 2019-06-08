# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ABCBuilderMainWindow(object):
    def setupUi(self, ABCBuilderMainWindow):
        ABCBuilderMainWindow.setObjectName("ABCBuilderMainWindow")
        ABCBuilderMainWindow.resize(1221, 858)
        self.centralwidget = QtWidgets.QWidget(ABCBuilderMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ABCBuilderMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ABCBuilderMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1221, 30))
        self.menubar.setObjectName("menubar")
        ABCBuilderMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ABCBuilderMainWindow)
        self.statusbar.setObjectName("statusbar")
        ABCBuilderMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ABCBuilderMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ABCBuilderMainWindow)

    def retranslateUi(self, ABCBuilderMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ABCBuilderMainWindow.setWindowTitle(_translate("ABCBuilderMainWindow", "ABCBuilder"))


