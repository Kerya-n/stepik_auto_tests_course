from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# Инициализация браузера
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

# Ожидание, пока цена дома не уменьшится до $100
WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

# Нажимаем на кнопку "Book"
button = browser.find_element(By.ID, "book")
button.click()

#Считать значение для переменной x
num1 = browser.find_element(By.ID, "input_value").text

#Посчитать математическую функцию от x
result = calc(num1)

#Ввести ответ в текстовое поле
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(result)

#Нажимаем кнопку "Submit"
button = browser.find_element(By.ID, "solve") 
button.click()

# Успеваем скопировать код за 30 секунд
time.sleep(10)

# Закрываем браузер после всех манипуляций
browser.quit()
