from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1, 5):
    driver.get(f"https://www.amazon.in/s?k={
        query}&page{i}&crid=3R3N1W3O9WG5T&sprefix=laptops%2Caps%2C265&ref=nb_sb_noss_1")
    elems = driver.find_elements(By.CLASS_NAME, "puisg-row")
    print(f"{len(elems)} items found")
    print("  ")
    for elem in elems:
        print(elem.text)

    time.sleep(2)
driver.close()
