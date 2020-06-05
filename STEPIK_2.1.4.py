
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    # Перход на нужную вкладку
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск числа с которым необходимо провести расчеты
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Ввод полученного ответа в поле
    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    # Выбор чек-бокса
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    # Выбор радиобатона
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Нажатие на кнопку отправки ответа
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


