
# SETTINGS
# Please download the right driver @ https://selenium-python.readthedocs.io/installation.html#drivers
# and put it in drivers folder

import selenium, os, sys, time, random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from utils import deprecated

def dbg_print(*a):
    print(*a)
dbg_counter1 = 0
class message:
    def __init__(self, body, author, timestamp):
        self.body = body
        self.author = author
        self.timestamp = timestamp
        self.__id = random.randint(0,1000)

    def __repr__(self):
        return "<{0}> \n by <{1}> \t <{2}>".format(self.body, self.author, self.timestamp)

    def __str__(self):
        return self.body

    def __eq__(self, obj):
        return obj.body == self.body and obj.author == self.author and obj.timestamp == self.timestamp and self.__id == obj.__id


class scraper:
    def __init__(self, browser_type='firefox'):
        driver_path = None
        platform = sys.platform
        self.__message_count = 0
        self.__message_box_count = 0
        self.__channel_name = ""
        dbg_print("#of function called, message count, messagebox count")
        driver_class = None

        if browser_type == 'chrome':
            driver_name = 'chromedriver'
            driver_class = webdriver.Chrome
        elif browser_type == 'firefox':
            driver_name = 'geckodriver'
            driver_class = webdriver.Firefox
        else:
            dbg_print('unsupported browser type  ' + browser_type)
            exit(0)


        if 'win' in platform and 'dar' not in platform:
            # Windows
            driver_path = 'drivers/win/' + driver_name + '.exe'
        elif platform == 'darwin':
            # Mac
            driver_path = 'drivers/mac/' + driver_name
        elif platform == 'linux':
            # Linux
            driver_path = 'drivers/linux/' + driver_name
        else:
            dbg_print("Your operating system '" + platform + "' is not supported")
            exit(1)

        self.driver = driver_class(executable_path=driver_path)


    def get_login_page(self):
        self.driver.get("https://discordapp.com/login")


    def send_message(self, message: str):
        textbox = self.driver.find_element_by_xpath("//textarea[@class='textArea-2Spzkt textArea-2Spzkt scrollbarGhostHairline-1mSOM1 scrollbar-3dvm_9']")
        textbox.send_keys(message)
        textbox.send_keys(Keys.RETURN)


    @deprecated
    def fill_credentials(self, username: str, password: str):
        userBox = self.driver.find_element_by_xpath("//input[@class='inputDefault-_djjkz input-cIJ7To size16-14cGz5']")
        passBox = self.driver.find_element_by_xpath("//input[@class='inputDefault-_djjkz input-cIJ7To size16-14cGz5' and @type='password']")
        userBox.send_keys(username)
        passBox.send_keys(password)
        login = self.driver.find_element_by_xpath("//button[@class='marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN' and @type='submit']")
        login.click()


    def get_message(self):
        global dbg_counter1
        dbg_print(dbg_counter1, -self.__message_count-1, -self.__message_box_count-1)
        dbg_counter1 += 1
        try:
            a = self.driver.find_element_by_xpath("//span[@class='channelName-3stJzi']").text
        except:
            dbg_print("Please navigate to a texting screen")
            return 0
        if self.__channel_name != a:
            dbg_print("CHANNEL_CHANGED")
            self.__channel_name = a
            self.__message_count = 0
            self.__message_box_count = 0
        #Message count is for the count of messages inside a message_box
        try:
            message_box = self.driver.find_elements_by_class_name("containerCozy-jafyvG")[-self.__message_box_count-1]
            #print(message_box[0])
        except:
            return None
        author = message_box.find_element_by_class_name("username-_4ZSMR").text
        timestamp = message_box.find_element_by_class_name("timestampCozy-2hLAPV").text
        messages = message_box.find_elements_by_class_name("markup-2BOw-j")[::-1]
        # jk = ""
        # for i in range(len(messages)):
        #     if i == self.__message_count:
        #         jk = "->"
        #     dbg_print(i,"\t" + jk,messages[i].text)

        if (len(messages)-1) == self.__message_count:
            dbg_print("LENMESSAGES == MESSAGECOUNT")
            self.__message_box_count += 1
            self.__message_count = 0
            dbg_print(self.__message_count)
            return 0
        try:
            dbg_print(self.__message_count)
            body = messages[self.__message_count].text
        except Exception as e:
            dbg_print("ERROR",e)

        if body:
            dbg_print(body)
            self.__message_count += 1
            print(-self.__message_count-1)
            return message(body, author, timestamp)


    def get_all_available_messages(self):
        a = []
        for i in range(20):
            a += [self.get_message()]
        return a

    def get_last_message(self):
        message_box = self.driver.find_elements_by_class_name("containerCozy-jafyvG")[-1]
        author = message_box.find_element_by_class_name("username-_4ZSMR").text
        timestamp = message_box.find_element_by_class_name("timestampCozy-2hLAPV").text
        messages = message_box.find_elements_by_class_name("markup-2BOw-j")
        return message(messages[0], author, timestamp)

    def reset(self):
        self.__message_box_count = 0
        self.__message_count = 0


# INFO: Mockuser data: email: mevu@directmail24.net (tempmail) nick: MockUserForTesting#5173 pass: js76TwVj4hzBnwf
'''s = scraper()
s.get_login_page()
s.fill_credentials('mevu@directmail24.net', 'js76TwVj4hzBnwf')
input()
for i in range(25):
    s.get_message()'''

