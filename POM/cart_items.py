from selenium.webdriver.common.by import By

class CartItems:
    def __init__(self, driver):
        self.driver = driver

    cart_btn = (By.XPATH, "//*[@data-test='shopping-cart-link']")
    your_cart_page = (By.XPATH, "//*[text()='Your Cart']")
    contine_shp_btn = (By.XPATH, "//*[@data-test='continue-shopping']")
    chek_out_btn = (By.XPATH, "//*[@data-test='checkout']")

    def clic_on_car(self):
        self.driver.find_element(*self.cart_btn).click()
    def verify_cart_page_displayed(self):
        self.driver.find_element(*self.your_cart_page).is_displayed()

    def verify_continue_shp_btn_displayed(self):
            self.driver.find_element(*self.contine_shp_btn).is_displayed()
    def verify_check_out_btn_displayed(self):
        self.driver.find_element(*self.chek_out_btn).is_displayed()

