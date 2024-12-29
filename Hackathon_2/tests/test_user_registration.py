import pytest
from ..pages.home_page import HomePage
from ..pages.register_page import RegisterPage

def test_user_registration(driver):
    home_page = HomePage(driver)
    register_page = RegisterPage(driver)

    driver.get("https://demo.nopcommerce.com")
    home_page.click_register_link()
    register_page.register("John", "Doe", "john.doe@example.com", "password123", "password123")

    assert "Your registration completed" in driver.page_source
