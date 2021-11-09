# Link: https://petstore.octoperf.com/actions/Catalog.action
"""
Home
V click on reptile picture
V click on "RP-LI-02"
V click on "add to cart"
V click on "Return to main menu"
V click on "Dogs" text on the left
V click on "K9-DL-01" ("Dalmation")
V click on "return to dogs"
V in the search bar, type "Manx"
V click on keyboard "Enter"
V click on the picture
V choose "add to cart" for "EST-14"
V change "EST-14"'s quantity to '2'
V click "Update cart"
V click "proceed to checkout"
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://petstore.octoperf.com/actions/Catalog.action")



reptile_pic = driver.find_element(By.CSS_SELECTOR, "area[alt='Reptiles']")
reptile_pic.click()
sleep(0.5)
driver.find_element(By.LINK_TEXT,"RP-LI-02").click()
sleep(0.5)
driver.find_element(By.LINK_TEXT,"Add to Cart").click()
sleep(0.5)
driver.find_element(By.LINK_TEXT,"Return to Main Menu").click()
sleep(0.5)
driver.find_element(By.XPATH,"//div[@id='SidebarContent']/a[2]").click()
sleep(0.5)
driver.find_element(By.LINK_TEXT,"K9-DL-01").click()
sleep(0.5)
driver.find_element(By.LINK_TEXT,"Return to DOGS").click()
sleep(0.5)
search_box = driver.find_element(By.XPATH,"//div[@id='SearchContent']/form/input[1]")
search_box.send_keys("Manx")
sleep(0.5)
search_box.send_keys(Keys.ENTER)
sleep(0.5)
driver.find_element(By.XPATH,"//div[@id='Catalog']/table/tbody/tr[2]/td/a/img").click()
sleep(0.5)
driver.find_element(By.XPATH,"//div[@id='Catalog']/table/tbody/tr/td[5]/a").click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR,"input[name=EST-14]").clear()
driver.find_element(By.CSS_SELECTOR,"input[name=EST-14]").send_keys(2)
sleep(0.5)
driver.find_element(By.CSS_SELECTOR,"input[name=updateCartQuantities]").click()
sleep(0.5)
driver.find_element(By.LINK_TEXT,"Proceed to Checkout").click()

sleep(2)
driver.close()


