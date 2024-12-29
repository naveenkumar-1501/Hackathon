import pytest
from ..pages.product_page import ProductPage

def test_product_search(driver):
    product_page = ProductPage(driver)

    driver.get("https://demo.nopcommerce.com")
    product_page.search_product("Laptop")

    assert "Laptop" in driver.page_source
