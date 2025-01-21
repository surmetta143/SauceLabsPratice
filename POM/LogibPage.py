from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginLocators:
    Username = (By.ID, "user-name")
    Password = (By.ID, "password")
    LoginButton = (By.ID, "login-button")
    SwagLabsTitle = (By.XPATH, "(//*[text()='Swag Labs'])[1]")
    def __init__(self, driver):
        self.driver = driver



    def EnterUsername(self,username):
        self.driver.find_element(*self.Username).send_keys(username)
        #self.driver.find_element(By.ID,"user-name").send_keys("standard_user")

    def EnterPassword(self,password):
        self.driver.find_element(*self.Password).send_keys(password)
        #self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
    def ClickLoginButton(self):
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(*self.LoginButton)
        # )
        # element.click()
       self.driver.find_element(*self.LoginButton).click()
    def VerifySwagLabsTitle(self):
        self.driver.find_element(*self.SwagLabsTitle).is_displayed()


