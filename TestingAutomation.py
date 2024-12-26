from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

# test case 1
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.implicitly_wait(7)
driver.find_element(By.XPATH,"(//*[text()='Swag Labs'])[1]").is_displayed()
time.sleep(5)

print("test case 1 passed")
# test case 2

driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH,"//*[@data-test='add-to-cart-sauce-labs-bike-light']").click()


driver.find_element(By.XPATH,"//*[text()='2']//parent::a").is_displayed()
driver.find_element(By.ID,"remove-sauce-labs-backpack").is_displayed()
time.sleep(5)
print("test case 2 passed")


#test case 3
driver.find_element(By.XPATH,"//*[text()='2']//parent::a").click()
driver.find_element(By.ID,"checkout").click()
driver.find_element(By.ID,"first-name").is_displayed()
time.sleep(5)
print("test case 3 passed")

#test case 4
driver.find_element(By.ID,"cancel").click()
time.sleep(3)
driver.find_element(By.ID,"continue-shopping").click()
time.sleep(3)

# dropwdown handling
dropdown= driver.find_element(By.XPATH,"//*[@data-test='product-sort-container']")
# we will create object for class

obj= Select(dropdown)
obj.select_by_visible_text("Price (high to low)")
time.sleep(7)
driver.find_element(By.XPATH,"(//*[text()='Price (low to high)'])[1]").is_displayed()
print("test case 4 passed")

driver.quit()



