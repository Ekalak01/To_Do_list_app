# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_1_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(322, 247)
        Login.setMinimumSize(QtCore.QSize(322, 247))
        Login.setMaximumSize(QtCore.QSize(322, 247))
        Login.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.Ex_bt = QtWidgets.QPushButton(self.centralwidget)
        self.Ex_bt.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.Ex_bt.setStyleSheet("background:rgb(255, 255, 255)")
        self.Ex_bt.setObjectName("Ex_bt")
        self.user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_edit.setGeometry(QtCore.QRect(110, 70, 116, 20))
        
        
        self.user_edit.setObjectName("user_edit")
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setGeometry(QtCore.QRect(110, 100, 116, 20))
        
       
        
        self.pass_edit.setObjectName("pass_edit")
        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setGeometry(QtCore.QRect(40, 100, 61, 20))
        self.label_pass.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_pass.setObjectName("label_pass")
        self.label_Head = QtWidgets.QLabel(self.centralwidget)
        self.label_Head.setGeometry(QtCore.QRect(110, 30, 100, 23))
        
        self.label_Head.setStyleSheet("Text : rgb(255, 255, 255)")
        self.label_Head.setObjectName("label_Head")
        self.login_bt = QtWidgets.QPushButton(self.centralwidget)
        self.login_bt.setEnabled(True)
        self.login_bt.setGeometry(QtCore.QRect(120, 130, 91, 23))
        
        
        self.login_bt.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login_bt.setStyleSheet("background:rgb(255, 255, 255)")
        self.login_bt.setObjectName("login_bt")
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(50, 70, 41, 20))
        self.label_user.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_user.setObjectName("label_user")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 322, 22))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.Ex_bt.setText(_translate("Login", "Exit"))
        self.label_pass.setText(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\"> Password</span></p></body></html>"))
        self.label_Head.setWhatsThis(_translate("Login", "<html><head/><body><p><span style=\" font-size:10pt;\">LOGIN</span></p><p><br/></p></body></html>"))
        self.label_Head.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0515;\">Login user</span></p></body></html>"))
        self.login_bt.setText(_translate("Login", "Login"))
        self.label_user.setText(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">  User</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

