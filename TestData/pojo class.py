from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
    cart_icon = (By.XPATH, "//*[text()='2']//parent::a")
    product_sort_dropdown = (By.XPATH, "//*[@data-test='product-sort-container']")
    remove_backpack = (By.ID, "remove-sauce-labs-backpack")

    def add_items_to_cart(self):
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_bike_light).click()

    def verify_cart_icon(self):
        return self.driver.find_element(*self.cart_icon).is_displayed()

    def sort_products(self, option_text):
        dropdown = self.driver.find_element(*self.product_sort_dropdown)
        Select(dropdown).select_by_visible_text(option_text)
