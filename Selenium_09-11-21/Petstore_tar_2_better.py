##          Randomization       ##
## Link: https://petstore.octoperf.com/actions/Catalog.action
"""
choose random pet
random from the list
change quantities
check the quantity * list price = total cost
total cost + total cost = sub total

"""
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import choice

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://petstore.octoperf.com/actions/Catalog.action")


def str_to_float(str: str):
    if '$' in str:
        return float(str.split('$')[1].replace(",", ""))
    return float(str.replace(",", ""))


# choosing a random animal from the home page sidebar list.
animals = driver.find_elements(By.CSS_SELECTOR, "div#SidebarContent>a")
rand_animal = choice(animals)
rand_animal.click()

# choosing a random animal type from the table
animal_types = driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a")
rand_type = choice(animal_types)
rand_type.click()

# choosing a random animal from the table
animal_items_btn = driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a.Button")
rand_item = choice(animal_items_btn)
rand_item.click()

# initializing cart table and rows variables
cart_table = driver.find_element(By.CSS_SELECTOR, "table>tbody")
cart_table_rows = cart_table.find_elements(By.CSS_SELECTOR, "tr")

# creating a list of quantities for future random choice.
list_quantities = []
for row in cart_table_rows[1:len(cart_table_rows) - 1]:
    cells = row.find_elements(By.CSS_SELECTOR, "td")
    quantity = cells[4].find_element(By.TAG_NAME, "input")
    list_quantities.append(quantity)

# choosing a random quantity for one of the items
rnd_quantity = random.randint(1, 10)  # choosing random quantity to apply
rand_quant_cell = choice(list_quantities)
rand_quant_cell.clear()
rand_quant_cell.send_keys(rnd_quantity)

# updating the quantities
update_cart_btn = driver.find_element(By.NAME, "updateCartQuantities")
update_cart_btn.click()

# updating cart table and rows variables (changed after clicking on 'update cart')
cart_table = driver.find_element(By.CSS_SELECTOR, "table>tbody")
cart_table_rows = cart_table.find_elements(By.CSS_SELECTOR, "tr")

# initializing variable for the sum of the expected sub total
expected_sub_total = 0
# checking total cost for each item in the table
for row in cart_table_rows[1:len(cart_table_rows) - 1]:
    cells = row.find_elements(By.CSS_SELECTOR, "td")
    # getting the values of 'Total Cost', 'Quantity' and 'List Price' columns
    existing_cost = str_to_float(cells[6].text)
    existing_price = str_to_float(cells[5].text)
    existing_quantity = str_to_float(cells[4].find_element(By.TAG_NAME, "input").get_attribute("value"))

    expected_cost = existing_price * existing_quantity  # List Price column * Quantity column = expected Total Cost
    # Checking expected 'Total Cost' against existing.
    if expected_cost == existing_cost:
        print(
            f"Price Passed for row number:{cart_table_rows.index(row)}. Expected: {expected_cost}, Existing: {existing_cost}",
            end="\t")
        expected_sub_total += expected_cost
    else:
        print(
            f"Price FAILED for row number:{cart_table_rows.index(row)}. Expected: {expected_cost}, Existing: {existing_cost}",
            end="\t")
    print()

# getting existing sub total
existing_sub_total = float(driver.find_element(By.CSS_SELECTOR, "td[colspan='7']").text.split('$')[1].replace(",", ""))

# checking sub total
if expected_sub_total == existing_sub_total:
    print(f"Sub Total Passed, expected: {expected_sub_total}, existing: {existing_sub_total}")
else:
    print(f"Sub Total FAILED. expected:{expected_sub_total} existing: {existing_sub_total} ")

sleep(1)
driver.close()
