import pytest
from ..pages.cart_page import CartPage
from ..pages.checkout_page import CheckoutPage

def test_payment_methods(driver):
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    driver.get("https://demo.nopcommerce.com")
    cart_page.add_to_cart()
    cart_page.go_to_cart()
    checkout_page.proceed_to_checkout()
    billing_details = {
        "BillingNewAddress_FirstName": "John",
        "BillingNewAddress_LastName": "Doe",
        "BillingNewAddress_Email": "john.doe@example.com",
        "BillingNewAddress_Company": "My Company",
        "BillingNewAddress_CountryId": "1",
        "BillingNewAddress_City": "City",
        "BillingNewAddress_Address1": "Address",
        "BillingNewAddress_ZipPostalCode": "00000",
        "BillingNewAddress_PhoneNumber": "1234567890"
    }
    checkout_page.enter_billing_details(billing_details)
    checkout_page.choose_shipping_method()
    checkout_page.choose_payment_method()
    checkout_page.confirm_order()

    assert "Your order has been successfully processed!" in driver.page_source
