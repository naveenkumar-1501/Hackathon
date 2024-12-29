from base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "FirstName")
    LAST_NAME_FIELD = (By.ID, "LastName")
    EMAIL_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

    def register(self, first_name, last_name, email, password, confirm_password):
        self.type(self.FIRST_NAME_FIELD, first_name)
        self.type(self.LAST_NAME_FIELD, last_name)
        self.type(self.EMAIL_FIELD, email)
        self.type(self.PASSWORD_FIELD, password)
        self.type(self.CONFIRM_PASSWORD_FIELD, confirm_password)
        self.click(self.REGISTER_BUTTON)
