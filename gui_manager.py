# This file is for Qt GUI
import ui, sys,time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
import scraper, crypto

# -*- coding: utf-8 -*-




def print_message(message: scraper.message):
    global mainWinUi
    file = open('message_format.html', 'r')
    message_format = file.read()
    try:
        mainWinUi.DisplayMessages.insertHtml(message_format.format(body=message.body, author=message.author, timestamp=message.timestamp))
    except:
        time.sleep(0.4)

def send_button_click():
    global s
    m = s.get_message()
    print_message(m)


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
        self.DisplayMessages.setReadOnly(True)

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
s = scraper.scraper()
s.get_login_page()
#s.fill_credentials('mevu@directmail24.net', 'js76TwVj4hzBnwf')
input()
MainWindow.show()
sys.exit(app.exec_())
