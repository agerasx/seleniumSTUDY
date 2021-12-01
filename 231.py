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

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://suninjuly.github.io/redirect_accept.html")

button = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element(By.CLASS_NAME, "btn-primary"))
button.click()

window1 = driver.window_handles[0]
window2 = driver.window_handles[1]

window_active = driver.switch_to.window(window2)

x = WebDriverWait(driver, timeout=4).until((lambda d: int(d.find_element(By.ID, "input_value").text)))
y = calc(x)

answer = driver.find_element(By.ID, "answer").send_keys(y)
button2 = driver.find_element(By.CLASS_NAME, "btn-primary").click()

time.sleep(4)
driver.quit()
