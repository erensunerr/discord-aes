# This file is for Qt GUI
import ui, sys,time, threading
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import scraper, crypto

# -*- coding: utf-8 -*-

def dbg_print(*a):
    print(*a)

with open('message_format_encrypted.html', 'r') as fin:
    message_format = fin.read()

scraper_lock = threading.Lock()
print_lock = threading.Lock()

last_message = scraper.message("-", "-", "-")
get_older_messages_count = 50
def get_older_messages():
    global s, scraper_lock, get_older_messages_count
    if scraper_lock.acquire():
        for i in range(get_older_messages_count):
            print_message_top(s.get_message())
            #print_message_top(scraper.message(str(i), ' ', ' '))
        scraper_lock.release()
        get_older_messages_count += 10



def message_checker():
    global s, scraper_lock, last_message
    if scraper_lock.acquire():
        real_last_message =  s.get_last_message()
        scraper_lock.release()
    else:
        message_checker()

    if real_last_message != last_message:
        last_message = real_last_message
        print(last_message)
        print_message_bottom(last_message)

def message_checker_t():
    pass
    #while True:
     #   message_checker()


def print_message_bottom(message: scraper.message):
    """
    inserts message from bottom to up, like getting f*%!#d in the ass (sorry, no better analogies)
    """
    if message is None:
        dbg_print('no more messages left!')
        return

    global mainWinUi, print_lock
    if print_lock.acquire():

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
    """
    stacks message on top of current selection
    """
    if message is None:
        dbg_print('no more messages left!')
        return

    global mainWinUi, print_lock
    if print_lock.acquire():

        m = message_format.format(author=message.author, timestamp=message.timestamp, body=message.body)
        try:
            mytext = mainWinUi.DisplayMessages.toHtml()
            mainWinUi.DisplayMessages.setText('')
            mainWinUi.DisplayMessages.insertHtml(m + mytext)
        except:
            time.sleep(0.1)
            print('top printing exception')
        print_lock.release()
    else:
        print_message_top(message)


m_check_thread = threading.Thread(target=message_checker_t)

def start_conversation():
    global s, scraper_lock, m_check_thread
    if scraper_lock.acquire():
        l = s.get_all_available_messages()
        for i in l:
            print_message_top(i)
        scraper_lock.release()
    m_check_thread.start()





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
        self.SendButton.clicked.connect(self.send_button_click)
        self.StartConversation.clicked.connect(start_conversation)
        self.actionSave_Messages.triggered.connect(save_messages_trigger)
        self.actionImport_Key.triggered.connect(import_key_trigger)
        self.actionImport_Keylist.triggered.connect(import_keylist_trigger)
        self.actionExport_Your_Key.triggered.connect(export_key_trigger)
        self.actionExport_Your_Keylist.triggered.connect(export_keylist_trigger)
        self.WriteMessage.returnPressed.connect(self.send_button_click)
        self.GetOlderMessages.clicked.connect(get_older_messages)
        self.DisplayMessages.setReadOnly(True)

    def send_button_click(self):
        global s
        m = self.WriteMessage.text()
        s.send_message(m)
        self.WriteMessage.clear()
        return True

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

sys.exit(app.exec_())
