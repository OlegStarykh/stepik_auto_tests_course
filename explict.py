import os
import time
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


driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

driver.find_element('xpath', "//button[@id='populate-text']").click()
TEXT_VISIBLE = ('xpath', "//h2[@id='h2']")
wait.until(EC.text_to_be_present_in_element(TEXT_VISIBLE, 'Selenium Webdriver'), message='Непракатило')

driver.find_element('xpath', "//button[@id='display-other-button']").click()
wait.until(EC.element_to_be_clickable(('xpath', "//button[@id='hidden']")), message='Кнопка не нажимается')

driver.find_element('xpath', "//button[@id='enable-button']").click()
wait.until(EC.element_to_be_clickable(('xpath', "//button[@id='disable']")), message='Кнопка не нажимается')





