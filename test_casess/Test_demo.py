import time
import allure_pytest

from selenium import webdriver
from pageobj.login_page import Demo_page
import pytest
import time


class Test_demo:
    baseurl = 'https://seleniumbase.io/demo_page'
    txt = 'Ho Dinesh'
    pretext = 'Hi krishna'


    def test_damot(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.demo = Demo_page(self.driver)
        self.demo.textinput(self.txt)
        self.driver.implicitly_wait(10)
        self.demo.set_prefilled(self.pretext)
        time.sleep(3)
        self.driver.close()


    def test_slider(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.obj = Demo_page(self.driver)
        time.sleep(5)
        self.obj.input_slider()
        time.sleep(3)

    def test_drop(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.objdrop=Demo_page(self.driver)
        self.objdrop.dropdown()
        time.sleep(3)

    def test_cheeckbox(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.objdrop = Demo_page(self.driver)
        self.objdrop.checkbox()
        time.sleep(3)

    def test_llink(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.objdrop = Demo_page(self.driver)
        self.objdrop.url_link()
        time.sleep(3)

    def test_readonlly(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.objdrop = Demo_page(self.driver)
        self.objdrop.readonlytext()
        self.driver.implicitly_wait(5)

    def test_drag(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.objdrop = Demo_page(self.driver)
        self.objdrop.checkbox()
        self.objdrop.draganddrop()
        self.driver.quit()



# --html=Reports\\htmlreport.html
# --alluredir='.\\Reports'

# allure serve