# Speaking alarm clock using Raspberry Pi
#Connect 3.5" LCD and speaker though AUX and run the program with PyQt4 and espeak packages
# Program by: B.Aswinth Raj
# Website: circuitdigest.com
#
# GUI code was created using Qt Designer 

import sys
import time
import os
import random
import subprocess

from threading import Thread
from PyQt4 import QtCore,QtGui #PyQt4 is used for designing the GUI
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
#from espeak import espeak #text to speech sonversion
from time import strftime # To get time from Raspberry pi

#Code from Qt Designer
try:
    _fromUtf8 = QtCore.QtString.fromUtf8
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
        self.pil1 = 0
        self.pil2 = 0
        self.pil3 = 0
        self.pil4 = 0
        self.input = 0
        self.solution = 0
        self.user_solution = 0
        self.sol1 = 0
        self.sol2 = 0
        self.sol3 = 0
        self.sol4 = 0
        self.btn1pushed = False
        self.btn2pushed = False
        self.btn3pushed = False
        self.btn4pushed = False
        self.correct = False
    	
    	MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

    	self.timer = QtCore.QTimer(MainWindow)
    	self.timer.timeout.connect(self.Time)
    	self.timer.start(1000)
    	
    	current_time = QtCore.QTime()
        self.Set_Time = QtGui.QTimeEdit(self.centralwidget)
        self.Set_Time.setObjectName(_fromUtf8("Set_Time"))
    	self.Set_Time.setTime(current_time.currentTime())
        self.gridLayout.addWidget(self.Set_Time, 2, 0, 1, 1)

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


        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.button_pressed)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),self.button_pressed_1)
        #self.pushButton_2.clicked.connect(self.button_pressed_1)

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.button_pressed_2)
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.button_pressed_3)
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)

        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.button_pressed_4)
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

