# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'discord-pgp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1394, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1394, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuKey = QtWidgets.QMenu(self.menubar)
        self.menuKey.setObjectName("menuKey")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_Key = QtWidgets.QAction(MainWindow)
        self.actionImport_Key.setObjectName("actionImport_Key")
        self.actionExport_Your_Key = QtWidgets.QAction(MainWindow)
        self.actionExport_Your_Key.setObjectName("actionExport_Your_Key")
        self.actionExport_Your_Keylist = QtWidgets.QAction(MainWindow)
        self.actionExport_Your_Keylist.setObjectName("actionExport_Your_Keylist")
        self.actionImport_Keylist = QtWidgets.QAction(MainWindow)
        self.actionImport_Keylist.setObjectName("actionImport_Keylist")
        self.actionSave_Messages = QtWidgets.QAction(MainWindow)
        self.actionSave_Messages.setObjectName("actionSave_Messages")
        self.menuFile.addAction(self.actionSave_Messages)
        self.menuKey.addAction(self.actionImport_Key)
        self.menuKey.addAction(self.actionExport_Your_Key)
        self.menuKey.addAction(self.actionExport_Your_Keylist)
        self.menuKey.addAction(self.actionImport_Keylist)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuKey.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuKey.setTitle(_translate("MainWindow", "Key"))
        self.actionImport_Key.setText(_translate("MainWindow", "Import Key"))
        self.actionExport_Your_Key.setText(_translate("MainWindow", "Export Your Key"))
        self.actionExport_Your_Keylist.setText(_translate("MainWindow", "Export Your Keylist"))
        self.actionImport_Keylist.setText(_translate("MainWindow", "Import Keylist"))
        self.actionSave_Messages.setText(_translate("MainWindow", "Save Messages"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
