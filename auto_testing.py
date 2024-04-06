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

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(options=options)
browser.get(link)

 # Ваш код, который заполняет обязательные поля
input1 = browser.find_element("xpath", '/html/body/div/form/div[1]/div[1]/input')
input1.send_keys("Ivan")
input2 = browser.find_element("xpath", '/html/body/div/form/div[1]/div[2]/input')
input2.send_keys("Petrov")
input3 = browser.find_element("xpath", '/html/body/div/form/div[1]/div[3]/input')
input3.send_keys("asasasa@mail.ru")
input4 = browser.find_element("xpath", '/html/body/div/form/div[2]/div[1]/input')
input4.send_keys("+375463453456")
input5 = browser.find_element("xpath", '/html/body/div/form/div[2]/div[2]/input')
input5.send_keys("Moscow, Tverskaya 9")
button = browser.find_element("xpath", '/html/body/div/form/button')
button.click()
# Отправляем заполненную форму


# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element('xpath', '/html/body/div/h1')
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text, 'Registrtion fail'




