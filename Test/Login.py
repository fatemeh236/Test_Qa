from time import sleep
from Locators import *

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest
from Pages.Login import PagesLogin

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


    def test01(self):
        login = PagesLogin(driver=self.driver)
        login.get_url(url_bimeh)
        sleep(1)
        login.click_element(login_btn_home)
        login.check_element(logo_bimeh_popup)
        login.check_element(link_terms)
        login.check_element(button_close)
        login.send_keys_element(login_input_phone_number, "0 9 3 6 5 4 4 1 7 4 ")
        login.click_element(login_submit_phone_number)
        login.check_element(error_phone_number)
        login.delete_text_and_send_keys_element(login_input_phone_number, '*/7@afghjkklh')
        login.click_element(login_submit_phone_number)
        login.check_element(error_phone_number)
        login.delete_text_and_send_keys_element(login_input_phone_number, phone_number)
        login.click_element(login_submit_phone_number)

    def test02(self):
        login = PagesLogin(driver=self.driver)
        login.check_timer_otp(otp_timer,'120')
        login.check_len_elements(otp_inputs, 5)
        login.check_text_in_element(check_text_phone_number, phone_number)
        login.check_element(logo_bimeh_popup)
        login.check_element(button_close)
        login.click_element(check_phone_number)
        login.delete_text_and_send_keys_element(login_input_phone_number, "09379161533")
        login.click_element(login_submit_phone_number)
        login.check_text_in_element(check_text_phone_number, "09379161533")
        login.send_keys_element(otp_input1, '5')
        login.send_keys_element(otp_input2, '9')
        login.send_keys_element(otp_input3, '8')
        login.send_keys_element(otp_input4, '2')
        login.send_keys_element(otp_input5, '0')
        login.check_element(error_number)

    def test03(self):
        login = PagesLogin(driver=self.driver)
        login.click_element(check_phone_number)
        login.delete_text_and_send_keys_element(login_input_phone_number, phone_number)
        login.click_element(login_submit_phone_number)
        login.click_element(login_btn_password)
        login.check_element(logo_bimeh_popup)
        login.check_element(button_close)
        login.check_element(check_phone_number)
        login.check_text_in_element(check_text_phone_number, phone_number)
        login.send_keys_element(login_input_password, '5555546')
        login.click_element(login_submit_password)
        login.check_element(error_password)
        sleep(1)

    def test04(self):
        login = PagesLogin(driver=self.driver)
        login.click_element(login_forget_password)
        login.check_timer_otp(otp_timer,'120')
        login.check_len_elements(otp_inputs, 5)
        login.check_element(logo_bimeh_popup)
        login.check_element(button_close)
        login.check_element(check_phone_number)
        login.check_text_in_element(check_text_phone_number, phone_number)
        login.send_keys_element(otp_input1, '5')
        login.send_keys_element(otp_input2, '9')
        login.send_keys_element(otp_input3, '8')
        login.send_keys_element(otp_input4, '2')
        login.send_keys_element(otp_input5, '0')
        login.check_element(error_number)

    def test05(self):
        login = PagesLogin(driver=self.driver)
        login.click_element(check_phone_number)
        login.click_element(login_submit_phone_number)
        login.click_element(login_btn_password)
        login.send_keys_element(login_input_password, 'A19223674f')
        login.click_element(submit_button)
        sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(0.5)
        cls.driver.close()
        cls.driver.quit()