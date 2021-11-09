# Link: https://drive.google.com/file/d/1EgFZEOm_OCNvScn1hNdCkRbJy4kxUqa3/view


from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

###  ___________1______________
service_chrome = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
service_firefox = Service(r'D:\QA_Course\webdrivers\geckodriver.exe')
# ^ the 'r' stands for 'raw', so the pycharm won't translate parts of the path to control character (such as /n)
driver_chrome = webdriver.Chrome(service=service_chrome)
# driver_firefox = webdriver.Firefox(service=service_firefox)
# we want to give the driver the exact service we want, therefore we give it our service as default .

driver_chrome.get('https://phptravels.net/api/admin')
# in case an element not found- set 10 seconds timeout
driver_chrome.implicitly_wait(10)
email_input = driver_chrome.find_element('name', 'email')
email_input.send_keys('admin@phptravels.com')
password_input = driver_chrome.find_element('name', 'password')
password_input.send_keys('demoadmin')

###  TRYING TO CLICK THE LOGIN BUTTON  T-T ###
# driver_chrome.find_element(by='type', value='submit').click()
# driver_chrome.find_element(by='cssSelector',value="button.dialog-confirm").click()
# driver_chrome.find_element(by='class',value='btn').click()
# driver_chrome.find_element(by='name',value='LOGIN').click()
# driver_chrome.find_element(by='Role',value='button').click()
# driver_chrome.find_element(by=By.cssSelector, value="body > div:nth-child(1) > form.form-signin.form-horizontal.wow.fadeIn.animated.animated > button").click()

login_button = driver_chrome.find_element(By.CSS_SELECTOR,'body > div:nth-child(1) > form.form-signin.form-horizontal.wow.fadeIn.animated.animated > button')
login_button.click()
### hecking FINALLY!!! ###
# driver_chrome.find_element(By.CLASS_NAME, 'btn').click()
# driver_chrome.find_element(by='class_name',value='btn').click()
### ^ also works ###
# pressing ENTER instead of clicking the 'login' button
# password_input.send_keys(Keys.ENTER)


###  ___________2______________
dashboard_text = driver_chrome.find_element(By.CSS_SELECTOR,'body > nav > div > div.navbar-header > a > strong > small')
if dashboard_text.text == 'DASHBOARD':
    print('Success')
else:
    print('Fail')


def logout_close():
    driver_chrome.maximize_window()

    ### TRYING TO GET THE 'LOGOUT' HREF
    # logout_button = driver_chrome.find_element(By.CSS_SELECTOR,'#logout > a')
    # logout_button = driver_chrome.find_element(By.CSS_SELECTOR,'#logout > a > strong')
    # logout_button = driver_chrome.find_element(By.CSS_SELECTOR,'#logout')
    # logout_button = driver_chrome.find_element(By.)
    # logout_button= driver_chrome.find_element(By.xpath("#logout")).click()
    # logout_button= driver_chrome.find_element(By.XPATH,'#logout')
    # logout_button= driver_chrome.find_element(By.XPATH,"https://phptravels.net/api/admin/logout")
    # logout_button= driver_chrome.find_element(By.XPATH,"//a[text()='Logout']")
    logout_button = driver_chrome.find_element(By.XPATH, "//a[@href='https://phptravels.net/api/admin/logout']")

    """ 
    TRYING TO GET SOME ANSWERS FROM STACK OVERFLOW: https://stackoverflow.com/questions/30635228/how-to-click-a-href-link-using-selenium
        #<a href="https://phptravels.net/api/admin/logout"><strong><i class="fa fa-sign-out"></i> Logout</strong></a>
        #//a[text()='Logout']
        #//a[@href='https://phptravels.net/api/admin/logout']
        #"//a[@href='/docs/configuration']"
        # <a href="/docs/configuration">App Configuration</a>
    """

    logout_button.click()
    sleep(3)
    driver_chrome.close()


logout_close()

# sleep(10)
# driver_chrome.close()


# driver.back ->  go back (return)
