# This file is for Qt GUI
import ui, sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
# -*- coding: utf-8 -*-

def send_button_click():
    print("send button")


def save_messages_trigger():
    pass

def import_key_trigger():
    pass

def import_keylist_trigger():
    pass

def export_key_trigger():
    pass

def export_keylist_trigger():
    pass

def scrollbar_changed():
    print("Scr")


class TheMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()



class QApplication(QtWidgets.QApplication):
    pass

app = QApplication(sys.argv)
MainWindow = TheMainWindow()
isFull = False

class Ui_MainWindow(ui.Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.SendButton.clicked.connect(send_button_click)
        self.actionSave_Messages.triggered.connect(save_messages_trigger)
        self.actionImport_Key.triggered.connect(import_key_trigger)
        self.actionImport_Keylist.triggered.connect(import_keylist_trigger)
        self.actionExport_Your_Key.triggered.connect(export_key_trigger)
        self.actionExport_Your_Keylist.triggered.connect(export_keylist_trigger)
        self.WriteMessage.returnPressed.connect(send_button_click)
        self.DisplayMessages.horizontalScrollBar().valueChanged.connect(scrollbar_changed)

    def retranslateUi(self, MainWindow):
        super().retranslateUi( MainWindow)

    def asdFullsc(self,a):
        global MainWindow, isFull
        if not(isFull):
            MainWindow.showFullScreen()
            isFull = True
        else:
            MainWindow.showMaximized()
            isFull = False




mainWinUi = Ui_MainWindow()
mainWinUi.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
