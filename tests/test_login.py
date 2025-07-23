"""Login page tests."""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:
    """Test cases for login functionality."""

    def test_successful_login(self, page):
        """Test successful login with valid credentials."""
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.navigate_to_login()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_on_inventory_page()
        assert inventory_page.get_page_title() == "Products"

    def test_invalid_username(self, page):
        """Test login with invalid username."""
        login_page = LoginPage(page)

        login_page.navigate_to_login()
        login_page.login("invalid_user", "secret_sauce")

        assert login_page.is_error_displayed()
        print(" Get Error message is: ", login_page.get_error_message)
        assert (
            "Epic sadface: Username and password do not match"
            in login_page.get_error_message()
        )
    

    def test_invalid_password(self, page):
        """Test login with invalid password."""
        login_page = LoginPage(page)

        login_page.navigate_to_login()
        login_page.login("standard_user", "invalid_password")

        assert login_page.is_error_displayed()
        assert (
            "Epic sadface: Username and password do not match"
            in login_page.get_error_message()
        )

    def test_empty_credentials(self, page):
        """Test login with empty credentials."""
        login_page = LoginPage(page)

        login_page.navigate_to_login()
        login_page.click_login_button()

        assert login_page.is_error_displayed()
        assert "Epic sadface: Username is required" in login_page.get_error_message()

    def test_locked_out_user(self, page):
        """Test login with locked out user."""
        login_page = LoginPage(page)

        login_page.navigate_to_login()
        login_page.login("locked_out_user", "secret_sauce")

        assert login_page.is_error_displayed()
        assert (
            "Epic sadface: Sorry, this user has been locked out"
            in login_page.get_error_message()
        )

    def test_error_message_close(self, page):
        """Test closing error message."""
        login_page = LoginPage(page)

        login_page.navigate_to_login()
        login_page.login("invalid_user", "secret_sauce")

        assert login_page.is_error_displayed()

        login_page.close_error_message()

        assert not login_page.is_error_displayed()
