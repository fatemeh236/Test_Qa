from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

from Locators import *
from Pages.Base import BasePages

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class test_third_party(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test01_click_third_party(self):
        base = BasePages(driver=self.driver)
        base.get_url(url_bimeh)
        base.click_element(third_party_icon)
        base.send_keys_element(plaque_left_side, '11')
        base.send_keys_element(plaque_right_side, '111')
        base.send_keys_element(plaque_iran_code, '11')
        base.send_keys_element(plaque_national_code, '1111111111')


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(0.1)
        cls.driver.close()
        cls.driver.quit()