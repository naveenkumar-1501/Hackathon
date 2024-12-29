import pytest
from ..pages.home_page import HomePage
from ..pages.login_page import LoginPage
from ..pages.base_page import BasePage


def test_logout(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    base_page = BasePage(driver)

    driver.get("https://demo.nopcommerce.com")

    # Logging in first
    home_page.click_login_link()
    login_page.login("john.doe@example.com", "password123")

    # Logging out
    logout_link = base_page.find_element((By.LINK_TEXT, "Log out"))
    logout_link.click()

    # Verifying logout
    assert "Log in" in driver.page_source
    assert "Register" in driver.page_source
