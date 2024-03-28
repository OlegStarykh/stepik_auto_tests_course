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

# driver.get("https://www.amazon.com/")
#
# driver.find_element('xpath', "//a[@aria-label='Chairs']").click()
#
# driver.add_cookie({'name': 'username', 'value': 'user123'})
# time.sleep(1)
# driver.refresh()
# assert driver.get_cookie('username')['value'] == 'user123', 'no suspect'
# print(driver.get_cookie('username')['value'])
#
# driver.delete_cookie('skin')
# driver.refresh()
# assert driver.get_cookie('skin') is None


# Добавление и удаление товаров из корзины через cookies

driver.get('https://aza.by/')
ENTER_BUTTON = ('xpath', "//span[@class='text-s-item']")
wait.until(EC.element_to_be_clickable(ENTER_BUTTON)).click()


wait.until(EC.element_to_be_clickable(("xpath", "//input[@id='form_email']"))).send_keys('296402676')
wait.until(EC.element_to_be_clickable(("xpath", "//input[@id='form_pass']"))).send_keys('ghjnjrjk')
driver.find_element("xpath", "//label[@id='recaptcha-anchor-label']").click()


