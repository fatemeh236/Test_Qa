from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://bimeh.com/")
driver.find_element('xpath', '//div[@class="d-flex flex-column"]/ul/li/a[@href="/reminder"]').click()
driver.find_element('xpath', '//*[@id="name"]').send_keys('fati')
sleep(5)
driver.quit()