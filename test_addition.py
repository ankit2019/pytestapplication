import pytest
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class testaddition:
    driver = None

    @pytest.fixture()
    def Setup(self):
        testaddition.driver = webdriver.Chrome(executable_path="D:\\Ankit\\eclipse\\CalcualtorWebApplication\\Driver\\chromedriver.exe")
        testaddition.driver.get("file:///D:/Ankit/project/CalcualtorWebApplication/src/main/webapp/Calculator.html")

    def testAdditionwithpositiveValues(self, Setup):
        ButtonEight = testaddition.driver.find_element_by_css_selector("input[value='9']")
        Buttonplus = testaddition.driver.find_element_by_css_selector("input[value='+']")
        ButtonFour = testaddition.driver.find_element_by_css_selector("input[value='4']")
        ButtonEqual = testaddition.driver.find_element_by_css_selector("input[value='=']")
        ButtonEdit = testaddition.driver.find_element_by_id("result")

        ButtonEight.click()
        Buttonplus.click()
        ButtonFour.click()
        ButtonEqual.click()

        ActualResult = ButtonEdit.get_attributes("values")
        assert ActualResult == "13", "Addition error"
