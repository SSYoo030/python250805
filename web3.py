from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

from urllib.request import urlretrieve # Importing urlretrieve to download images

input_name = input("Enter the name of the item to search: ")
driver = wb.chrome()
driver.get("https://www.clien.net/service/board/sold")

#약간의 대기시간주기
time.sleep
for i in range(2):
    driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)
    time.sleep(2)
print("Scrolling down...")
