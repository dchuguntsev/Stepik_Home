from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# открываем страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

# считываем 2 числа
num1 = browser.find_element_by_css_selector("#num1").text
num2 = browser.find_element_by_css_selector("#num2").text

# вычисляем их сумму и преобразуем результат в str
sum = int(num1) + int(num2)
sum = str(sum)

# выбираем правильный ответ из списка
select = Select(browser.find_element_by_css_selector("#dropdown"))
select.select_by_value(sum)
browser.find_element_by_css_selector(".btn").click()

# Выходим
time.sleep(10)
browser.quit()
