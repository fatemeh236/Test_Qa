from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys



class PagesLogin:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def click_element(self, element):
        self.driver.find_element('xpath', element).click()

    def send_keys_element(self, element, txt):
        self.driver.find_element('xpath', element).send_keys(txt)

    def  delete_text_and_send_keys_element(self, element, txt):
        el = self.driver.find_element('xpath', element)
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(txt)

    def check_element(self, element):
        self.driver.find_element('xpath', element)

    def check_text_in_element(self, element, txt):
        el = self.driver.find_element('xpath', element).text
        print(el)
        assert txt in el

    def check_len_elements(self, element, txt):
        els = self.driver.find_elements('xpath', element)
        el = len(els)
        assert txt == el

    def check_timer_otp(self, element, txt):
        el = self.driver.find_element('xpath', element).text
        print(el)
        assert txt in el



