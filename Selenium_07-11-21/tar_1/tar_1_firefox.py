# Link: https://drive.google.com/file/d/1EgFZEOm_OCNvScn1hNdCkRbJy4kxUqa3/view

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

###  ___________1______________
service_firefox = Service(r'D:\QA_Course\webdrivers\geckodriver.exe')
driver_firefox = webdriver.Firefox(service=service_firefox)

driver_firefox.get('https://phptravels.net/api/admin')
driver_firefox.implicitly_wait(10)
email_input = driver_firefox.find_element('name', 'email')
email_input.send_keys('admin@phptravels.com')
password_input = driver_firefox.find_element('name', 'password')
password_input.send_keys('demoadmin')

login_button = driver_firefox.find_element(By.CSS_SELECTOR,'body > div:nth-child(1) > form.form-signin.form-horizontal.wow.fadeIn.animated.animated > button')
login_button.click()

###  ___________2______________
dashboard_text = driver_firefox.find_element(By.CSS_SELECTOR,'body > nav > div > div.navbar-header > a > strong > small')
if dashboard_text.text == 'DASHBOARD':
    print('Success')
else:
    print('Fail')


def logout_close():
    driver_firefox.maximize_window()
    logout_button = driver_firefox.find_element(By.XPATH, "//a[@href='https://phptravels.net/api/admin/logout']")
    logout_button.click()
    print("This is not working because in firefox, even in full-screen, there is another element that covers the 'logout' button.")
    sleep(3)
    driver_firefox.close()


logout_close()
