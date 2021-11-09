# Link: https://drive.google.com/file/d/1EgFZEOm_OCNvScn1hNdCkRbJy4kxUqa3/view


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

###  ___________1______________
service_chrome = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
service_firefox = Service(r'D:\QA_Course\webdrivers\geckodriver.exe')
driver_chrome = webdriver.Chrome(service=service_chrome)

driver_chrome.get('https://phptravels.net/api/admin')
driver_chrome.implicitly_wait(10)
email_input = driver_chrome.find_element('name', 'email')
email_input.send_keys('admin@phptravels.com')
password_input = driver_chrome.find_element('name', 'password')
password_input.send_keys('demoadmin')

login_button = driver_chrome.find_element(By.CSS_SELECTOR,
                                          'body > div:nth-child(1) > form.form-signin.form-horizontal.wow.fadeIn.animated.animated > button')
login_button.click()

###  ___________2______________
dashboard_text = driver_chrome.find_element(By.CSS_SELECTOR,
                                            'body > nav > div > div.navbar-header > a > strong > small')
if dashboard_text.text == 'DASHBOARD':
    print('Success')
else:
    print('Fail')


def logout_close():
    driver_chrome.maximize_window()
    logout_button = driver_chrome.find_element(By.XPATH, "//a[@href='https://phptravels.net/api/admin/logout']")
    logout_button.click()
    sleep(3)
    driver_chrome.close()


logout_close()
