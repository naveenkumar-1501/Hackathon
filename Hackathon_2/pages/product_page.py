from base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    SEARCH_FIELD = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def search_product(self, product_name):
        self.type(self.SEARCH_FIELD, product_name)
        self.click(self.SEARCH_BUTTON)
