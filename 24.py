import time
import math
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = driver.find_element(By.ID, "book").click()

x = WebDriverWait(driver, timeout=4).until((lambda d: int(d.find_element(By.ID, "input_value").text)))
y = calc(x)

answer = driver.find_element(By.ID, "answer").send_keys(y)
button2 = driver.find_element(By.ID, "solve").click()

time.sleep(4)
driver.quit()


