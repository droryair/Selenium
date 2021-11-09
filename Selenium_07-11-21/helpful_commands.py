from time import sleep
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service_chrome = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
# ^ the 'r' stands for 'raw', so the pycharm won't translate parts of the path to control character (such as /n)
driver = webdriver.Chrome(service=service_chrome)
driver.get('https://phptravels.net/api/admin')

# in case an element not found- set 10 seconds timeout:
driver.implicitly_wait(10)


# maximise the window to avoid elements covering other elements:
driver.maximize_window()

# linger in order for the tester (us) to see the changes before continuing:
sleep(10)

# go back (return)
driver.back()


textbox = driver.find_element('name', 'email')

# pressing ENTER instead of clicking the 'login' button
# password_input = driver.find_element('name', 'password')
# password_input.send_keys(Keys.ENTER)

"""
.get_attribute("value") VS .text:
.get_attribute("value") -> text from an textbox (that the user enters)
.text-> text from the site (built-in in the html)
"""

# get a textbox's text (from an input field).
textbox.get_attribute("value")
# -> if textbox.get_attribute("value") == 'something'
textbox.get_attribute
# get a text (from the built-in html):
textbox.text

# clear an input box
textbox.clear()

## ========================================
###             LOCATORS                ###
# id                    -> driver.find_element(By.ID,"value")
# name                  -> driver.find_element(By.NAME,"value")
# class name            -> driver.find_element(By.CLASS_NAME,"value")
# css selector          -> driver.find_element(By.CSS_SELECTOR,"tag_name[name='value']")
# xpath                 -> driver.find_element(By.XPATH,"//input[@name='q']")
# tag name              -> driver.find_element(By.TAG_NAME,"tr")
# link text             -> driver.find_element(By.LINK_TEXT,"full_text_of_href_link").click()
# partial link text     -> driver.find_element(By.PARTIAL_LINK_TEXT,"partial_text_of_href_link").click()
# drop-down             -> operator = driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")
#                       -> select_operator = Select(operator)
#                       -> select_operator.select_by_visible_text("*")
# Reference to drop-down: https://juliemr.github.io/protractor-demo/

## FINDING BY MULTIPLE ATTRIBUTES:
# driver.find_element(By.CSS_SELECTORS,"tag_name[name='value'][text='value2']")

## =========================================
###                SYNC                  ###
"""
            Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

wait = WebDriverWait(driver,10)
wait.until(EC.<method>((By.<something>,"value"))) # EC excepts tuple
    Example: wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"td.ng-binding")))

tip: before using wait, we can try to put the program to sleep (sleep()),
and see if the problem is solved (if the sleep() worked, it means that the problem was really sync)
and then we can write the wait commands, and know that it will solve our problem. 
if the sleep() didn't work, it means that writing the wait commands won't work because the problem is not sync.)

"""

## =========================================
###           ActionChains               ###
"""
used in situations where we can't reach elements


from selenium.webdriver import ActionChains
actionChains = ActionChains(driver)
actionChains.move_to_element(hotels).send_keys("Hyat").perform()

"""

## =========================================
###            execute_script            ###

"""
driver.execute_script("arguments[0].click();",element)
driver.execute_script("arguments[0].scrollIntoView();", element)

"""