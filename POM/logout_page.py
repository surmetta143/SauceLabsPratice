import time

from selenium.webdriver.common.by import By

class LogOut:
    def __init__(self, driver):
        self.driver = driver

    menu_btn = (By.ID, "react-burger-menu-btn")
    log_out_btn = (By.XPATH,"//*[@data-test='logout-sidebar-link']")
    login_button = (By.ID, "login-button")

    def logout(self):
        self.driver.find_element(*self.menu_btn).click()
        time.sleep(5)
        self.driver.find_element(*self.log_out_btn).click()
        time.sleep(5)

    def Login_Page_displayed(self):
         self.driver.find_element(*self.login_button).is_displayed()

