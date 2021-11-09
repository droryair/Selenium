#Link: https://drive.google.com/file/d/1EgFZEOm_OCNvScn1hNdCkRbJy4kxUqa3/view

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('http://demo.guru99.com/test/newtours')
driver.find_element(By.CSS_SELECTOR, "input[name='userName']").send_keys('tutorial')
driver.find_element(By.CSS_SELECTOR, "input[name='password'][type='password']").send_keys('tutorial')
driver.find_element(By.CSS_SELECTOR, "input[name='submit'][type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "a[href='reservation.php']").click()

oneway = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][name='tripType'][value='oneway']")
roundtrip = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][name='tripType'][value='roundtrip']")

oneway.click()
print(oneway.is_selected())

roundtrip.click()
print(oneway.is_selected())


driver.find_element(By.CSS_SELECTOR, "input[type='radio'][name='servClass'][value='First']").click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[src='images/continue.gif']").click()

sleep(10)
driver.close()
