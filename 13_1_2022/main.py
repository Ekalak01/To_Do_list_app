import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
import os
from fs_main import Ui_MainWindow
from sc_main     import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
import json
"""class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)"""


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #############
        parent_dir=QtCore.QDir.currentPath()
        directory="neyto"
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.dirr=path
        self.ui.setupUi(self)
        self.filename = "savefile"
        self.save_file = self.dirr+"\\"+self.filename+'.txt'
        self.read_from_file(self.save_file)
        ###############
        """self.filename = "savefile"
        self.save_file = self.filename+'.json'
        self.read_from_file(self.save_file)"""
    
    def write_to_file(self, file):
        try:
            list_widget = self.ui.listWidget
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            with open(file, 'w') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file {file} could not be written")

    def read_from_file(self, file):
        try:
            list_widget = self.ui.listWidget
            with open(file, 'r') as fin:
                entries = [e.strip() for e in fin.readlines()]
            list_widget.insertItems(0, entries)
        except OSError as err:
            with open(file, 'w'):
                pass
    
    def closeEvent(self, event):
        should_save = QMessageBox.question(self, "Save data", 
                                                     "Should the data be saved?",
                                                     defaultButton = QMessageBox.Yes)
        if should_save == QMessageBox.Yes:
            self.write_to_file(self.save_file)
        return super().closeEvent(event)
    
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.resize(306, 425)
        self.centralwidget = QtWidgets.QWidget(centralWidget)
        self.centralwidget.setObjectName("centralwidget")
        
        """#####
        self.ui.User_ed = QLineEdit(centralWidget)
        self.ui.User_ed.setGeometry(QtCore.QRect(110, 60, 116, 20))
        self.ui.User_ed.setObjectName("User_ed")
        
        self.ui.Pass_ed = QLineEdit(centralWidget)
        self.ui.Pass_ed.setGeometry(QtCore.QRect(110, 90, 116, 20))
        self.ui.Pass_ed.setObjectName("Pass_ed")
        
        self.ui.label_pass = QLabel(centralWidget)
        self.ui.label_pass.setGeometry(QtCore.QRect(40, 90, 46, 16))
        self.ui.label_pass.setObjectName("label_pass")
        
        self.ui.label_login = QLabel(centralWidget)
        self.ui.label_login.setGeometry(QtCore.QRect(120, 20, 100, 23))
        self.ui.label_login.setObjectName("label_login")
        
        self.ui.login_bt = QPushButton(centralWidget)
        #self.ui.login_bt.setEnabled(True)
        self.ui.login_bt.setGeometry(QtCore.QRect(110, 120, 111, 23))
        self.ui.login_bt.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ui.login_bt.setObjectName("login_bt")
        
        self.ui.label_user = QLabel(centralWidget)
        self.ui.label_user.setGeometry(QtCore.QRect(50, 60, 33, 16))
        self.ui.label_user.setObjectName("label_user")
        
        self.ui.Ex_bt = QPushButton(centralWidget)
        self.ui.Ex_bt.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.ui.Ex_bt.setObjectName("Ex_bt")
        
        
        #self.ui.login_bt.clicked.connect(centralWidget)
        QtCore.QMetaObject.connectSlotsByName(centralWidget)
        
        ####
        _translate = QtCore.QCoreApplication.translate
        
        centralWidget.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ui.Ex_bt.setText(_translate("MainWindow", "Exit"))
        self.ui.label_pass.setText(_translate("MainWindow", "Password"))
        self.ui.label_login.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">LOGIN</span></p><p><br/></p></body></html>"))
        self.ui.label_login.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Login user</span></p></body></html>"))
        self.ui.login_bt.setText(_translate("MainWindow", "Login"))
        self.ui.label_user.setText(_translate("MainWindow", "   User"))
        ####"""
        
        gridLayout = QGridLayout(centralWidget)
        gridLayout.addWidget(self.ui.label_login,0,0,1,3, alignment=Qt.AlignCenter)
        
        gridLayout.addWidget(self.ui.label_user, 1,0,1,1)
        gridLayout.addWidget(self.ui.label_pass, 2,0,1,1)
        
        gridLayout.addWidget(self.ui.User_ed, 1, 1,1,1)
        gridLayout.addWidget(self.ui.Pass_ed, 2, 1,1,1)
        
        gridLayout.addWidget(self.ui.login_bt, 3, 0)
        gridLayout.addWidget(self.ui.Ex_bt, 4, 0)
    
    def login(self):
        data=json.load(open('login.json','r'))
        user=self.ui.User_ed.text()
        pw=self.ui.Pass_ed.text()
        try:
            us=False
            for i in range(len(data)):      
                if user == data[i]["user"] and pw == data[i]["password"]: 
                    print("login success")
                    us=True
                    self.hide()
                    self.myDialog = MyMainWindow()
                    self.myDialog.show()
                    break
            if us == False:
                print("invalid user or password")
        except:
            print("Got some error")
    
    """def secondscr(self):
        self.hide()
        self.myDialog = MyMainWindow()
        #self.myDialog = MyDialog()
        self.myDialog.show()"""
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    fsmain = QtWidgets.QWidget()
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())