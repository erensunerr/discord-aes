
# SETTINGS
# Please download the right driver @ https://selenium-python.readthedocs.io/installation.html#drivers
# and put it in drivers folder

import selenium, os, sys


class scraper:
    def __init__():
        from selenium import webdriver
        self.driver = webdriver.Firefox()

    def get_login_page():
        self.driver.get("https://discordapp.com/login")

    def send_message(message):
        from selenium.webdriver.common.keys import Keys
        textbox = self.driver.find_element_by_xpath("//textarea[@class='textArea-2Spzkt textArea-2Spzkt scrollbarGhostHairline-1mSOM1 scrollbar-3dvm_9']")
        textbox.send_keys(message)
        textbox.send_keys(Keys.RETURN)

    def get_message(num):
        for i in range(num,0,-1):
            bigbox = self.driver.find_elements_by_xpath("//div[@class='containerCozyBounded-1rKFAn containerCozy-jafyvG container-1YxwTf']")[-num]
            message = self.driver.find_element_by_xpath("")
            ## TODO: finish this and test
