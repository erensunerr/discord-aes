# This file is for Qt GUI
import ui, sys,time, threading
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
import scraper, crypto

# -*- coding: utf-8 -*-

scraper_lock = threading.Lock()
print_lock = threading.Lock()

last_message = scraper.message("-", "-", "-")

def get_older_messages():
    global s, scraper_lock
    if scraper_lock.acquire():
        for i in range(50):
            print_message_top(s.get_message())
        scraper_lock.release()



def message_checker():
    global s, scraper_lock, last_message
    if scraper_lock.acquire():
        real_last_message =  s.get_last_message()
        scraper_lock.release()
    else:
        message_checker()

    if real_last_message != last_message:
        last_message = real_last_message
        print_message_bottom(last_message)

def message_checker_t():
    while True:
        message_checker()

def print_message_bottom(message: scraper.message):
    global mainWinUi, print_lock
    if print_lock.acquire():

        with open('message_format.html', 'r') as fin:
            message_format = fin.read()

        # AttributeError: 'int' object has no attribute 'author'
        m = message_format.format(author=message.author, timestamp=message.timestamp, body=message.body)
        try:
            mytext = mainWinUi.DisplayMessages.toHtml()
            mainWinUi.DisplayMessages.setText('')
            mainWinUi.DisplayMessages.insertHtml(mytext + m)
        except Exception as e:
            print(e)
            print_message_bottom(message)
        print_lock.release()
    else:
        print_message_bottom(message)


def print_message_top(message: scraper.message):
        global mainWinUi, print_lock
        if print_lock.acquire():

            with open('message_format.html', 'r') as fin:
                message_format = fin.read()

            # AttributeError: 'int' object has no attribute 'author'
            m = message_format.format(author=message.author, timestamp=message.timestamp, body=message.body)
            try:
                mytext = mainWinUi.DisplayMessages.toHtml()
                mainWinUi.DisplayMessages.setText('')
                mainWinUi.DisplayMessages.insertHtml(m + mytext)
            except:
                time.sleep(0.1)
            print_lock.release()
        else:
            print_message_top(message)

m_check_thread = threading.Thread(target=message_checker_t)

def start_conversation():
    global s, scraper_lock, m_check_thread
    if scraper_lock.acquire():
        l = s.get_all_available_messages()
        for i in l:
            print_message_bottom(i)
        scraper_lock.release()
    m_check_thread.start()


def send_button_click():
    global s
    #s.send_message('this was sent via geros qt gui')
    m = s.get_message()
    print_message_bottom(m)


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
        self.StartConversation.clicked.connect(start_conversation)
        self.actionSave_Messages.triggered.connect(save_messages_trigger)
        self.actionImport_Key.triggered.connect(import_key_trigger)
        self.actionImport_Keylist.triggered.connect(import_keylist_trigger)
        self.actionExport_Your_Key.triggered.connect(export_key_trigger)
        self.actionExport_Your_Keylist.triggered.connect(export_keylist_trigger)
        self.WriteMessage.returnPressed.connect(send_button_click)
        self.GetOlderMessages.clicked.connect(get_older_messages)
        self.DisplayMessages.setReadOnly(True)

    def retranslateUi(self, MainWindow):
        super().retranslateUi( MainWindow)

    def asdFullsc(self,a):
        global MainWindow, isFull
        if not isFull:
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
