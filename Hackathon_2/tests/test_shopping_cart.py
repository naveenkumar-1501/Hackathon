import pytest
from ..pages.product_page import ProductPage
from ..pages.cart_page import CartPage

def test_shopping_cart(driver):
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    driver.get("https://demo.nopcommerce.com")
    product_page.search_product("Laptop")
    cart_page.add_to_cart()
    cart_page.go_to_cart()

    assert "Shopping cart" in driver.page_source
