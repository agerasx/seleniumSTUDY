import time
import math
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://suninjuly.github.io/file_input.html")
firstName = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element(By.NAME, "firstname"))
firstName.send_keys("Alex")
lastName = driver.find_element(By.NAME, "lastname")
lastName.send_keys("Malyshev")
email = driver.find_element(By.NAME, "email")
email.send_keys("gmail@gmail.com")

file = driver.find_element(By.ID, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'requirements.txt')
file.send_keys(file_path)

button = driver.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(3)

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# driver = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# driver.get(link)
#
# x = int(driver.find_element(By.ID, "input_value").text)
# y = calc(x)
# answer = driver.find_element(By.CSS_SELECTOR, ".form-group #answer").send_keys(y)
#
# check = driver.find_element(By.ID, "robotCheckbox")
# driver.execute_script("return arguments[0].scrollIntoView(true);", check)
# check.click()
#
# radio = driver.find_element(By.ID, "robotsRule")
# driver.execute_script("return arguments[0].scrollIntoView(true);", radio)
# radio.click()
#
# button = driver.find_element(By.TAG_NAME, "button")
# driver.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# driver.get("http://suninjuly.github.io/selects1.html")
#
# x = int(driver.find_element(By.ID, "num1").text) + int(driver.find_element(By.ID, "num2").text)
#
# select = Select(driver.find_element(By.ID, "dropdown"))
# select.select_by_value(str(x))

# x_pic = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element(By.ID, "treasure"))
# x = x_pic.get_attribute("valuex")
# y = calc(x)
#
# answer = driver.find_element(By.CSS_SELECTOR, ".form-group #answer").send_keys(y)
#
# driver.find_element(By.ID, "robotCheckbox").click()
# driver.find_element(By.ID, "robotsRule").click()

#driver.find_element(By.CLASS_NAME, "btn-default").click()

# time.sleep(4)
# driver.quit()



