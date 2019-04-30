# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_alarm.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
	self.alarm_h = 0
	self.alarm_m = 0
	
	MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(676, 439)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
	
	current_time = QtCore.QTime()
        self.Set_Time = QtGui.QTimeEdit(self.centralwidget)
        self.Set_Time.setObjectName(_fromUtf8("Set_Time"))
	self.Set_Time.setTime(current_time.currentTime())
        self.gridLayout.addWidget(self.Set_Time, 2, 0, 1, 1)

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 2)

        self.Time_LCD = QtGui.QLCDNumber(self.centralwidget)
        self.Time_LCD.setObjectName(_fromUtf8("Time_LCD"))
	self.Time_LCD.setDigitCount(8)
        self.Time_LCD.display(strftime("%H"+":"+"%M"+":"+"%S")) #get time from Pi and display it 

        self.gridLayout.addWidget(self.Time_LCD, 1, 0, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)

        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 4, 2, 1, 1)
	MainWindow.setCentralWidget(self.centralwidget)
        
	self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Set Alarm", None))
        self.label_2.setText(_translate("MainWindow", "Soal", None))
        self.label.setText(_translate("MainWindow", "Your next Alarm is at : ", None))

