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
options.add_argument("--disable-blink-features=AutomationControlled") #Отключение WedDrivera
# options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")









