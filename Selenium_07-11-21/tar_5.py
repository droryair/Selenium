from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://juliemr.github.io/protractor-demo/')
first = driver.find_element(By.CSS_SELECTOR, "input[ng-model='first']")
second = driver.find_element(By.CSS_SELECTOR, "input[ng-model='second']")
driver.find_element(By.CSS_SELECTOR, "select[ng-model='operator']").click()

add = driver.find_element(By.CSS_SELECTOR, "option[value='ADDITION']")
div = driver.find_element(By.CSS_SELECTOR, "option[value='DIVISION']")
mod = driver.find_element(By.CSS_SELECTOR, "option[value='MODULO']")
multi = driver.find_element(By.CSS_SELECTOR, "option[value='MULTIPLICATION']")
sub = driver.find_element(By.CSS_SELECTOR, "option[value='SUBTRACTION']")

calculate = driver.find_element(By.ID,'gobutton')

a = 13
b = 8
div.click()  # don't forget to change the 'if' statement


first.send_keys(a)
second.send_keys(b)
sleep(1)
calculate.click()

answer = driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(3)").text
if answer == str(a/b):  # change sign when changing operation
    print("Pass")
else:
    print(answer)
    print(type(answer))


sleep(5)
driver.close()
