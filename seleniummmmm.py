import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.page_load_strategy = 'normal'
options.add_argument('--window-size=7920,1080')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4")
driver = webdriver.Chrome(options=options)


import math

def calc(x: int):
  return str(math.log(abs(12*math.sin(int(x)))))

driver.get("http://suninjuly.github.io/explicit_wait2.html")

wait = WebDriverWait(driver, 30, poll_frequency=1)
PRICE = ('xpath', '//*[@id="price"]')
wait.until(EC.text_to_be_present_in_element(PRICE, '$100'))
driver.find_element('xpath', '//*[@id="book"]').click()


time.sleep(1)


x = driver.find_element('xpath', '//*[@id="input_value"]').text
y = calc(x)

driver.find_element('xpath', '//*[@id="answer"]').send_keys(y)

button_end = driver.find_element('xpath', "/html/body/form/div/div/button")
button_end.click()
time.sleep(5)
