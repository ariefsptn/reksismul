# Speaking alarm clock using Raspberry Pi
#Connect 3.5" LCD and speaker though AUX and run the program with PyQt4 and espeak packages
# Program by: B.Aswinth Raj
# Website: circuitdigest.com
#
# GUI code was created using Qt Designer 

import sys
import time

from PyQt4 import QtCore, QtGui #PyQt4 is used for designing the GUI
from espeak import espeak #text to speech sonversion
from time import strftime # To get time from Raspberry pi

#Code from Qt Designer

#End of code from Qt Designer
        

    def retranslateUi(self, MainWindow): #update the GUI window 
        print("Dispay Re-translated")
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Alarm curretly Turned off", None))
        self.pushButton.setText(_translate("MainWindow", "Set Alarm", None))

    
    def Time(self): #Function to compare current time with set time 
        self.Time_LCD.display(strftime("%H"+":"+"%M"+":"+"%S"))
        self.current_h = int (strftime("%H"))
        self.current_m = int (strftime("%M"))

        if (self.current_h == self.alarm_h) and (self.current_m == self.alarm_m) and ((int(strftime("%S"))%15) == 0): #if the both time match 
            
	while (self.alarm_m < self.alarm_plus ):
	    print("ALARM ON!!!!!")
            
            message1 = " The time is " + str(self.alarm_h) + " : " + str(self.alarm_m) + " on " + strftime("%A")
            message = "Sir, Good morning.. This is your wake up Alarm." + message1
  
            self.label.setText(_translate("MainWindow",message1, None)) #display the message on GUI screen  
            #espeak.synth (message) #speak the message through audio jack 
            time.sleep(1)
            
            

    def button_pressed(self): #when set alarm button is pressed 
        print("Button Pressed")
        alarm_time = str(self.Set_Time.time())
        
        self.alarm_h = int(alarm_time[19:21]) #value of hour is sotred in index value 19 and 20
        self.alarm_m = int (alarm_time[23:25]) #value of minute is sotred in index value 23 and 24
	self.alarm_plus = self.alarm_m + 1

        message = "Alarm is set at " + str(self.alarm_h) + " hours " + str(self.alarm_m) + " minutes"
        self.label.setText(_translate("MainWindow", message, None)) #display the message on GUI screen  
        espeak.synth (message) #speak the message through audio jack 

        

if __name__ == "__main__": #main function 
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
