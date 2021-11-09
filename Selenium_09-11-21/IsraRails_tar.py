# Link: https://www.rail.co.il/

"""
        חיפוש של רכבת מסויימת
מאיפה- סבידור
אנטר
לאן- אוניברסיטה
שני חצים למטה
אנטר
חיפוש
wait
פרטים (כפתור חץ למטה) 736


"""
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.rail.co.il/")

# where from textbox - TLV Savidor
sta_from = driver.find_element(By.XPATH,"//div[@id='trainSearchMain']/div/div/div/div/div/input[@role='combobox']")
sta_from.send_keys("סבידור")
sta_from.send_keys(Keys.ENTER)

# where to textbox - TLV university
sta_to = driver.find_element(By.CSS_SELECTOR,"input[aria-label='בחר תחנת יעד']")
sta_to.send_keys("אוניברסיטה")
sta_to.send_keys(Keys.ARROW_DOWN)
sta_to.send_keys(Keys.ARROW_DOWN)
sta_to.send_keys(Keys.ENTER)

sleep(2) # see changes before 'search' button is clicked
# search button
driver.find_element(By.XPATH,"//div[@class='col-md-12 trip']/div[7]/button").click()

# waiting for results to render
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='בחירת רכבת']/div[4]/div[@role='radio']")))

# show details of train number  736 (div[3] might change)
driver.find_element(By.XPATH,"//div[@aria-label='בחירת רכבת']/div[3]/div[@role='radio']").click()