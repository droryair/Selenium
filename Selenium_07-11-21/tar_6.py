
"""
DEPRECATED EXERCISE
"""
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# where_from = driver.find_element(By.CSS_SELECTOR,"#fromInput")
# where_to = driver.find_element(By.CSS_SELECTOR,"#toInput")
# calc_dist_btn = driver.find_element((By.LINK_TEXT,'Calculate Distance'))
#
# dest = ''
# max_dist =0
# for i in range(4):
#     where_from.send_keys('tel aviv')
#     where_to = input("Where to? ")
#