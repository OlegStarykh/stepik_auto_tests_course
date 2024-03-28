import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
options.page_load_strategy = 'normal'
options.add_argument('--window-size=7920,1080')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4")
driver = webdriver.Chrome(options=options)

# Шаг 1 - Открыть базовую страницу
driver.get("https://hyperskill.org/login")

# Шаг 2 - Открытие нескольких вкладок
driver.switch_to.new_window("tab")
driver.get("https://www.avito.ru/")
driver.switch_to.new_window("tab")
driver.get("https://www.fontanka.ru/")


# Шаг 3 - Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows)) # Выведем на экран кол-во открытых вкладок

# Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
current_tab = driver.current_window_handle
print(driver.title)
print("Индекс: ", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности

# Шаг 5 - Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
current_tab = driver.current_window_handle
print(driver.title)
print("Индекс: ", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности

# Шаг 5 - Переключение на вкладку по ее индексу
driver.switch_to.window(windows[0])
current_tab = driver.current_window_handle
print(driver.title)
print("Индекс: ", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности
driver.find_element('xpath', "//button[@class='btn btn-auth position-relative btn-link btn-block']").click()
driver.switch_to.window(windows[1])
driver.find_element('xpath', "//button[@class='desktop-lqkwz0']").click()
driver.switch_to.window(windows[2])
driver.find_element('xpath', "//a[@class='RPa3']").click()
