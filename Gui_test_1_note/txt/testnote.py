# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Note_test1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(771, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 130, 481, 291))
        self.textEdit.setObjectName("textEdit")
        self.ActionSave = QtWidgets.QPushButton(self.centralwidget)
        self.ActionSave.setGeometry(QtCore.QRect(410, 450, 131, 23))
        self.ActionSave.setObjectName("ActionSave")
        self.ActionExit = QtWidgets.QPushButton(self.centralwidget)
        self.ActionExit.setGeometry(QtCore.QRect(550, 450, 75, 23))
        self.ActionExit.setObjectName("ActionExit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 40, 46, 23))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 47, 14))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 110, 111, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(250, 110, 111, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 47, 14))
        self.label_3.setObjectName("label_3")
        self.ActionSave.raise_()
        self.ActionExit.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.label_3.raise_()
        self.textEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ActionSave.setText(_translate("MainWindow", "Save"))
        self.ActionExit.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Note</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Open_File"))
        self.label_2.setText(_translate("MainWindow", "Date"))
        self.label_3.setText(_translate("MainWindow", "Time"))
        self.ActionExit.clicked.connect(MainWindow.close)
        self.ActionSave.clicked.connect(self.Save)
        
    def Save(self):
        path=QFileDialog.getSaveFileName()
        text=self.textEdit.toPlainText()
        print(text)
        try:
            with open(path[0],'w',encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

