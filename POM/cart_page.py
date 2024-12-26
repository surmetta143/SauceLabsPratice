from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.ID, "checkout")
    cancel_button = (By.ID, "cancel")
    continue_shopping_button = (By.ID, "continue-shopping")
    first_name_input = (By.ID, "first-name")

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def cancel_checkout(self):
        self.driver.find_element(*self.cancel_button).click()

    def continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button).click()

    def verify_checkout_page(self):
        return self.driver.find_element(*self.first_name_input).is_displayed()
