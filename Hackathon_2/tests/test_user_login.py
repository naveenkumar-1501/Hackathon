import pytest
from ..pages.home_page import HomePage
from ..pages.login_page import LoginPage

def test_user_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    driver.get("https://demo.nopcommerce.com")
    home_page.click_login_link()
    login_page.login("john.doe@example.com", "password123")

    assert "My account" in driver.page_source
