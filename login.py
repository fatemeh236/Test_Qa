from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Login_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test01_no_login(self):
        self.driver.get("https://pinvest.ir/")
        self.driver.find_element('xpath', '//a[@class="btn btn-success" and @href="https://my.pinvest.ir/auth"]').click()
        self.driver.find_element('xpath', '//a[@href="https://my.pinvest.ir/auth/register"]')
        self.driver.find_element('xpath', '//a[@href="https://my.pinvest.ir/auth/register"]')
        self.driver.find_element('xpath', '//a[@href="https://my.pinvest.ir/auth/forget"]')
        self.driver.find_element('xpath', '//a[@href="https://pinvest.ir/eula"]')
        self.driver.find_element('xpath', '//a[@href="https://pinvest.ir/eula"]')


    # def test02_no_login(self):
    #     self.driver.find_element('xpath', '//input[@placeholder="کد ملی"]').send_keys('12456378')
    #     self.driver.find_element('xpath', '//input[@placeholder="رمز عبور"]').send_keys('1459762')
    #     self.driver.find_element('xpath', '//button[@type="submit" and  @class="btn btn-primary mt-20px w-100"]').click()
    #     self.driver.find_element('xpath', '//div[@class="invalid-feedback" and text()="کد ملی معتبر نیست."]')

    def test03_no_login(self):
        self.driver.find_element('xpath', '//input[@placeholder="کد ملی"]').send_keys('5920039027')
        self.driver.find_element('xpath', '//input[@placeholder="رمز عبور"]').send_keys('1459762')
        self.driver.find_element('xpath', '//button[@type="submit" and  @class="btn btn-primary mt-20px w-100"]').click()
        self.driver.find_element('xpath', '//div[text()="اطلاعات ورود نامعتبر است."]')


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(0.5)
        cls.driver.close()
        cls.driver.quit()