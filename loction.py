from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={
           query}&crid=3R3N1W3O9WG5T&sprefix=laptops%2Caps%2C265&ref=nb_sb_noss_1")
# link of the product
# class name from where we can get data
elem = driver.find_element(By.CLASS_NAME, "puisg-row")

# print(elem.text) #print data of product
print(elem.get_attribute("outerHTML"))
time.sleep(4)
driver.close()
