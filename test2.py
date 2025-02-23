from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://bimeh.com/")
driver.find_element('xpath', '//a[@href="/thirdparty" and @title="بیمه شخص ثالث"]').click()
driver.back()
driver.find_element('xpath', '//a[@href="/thirdpartyMotor" and @title="بیمه موتور"]').click()
driver.back()
driver.find_element('xpath', '//a[@title="بیمه بدنه" and @data-tracking-id="sqare-badge"]').click()
driver.back()
driver.find_element('xpath', '//a[@href="/fire" and @title="بیمه آتش سوزی"]').click()
driver.back()
driver.find_element('xpath', '//a[@href="/earthquake" and @ title="بیمه زلزله"]').click()
driver.back()
driver.find_element('xpath', '//a[@href="/holyshrines-travel" and @ title="بیمه سفر کربلا"]').click()
driver.back()
driver.find_element('xpath', '//a[@href="/health" and @title="بیمه تکمیلی درمان"]').click()
driver.back()
driver.find_element('xpath', '//a[@href="/travelplus" and @ title="بیمه مسافرتی سامان" and @data-tracking-id="sqare-badge"]').click()
driver.back()
driver.find_element('xpath', '//a[@href="/travel" and @title="بیمه مسافرتی"]').click()
driver.back()
driver.find_element('xpath','//a[@href="/medical-liability" and @title="بیمه مسئولیت پزشکان"]').click()
driver.back()
driver.find_element('xpath','//a[@href="/elevator" and @title="بیمه آسانسور"]').click()
driver.back()
driver.find_element('xpath','//a[@href="/sports" and @class="newest-bimeh-bar-item"]').click()
driver.back()
driver.find_element('xpath','//a[@href="/personal-accident" and @title="بیمه حوادث انفرادی"]').click()
driver.back()
driver.find_element('xpath','//a[@href="/equipments" and @ title="بیمه موبایل"]').click()
driver.back()
driver.find_element('xpath','//a[@href="/life" and @data-tracking-id="sqare-badge"]').click()
driver.back()



driver.find_element('xpath', '//div[@class="d-flex flex-column"]//a[@href="/reminder" and text()="یادآور بیمه نامه"]').click()

driver.find_element('xpath', '//input[@id="name"]').send_keys('امین')
sleep(5)
import uuid
unique_id = str(uuid.uuid4())
print(unique_id)

driver.quit()