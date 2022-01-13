# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_3_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from os import close
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit
#from test3 import Ui_Form
#from test3 import MyMainWindow
#from test3 import *
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from sc_main import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 247)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Ex_bt = QtWidgets.QPushButton(self.centralwidget)
        self.Ex_bt.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.Ex_bt.setObjectName("Ex_bt")
        self.User_ed = QtWidgets.QLineEdit(self.centralwidget)
        self.User_ed.setGeometry(QtCore.QRect(110, 60, 116, 20))
        self.User_ed.setObjectName("User_ed")
        self.Pass_ed = QtWidgets.QLineEdit(self.centralwidget)
        self.Pass_ed.setGeometry(QtCore.QRect(110, 90, 116, 20))
        self.Pass_ed.setObjectName("Pass_ed")
        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setGeometry(QtCore.QRect(40, 90, 46, 16))
        self.label_pass.setObjectName("label_pass")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(120, 20, 100, 23))
        self.label_login.setObjectName("label_login")
        self.login_bt = QtWidgets.QPushButton(self.centralwidget)
        self.login_bt.setEnabled(True)
        self.login_bt.setGeometry(QtCore.QRect(110, 120, 111, 23))
        self.login_bt.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login_bt.setObjectName("login_bt")
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(50, 60, 33, 16))
        self.label_user.setObjectName("label_user")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 322, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.login_bt.clicked.connect(MainWindow.login)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Ex_bt.setText(_translate("MainWindow", "Exit"))
        self.label_pass.setText(_translate("MainWindow", "Password"))
        self.label_login.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">LOGIN</span></p><p><br/></p></body></html>"))
        self.label_login.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Login user</span></p></body></html>"))
        self.login_bt.setText(_translate("MainWindow", "Login"))
        self.label_user.setText(_translate("MainWindow", "   User"))
    
    """
    def secondscr(self):
        
        #code the 2nd screen here
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        MainWindow.hide()  

        self.login_bt.clicked.connect(lambda:self.closescr(login_window))
    """
    """def closescr(self,Form):
        # hide the screen on exit btn clicked
        self.Form = QtWidgets.QMainWindow()
        
        self.ui = Ui_Form()
        
        self.ui.setupUi(self.Form)
        
        self.Form.show()  
        Form.close() 
       """ 
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QWidget()
    ui = Ui_login_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())
"""
