from base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class, 'add-to-cart-button']")
    CART_LINK = (By.LINK_TEXT, "Shopping cart")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_LINK)
