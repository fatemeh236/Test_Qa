from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://bimeh.com/")
driver.find_element('xpath', '//div[@class="d-flex flex-column"]//a[@href="/reminder" and text()="یادآور بیمه نامه"]').click()
driver.find_element('xpath', '//input[@id="name"]').send_keys('امین')
driver.find_element('xpath','//input[@placeholder="نام خانوادگی خود را وارد کنید"]').send_keys('پاپی')
driver.find_element('xpath','//input[@placeholder="شماره موبایل خود را وارد کنید"]').send_keys('09000000000')
driver.find_element('xpath','//div[@class="ant-select-selector"]').click()
driver.find_element('xpath','//div[text()="بدنه"]').click()
driver.find_element('xpath','//button[@type="submit"]').click()
driver.find_element('xpath','//input[@id="brands"]').click()
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(('xpath', '//div[text()="پراید"]'))
)
element.click()
driver.find_element('xpath','//input[@id="models"]').click()
driver.find_element('xpath','//div[@title="پراید 131LE"]').click()
input_element = driver.find_element('xpath', '//input[@class="rmdp-input"]')
input_element.click()
sleep(1)
input_element.send_keys(Keys.CONTROL + "a") 
input_element.send_keys(Keys.BACKSPACE) 
input_element.send_keys('۱۴۰۴/۰۲/۰۸')
driver.find_element('xpath','type="submit"').click()
sleep(5)
driver.quit()
