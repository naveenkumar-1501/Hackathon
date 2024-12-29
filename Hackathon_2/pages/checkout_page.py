from base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'checkout-button')]")
    BILLING_ADDRESS_FORM = (By.ID, "billing-address-form")
    SHIPPING_METHOD_FORM = (By.ID, "shipping-method-form")
    PAYMENT_METHOD_FORM = (By.ID, "payment-method-form")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'confirm-order-button')]")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def enter_billing_details(self, details):
        for field, value in details.items():
            self.type((By.ID, field), value)
        self.click((By.ID, "continue-button"))

    def choose_shipping_method(self):
        self.click((By.ID, "shipping-method"))
        self.click((By.ID, "continue-button"))

    def choose_payment_method(self):
        self.click((By.ID, "payment-method"))
        self.click((By.ID, "continue-button"))

    def confirm_order(self):
        self.click(self.CONFIRM_ORDER_BUTTON)
