# Link:https://drive.google.com/file/d/1EgFZEOm_OCNvScn1hNdCkRbJy4kxUqa3/view

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://www.phptravels.net/admin')

driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys('admin@phptravels.com')
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys('demoadmin')
driver.find_element(By.CSS_SELECTOR,"button").click()
driver.maximize_window()


### no such button 'Quick Booking".


sleep(10)
driver.close()
