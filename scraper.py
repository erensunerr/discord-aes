
# SETTINGS
# Please download the right driver @ https://selenium-python.readthedocs.io/installation.html#drivers
# and put it in drivers folder

import selenium, os, sys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class scraper:
    def __init__(self):
        driver_path = None
        platform = sys.platform
        self.__message_count = 0
        self.__channel_name = ""
        if 'win' in platform and 'dar' not in platform:
            # Windows
            driver_path = 'drivers/win/chromedriver.exe'
        elif platform == 'darwin':
            # Mac
            driver_path = 'drivers/mac/chromedriver'
        elif platform == 'linux':
            # Linux
            driver_path = 'drivers/linux/chromedriver'
        else:
            print("Your operating system '" + platform + "' is not supported")
            exit(1)

        self.driver = webdriver.Chrome(driver_path)


    def get_login_page(self):
        self.driver.get("https://discordapp.com/login")


    def send_message(self, message: str):
        textbox = self.driver.find_element_by_xpath("//textarea[@class='textArea-2Spzkt textArea-2Spzkt scrollbarGhostHairline-1mSOM1 scrollbar-3dvm_9']")
        textbox.send_keys(message)
        textbox.send_keys(Keys.RETURN)


    def fill_credentials(self, username: str, password: str):
        userBox = self.driver.find_element_by_xpath("//input[@class='inputDefault-_djjkz input-cIJ7To size16-14cGz5']")
        passBox = self.driver.find_element_by_xpath("//input[@class='inputDefault-_djjkz input-cIJ7To size16-14cGz5' and @type='password']")
        userBox.send_keys(username)
        passBox.send_keys(password)
        login = self.driver.find_element_by_xpath("//button[@class='marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN' and @type='submit']")
        login.click()

    def get_message(self):
        a = self.driver.find_element_by_xpath("//span[@class='channelName-3stJzi']").text
        if self.__channel_name != a:
            self.__channel_name = a
            self.__message_count = 0
        messages = self.driver.find_elements_by_xpath("//div[@class='markup-2BOw-j']")[::-1]
        authors = self.driver.find_elements_by_xpath("//span[@class='username-_4ZSMR']")[::-1]
        print(help(authors[0]))
        #TODO: make this work
        message = {'body':messages[self.__message_count].text, 'author': authors[self.__message_count].text}
        self.__message_count += 1
        return message

s = scraper()
s.get_login_page()
# INFO: Mockuser data: email: mevu@directmail24.net (tempmail) nick: MockUserForTesting#5173 pass: js76TwVj4hzBnwf
s.fill_credentials('mevu@directmail24.net','js76TwVj4hzBnwf')
input("Please press enter when you are done with login")
print(s.get_message())
print(s.get_message())
input()
print(s.get_message())
