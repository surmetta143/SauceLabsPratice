import time

import pytest
from selenium import webdriver
from TestData.test_data import BASE_URL, USERNAME, PASSWORD
from POM.login_page import LoginPage
from POM.products_page import ProductsPage
from POM.cart_page import CartPage
from POM.logout_page import LogOut

from POM.cart_items import CartItems

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()