
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit

class Ui_Form(object):
    
    def setupUi(self, MainWindow):
    
        self.MW = MainWindow
        MainWindow.setObjectName("Form")
        MainWindow.resize(306, 425)
        self.listWidget = QtWidgets.QListWidget(MainWindow)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 261, 311))
        self.listWidget.setObjectName("listWidget")
        self.remove_bt = QtWidgets.QPushButton(MainWindow)
        self.remove_bt.setGeometry(QtCore.QRect(210, 30, 71, 23))
        self.remove_bt.setObjectName("remove_bt")
        self.add_bt = QtWidgets.QPushButton(MainWindow)
        self.add_bt.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.add_bt.setObjectName("add_bt")
        self.label_Head = QtWidgets.QLabel(MainWindow)
        self.label_Head.setGeometry(QtCore.QRect(100, 10, 91, 20))
        self.label_Head.setObjectName("label_Head")
        self.exit_bt = QtWidgets.QPushButton(MainWindow)
        self.exit_bt.setGeometry(QtCore.QRect(110, 380, 75, 23))
        self.exit_bt.setObjectName("exit_bt")

        self.retranslateUi(MainWindow)
        self.action(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def action(self,MainWindow):
        self.exit_bt.clicked.connect(MainWindow.close)
        self.add_bt.clicked.connect(self.Add)
        self.remove_bt.clicked.connect(self.remove)
    
    def Add(self):
        row = self.listWidget.currentRow()
        #QInputDialog.setStyleSheet(self.MW,"QInputDialog{background-color:#C3083F;}")
        text, ok = QInputDialog.getText(self.MW,"Add","Add Task")
        if ok and text is not None:
            self.listWidget.insertItem(row,text)
    
    """def acclose (self):
        global ac_close
        ac_close = True
        print(ac_close)
        MainWindow.close()"""
        
    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is None:
            return
        else:
            item = self.listWidget.takeItem(row)
            del item
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.add_bt.setText(_translate("MainWindow", "Add"))
        self.remove_bt.setText(_translate("MainWindow", "Remove"))
        self.exit_bt.setText(_translate("MainWindow", "Exit"))
        self.label_Head.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  To Do List</span></p></body></html>"))