#End of code from Qt Designer
        

    def retranslateUi(self, MainWindow): #update the GUI window 
        print("Dispay Re-translated")
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Alarm curretly Turned off", None))
        self.label_2.setText(_translate("MainWindow", "Soal", None))
        self.pushButton.setText(_translate("MainWindow", "Set Alarm", None))

    #def get_user_solution(self):
        
        
    #def alarm():
        #subprocess.call(['mplayer alarm2.mp3'], shell=True) 

    def Time(self): #Function to compare current time with set time 
        self.Time_LCD.display(strftime("%H"+":"+"%M"+":"+"%S"))
        self.current_h = int (strftime("%H"))
        self.current_m = int (strftime("%M"))

        if (self.current_h == self.alarm_h) and (self.current_m == self.alarm_m) and ((int(strftime("%S"))%15) == 0): #if the both time match 
            
            
            message1 = " The time is " + str(self.alarm_h) + " : " + str(self.alarm_m) + " on " + strftime("%A")
             
            self.label.setText(_translate("MainWindow",message1, None)) #display the message on GUI screen  
            #espeak.synth (message) #speak the message through audio jack
            
            while (self.correct == False):
                print("ALARM ON!!!!!")
                #os.system('mplayer alarm2.mp3') 
                #t = Thread(target=self.alarm,args=(i,) )
                #t.start()
                subprocess.call(['lxterminal -e mplayer alarm2.mp3'], shell=True) 
                number_one = random.randrange(1, 21)
                number_two = random.randrange(1, 21)
                problem = str(number_one) + " + " + str(number_two)
                self.solution = number_one + number_two
                self.label_2.setText(_translate("MainWindow",problem, None)) #display the message on GUI screen  
                
                #self.get_user_solution()
                self.sol1 = self.solution
                self.sol2 = self.solution + random.randrange(1,10)
                self.sol3 = self.solution - random.randrange(1,10)
                self.sol4 = self.solution - random.randrange(1,10)
                while (self.sol4 == self.sol3 ):
                    self.sol4 = self.solution - random.randrange(1,10)
                    
                self.pil1 = random.randrange(1,5)
                    
                self.pil2 = random.randrange(1,5)
                    #global self.pil2
                    
                self.pil3 = random.randrange(1,5)
                    #global self.pil3
                    
                self.pil4 = random.randrange(1,5)
                    #global self.pil4

                if (self.pil2 == self.pil1):

                    self.pil2 = random.randrange(1,5)
                while ((self.pil3 == self.pil2) or (self.pil3 == self.pil1)):
                    self.pil3 = random.randrange(1,5)
                while ((self.pil4 == self.pil3) or (self.pil4 == self.pil2) or (self.pil4 == self.pil1)):
                    self.pil4 = random.randrange(1,5)

                if (self.pil1 == 1):
                    pilihan1 = "1. " + str(self.sol1)
                    self.user_solution = 1
                elif (self.pil1 == 2):
                    pilihan1 = "1. " + str(self.sol2)
                elif (self.pil1 == 3):
                    pilihan1 = "1. " + str(self.sol3)
                else:
                    pilihan1 = "1. " + str(self.sol4)

                if (self.pil2 == 1):
                    pilihan2 = "2. " + str(self.sol1)
                    self.user_solution = 2 
                elif (self.pil2 == 2):
                    pilihan2 = "2. " + str(self.sol2)
                elif (self.pil2 == 3):
                    pilihan2 = "2. " + str(self.sol3)
                else:
                    pilihan2 = "2. " + str(self.sol4)

                if (self.pil3 == 1):
                    pilihan3 = "3. " + str(self.sol1)
                    self.user_solution = 3
                elif (self.pil3 == 2):
                    pilihan3 = "3. " + str(self.sol2)
                elif (self.pil3 == 3):
                    pilihan3 = "3. " + str(self.sol3)
                else:
                    pilihan3 = "3. " + str(self.sol4)

                if (self.pil4 == 1):
                    pilihan4 = "4. " + str(self.sol1)
                    self.user_solution = 4
                elif (self.pil4 == 2):
                    pilihan4 = "4. " + str(self.sol2)
                elif (self.pil4 == 3):
                    pilihan4 = "4. " + str(self.sol3)
                else:
                    pilihan4 = "4. " + str(self.sol4)

                self.pushButton_2.setText(_translate("MainWindow",pilihan1, None))
                self.pushButton_3.setText(_translate("MainWindow",pilihan2, None))
                self.pushButton_4.setText(_translate("MainWindow",pilihan3, None))
                self.pushButton_5.setText(_translate("MainWindow",pilihan4, None))
                print("Enter your answer")
                #self.input = input("Jawabannya? ")
                #time.sleep(10)
                self.btn1pushed = False
                self.btn2pushed = False
                self.btn3pushed = False
                self.btn4pushed = False
                i = 0
                while (( self.btn1pushed != True ) and ( self.btn2pushed != True ) and ( self.btn3pushed != True ) and ( self.btn4pushed != True )):
                   # not doing anything                                                                                                                                                                                                   
                   if ( i % 100000 == 0 ):
                       print("Waiting for user to push button")
                   QtCore.QCoreApplication.processEvents()
                   i += 1;

                
                
                if self.user_solution == self.input:
                    print("Correct.")
                    self.label_2.setText(_translate("MainWindow", "Jawaban Benar, Alarm berhasil dimatikan", None))
                    self.pushButton_2.setText(_translate("MainWindow","", None))
                    self.pushButton_3.setText(_translate("MainWindow","", None))
                    self.pushButton_4.setText(_translate("MainWindow","", None))
                    self.pushButton_5.setText(_translate("MainWindow","", None))
                    self.correct = True
                else:
                    print("Incorrect.")
                    self.correct = False
            

            time.sleep(1)
            

    def button_pressed(self): #when set alarm button is pressed 
        print("Button Pressed")
        alarm_time = str(self.Set_Time.time())
        
        self.alarm_h = int(alarm_time[19:21]) #value of hour is sotred in index value 19 and 20
        self.alarm_m = int (alarm_time[23:25]) #value of minute is sotred in index value 23 and 24
        self.correct = False

        #if ((int(alarm_time[19:20]) < 10) or (int(alarm_time[23:24] < 10))):
        #    self.alarm_h = int(alarm_time[19:20])
        #    self.alarm_m = int(alarm_time[24:25])
        #else:
        #    self.alarm_h = int(alarm_time[19:21]) #value of hour is sotred in index value 19 and 20
        #    self.alarm_m = int(alarm_time[23:25])

        #if (int(alarm_time[23:24]) < 10):
        #    self.alarm_m = int(alarm_time[23:24])
        #else:  
        #    self.alarm_m = int (alarm_time[23:25]) #value of minute is sotred in index value 23 and 24

        message = "Alarm is set at " + str(self.alarm_h) + " : " + str(self.alarm_m) 
        self.label.setText(_translate("MainWindow", message, None)) #display the message on GUI screen  
        #espeak.synth (message) #speak the message through audio jack 

    def button_pressed_1(self):
        #lobal self.btn1pushed
        self.btn1pushed = True
        print("Button 1 pushed")
        self.input = 1
    def button_pressed_2(self):
        #global self.btn2pushed
        self.btn2pushed = True
        print("Button 2 pushed")
        self.input = 2
    def button_pressed_3(self):
        #global self.btn3pushed
        self.btn3pushed = True
        print("Button 3 pushed")
        self.input = 3
    def button_pressed_4(self):
        #global btn4pushed
        self.btn4pushed = True
        print("Button 4 pushed")
        self.input = 4
   
           

if __name__ == "__main__": #main function 
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
