
# SETTINGS
# Please download the right driver @ https://selenium-python.readthedocs.io/installation.html#drivers
# and put it in drivers folder

import selenium, os, sys


class scraper:
    def __init__(self):
        from selenium import webdriver
        os.chdir("drivers/win")
        self.driver = webdriver.Chrome()

    def get_login_page(self):
        self.driver.get("https://discordapp.com/login")

    def send_message(self, message):
        from selenium.webdriver.common.keys import Keys
        textbox = self.driver.find_element_by_xpath("//textarea[@class='textArea-2Spzkt textArea-2Spzkt scrollbarGhostHairline-1mSOM1 scrollbar-3dvm_9']")
        textbox.send_keys(message)
        textbox.send_keys(Keys.RETURN)

    def get_message(self, num):
        q = []
        for i in range(num,0,-1):
            message = self.driver.find_elements_by_xpath("//div[@class='markup-2BOw-j']")[-num]
            q += [message.text]

s = scraper()
s.get_login_page()
input("Please press enter when you are done with login")
s.send_message("Hey")
print(s.get_message(3))
