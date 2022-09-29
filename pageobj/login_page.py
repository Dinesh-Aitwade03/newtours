from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# https://seleniumbase.io/demo_page
from selenium.webdriver.support.select import Select


class Demo_page:
    textinput_id='myTextInput'
    pre_filledtext_Name='preText2'
    placeholder_id='placeholderText'
    htmlsvg_xpath='//*[@id="svgRect"]'
    inputslidecon_id='mySlider'

    dorpdown_xpath='//*[@id="mySelect"]'
    checkbox1_id='checkBox1'
    sourcedraganddrop_xpath='//*[@id="drop1"]'
    targetdraganddrop_xpath='//*[@id="drop2"]'
    urllink_LINK_TEXT='seleniumbase.com'
    readonlytext_xpath='//*[@id="readOnlyText"]'


    def __init__(self,driver):
        self.driver=driver

    def textinput(self,txt):
        self.driver.find_element(By.ID,self.textinput_id).clear()
        self.driver.find_element(By.ID,self.textinput_id).send_keys(txt)

    def set_prefilled(self,pretext):
        self.driver.find_element(By.NAME,self.pre_filledtext_Name).clear()
        self.driver.find_element(By.NAME,self.pre_filledtext_Name).send_keys(pretext)

    def set_placeholder(self,placetext):
        self.driver.find_element(By.ID,self.placeholder_id).clear()
        self.driver.find_element(By.ID,self.placeholder_id).send_keys(placetext)

    def html_svg(self):
        self.driver.find_element(By.XPATH,self.htmlsvg_xpath).click()

    def input_slider(self):
        sourceele=self.driver.find_element(By.ID,self.inputslidecon_id)
        # targetele=self.driver.find_element(By.ID,self.inputslidecon_id)
        ActionChains(self.driver).drag_and_drop_by_offset(sourceele,0,0).perform()

    def dropdown(self):
        obj=Select(self.driver.find_element(By.XPATH,self.dorpdown_xpath))
        obj.select_by_index(2)
        var =obj.options
        for i in var:
            print(i.text)

    def checkbox(self):

        sel=self.driver.find_element(By.ID,self.checkbox1_id)
        checkk=sel.is_selected()
        if checkk==True:
            pass
        else:
            sel.click()

    def draganddrop(self):

        sourceele=self.driver.find_element(By.XPATH,self.sourcedraganddrop_xpath)
        targetele=self.driver.find_element(By.XPATH,self.targetdraganddrop_xpath)
        ActionChains(self.driver).drag_and_drop(sourceele,targetele).perform()

    def url_link(self):
        self.driver.find_element(By.LINK_TEXT,self.urllink_LINK_TEXT).click()

    def readonlytext(self):
        txt1=self.driver.find_element(By.XPATH,self.readonlytext_xpath).text
        print(txt1)

