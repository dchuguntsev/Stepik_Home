from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://SunInJuly.github.io/execute_script.html")

# Считываем число
x = int(browser.find_element_by_css_selector("#input_value").text)

# Скролим окно браузера
browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_css_selector("#input_value"))

# Вставлеям результат работы функции и нажимаем все чек боксы и радиокнопки
browser.find_element_by_css_selector("#answer").send_keys(str(calc(x)))
browser.find_element_by_css_selector("#robotCheckbox").click()
browser.find_element_by_css_selector("#robotsRule").click()

# Отпавляем результат
browser.find_element_by_css_selector("button[type = submit]").click()

# Выходим
time.sleep(5)
browser.quit()



