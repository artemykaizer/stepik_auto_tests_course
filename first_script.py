from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    book_button = browser.find_element(By.ID, "book")

    wait = WebDriverWait(browser, 12)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button.click()

    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)
    result_field = browser.find_element(By.ID, "answer")
    result_field.send_keys(result)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()