import pytest
import time
import os
import math

answer = math.log(int(time.time()))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture
def driver():
    print("\nstart browser for test..")
    options = Options()
    options.page_load_strategy = 'normal'
    options.add_argument('--window-size=920,1080')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--incognito')
    options.add_argument('--disable-cache')
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()


res = []


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1]'])
def test_autorization(link, driver):

    driver.get(link)
    wait = WebDriverWait(driver, 30, poll_frequency=1)
    LOGIN_BUTTON = ('xpath', '//*[@id="ember420"]')
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON), 'Problemmmmmmmmmmmm').click()
    driver.find_element('xpath', '//*[@id="id_login_email"]').send_keys('starikxxxl@mail.ru')
    driver.find_element('xpath', '//*[@id="id_login_password"]').send_keys('ghjnjrjk')
    ENTER_BUTTON = ('xpath', '//*[@id="login_form"]/button')
    wait.until(EC.element_to_be_clickable(ENTER_BUTTON)).click()
    driver.find_element('xpath', '//*[@id="login_form"]/button').click()
    # alert = wait.until(EC.alert_is_present())
    # driver.switch_to.alert
    # alert.dismiss()


    assert wait.until(EC.invisibility_of_element_located(LOGIN_BUTTON)), "Failed registration"

    answer = str(math.log(int(time.time())))
    print(answer)
    INPUT_POLE = ('xpath', '//textarea')
    wait.until(EC.visibility_of_element_located(INPUT_POLE)).clear()
    wait.until(EC.visibility_of_element_located(INPUT_POLE)).send_keys(answer)
    SEND_BUTTON = ('xpath', '//*[@class="attempt-main ember-view"]/div/section/div/div[1]/div[3]/button')
    wait.until(EC.element_to_be_clickable(SEND_BUTTON)).click()
    ANSWER_ = ('xpath', '//*[@class="smart-hints ember-view lesson__hint"]/p')
    x = wait.until(EC.visibility_of_element_located(ANSWER_)).text
    print(x)
    if x != 'Correct!':
        res.append(x)
    print(*res)



