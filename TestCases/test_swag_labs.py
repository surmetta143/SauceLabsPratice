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
@pytest.mark.sanity
def test_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
    assert driver.title == "Swag Labs"
    print("Test case 1 passed")

@pytest.mark.smoke
def test_add_to_cart(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    products_page = ProductsPage(driver)
    products_page.add_items_to_cart()
    assert products_page.verify_cart_icon()
    print("Test case 2 passed")

@pytest.mark.sanity
def test_checkout_flow(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    products_page = ProductsPage(driver)
    products_page.add_items_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    assert cart_page.verify_checkout_page()
    print("Test case 3 passed")


def test_sort_products(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    products_page = ProductsPage(driver)
    products_page.sort_products("Price (high to low)")
    assert "Price (low to high)" in driver.page_source
    print("Test case 4 passed")

def test_logout_functionality(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
    obj = LogOut(driver)
    obj.logout()
    time.sleep(5)
    obj.Login_Page_displayed()
def test_cart_items(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
    obj = CartItems(driver)
    obj.clic_on_car()
    time.sleep(5)
    obj.verify_cart_page_displayed()
    obj.verify_check_out_btn_displayed()
    obj.verify_continue_shp_btn_displayed()



