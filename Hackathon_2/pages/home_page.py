from base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    REGISTER_LINK = (By.LINK_TEXT, "Register")

    def click_login_link(self):
        self.click(self.LOGIN_LINK)

    def click_register_link(self):
        self.click(self.REGISTER_LINK)
