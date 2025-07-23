"""Base page class with common functionality."""

from playwright.sync_api import Page, expect
from pageobjects.base_locators import BaseLocators


class BasePage:
    """Base page class containing common page functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.base_locators = BaseLocators()

    def navigate_to(self, url: str):
        """Navigate to a specific URL."""
        self.page.goto(url)

    def get_page_title(self) -> str:
        """Get the current page title."""
        return self.page.title()

    def get_current_url(self) -> str:
        """Get the current page URL."""
        return self.page.url

    def click_element(self, locator: str):
        """Click on an element."""
        self.page.click(locator)

    def fill_input(self, locator: str, text: str):
        """Fill an input field with text."""
        self.page.fill(locator, text)

    def get_text(self, locator: str) -> str:
        """Get text content of an element."""
        return self.page.locator(locator).text_content()

    def is_element_visible(self, locator: str) -> bool:
        """Check if an element is visible."""
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator: str, timeout: int = 5000):
        """Wait for an element to be visible."""
        self.page.wait_for_selector(locator, timeout=timeout)

    def open_burger_menu(self):
        """Open the hamburger menu."""
        self.click_element(self.base_locators.BURGER_MENU_BUTTON)

    def close_burger_menu(self):
        """Close the hamburger menu."""
        self.click_element(self.base_locators.CLOSE_MENU_BUTTON)

    def click_shopping_cart(self):
        """Click on the shopping cart icon."""
        self.click_element(self.base_locators.SHOPPING_CART_LINK)

    def get_cart_badge_count(self) -> str:
        """Get the number displayed on the cart badge."""
        if self.is_element_visible(self.base_locators.SHOPPING_CART_BADGE):
            return self.get_text(self.base_locators.SHOPPING_CART_BADGE)
        return "0"

    def logout(self):
        """Logout from the application."""
        self.open_burger_menu()
        self.click_element(self.base_locators.LOGOUT_LINK)
