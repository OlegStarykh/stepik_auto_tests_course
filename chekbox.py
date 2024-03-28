import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
# options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-cache')
options.add_argument('--window-size=700,800')
options.add_argument("--disable-blink-features=AutomationControlled")  # Отключение WedDrivera
options.add_argument("--user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://demoqa.com/selectable')
driver.find_element('xpath', "//a[@id='demo-tab-grid']").click()
driver.find_element('xpath', '''//*[@id="row1"]/li[1]''').click()
driver.find_element('xpath', '''//*[@id="row1"]/li[2]''').click()

assert driver.find_element('xpath', '''//*[@id="row1"]/li[1]''').is_enabled()
assert driver.find_element('xpath', '''//*[@id="row1"]/li[2]''').is_enabled()

driver.find_element('xpath', '''//*[@id="row1"]/li[1]''').click()
driver.find_element('xpath', '''//*[@id="row1"]/li[2]''').click()
time.sleep(3)

assert 'active' not in driver.find_element('xpath', '''//*[@id="row1"]/li[1]''').get_attribute('class')
assert 'active' not in driver.find_element('xpath', '''//*[@id="row1"]/li[2]''').get_attribute('class')
