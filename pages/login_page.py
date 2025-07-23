"""Login page object."""

from email import message
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pageobjects.login_locators import LoginLocators


class LoginPage(BasePage):
    """Page object for the login page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.login_locators = LoginLocators()

    def navigate_to_login(self):
        """Navigate to the login page."""
        self.navigate_to("https://www.saucedemo.com/")

    def enter_username(self, username: str):
        """Enter username in the username field."""
        self.fill_input(self.login_locators.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """Enter password in the password field."""
        self.fill_input(self.login_locators.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click the login button."""
        self.click_element(self.login_locators.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Perform complete login process."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self) -> str:
        """Get the error message text."""
        try:
            self.page.wait_for_selector(
                self.login_locators.ERROR_MESSAGE_TEXT, timeout=3000
            )
            return self.page.inner_text(self.login_locators.ERROR_MESSAGE_TEXT)
        except Exception as e:
            print(f"[DEBUG] Error message not found: {e}")
            return ""

    def is_error_displayed(self) -> bool:
        """Check if error message is displayed."""
        return self.is_element_visible(self.login_locators.ERROR_MESSAGE_CONTAINER)

    def close_error_message(self):
        """Close the error message."""
        if self.is_error_displayed():
            self.click_element(self.login_locators.ERROR_CLOSE_BUTTON)

    def is_login_button_displayed(self) -> bool:
        """Check if login button is displayed."""
        return self.is_element_visible(self.login_locators.LOGIN_BUTTON)

    def get_login_credentials_info(self) -> str:
        """Get the login credentials information text."""
        return self.get_text(self.login_locators.LOGIN_CREDENTIALS)

    def get_password_info(self) -> str:
        """Get the password information text."""
        return self.get_text(self.login_locators.LOGIN_PASSWORD)
