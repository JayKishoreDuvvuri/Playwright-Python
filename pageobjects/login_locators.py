"""Locators for the login page."""


class LoginLocators:
    """Locators specific to the login page."""

    # Login form elements
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"

    # Error messages
    ERROR_MESSAGE_CONTAINER = "[data-test='error']"
    ERROR_MESSAGE_TEXT = "h3[data-test='error']"
    ERROR_CLOSE_BUTTON = "[data-test='error-button']"

    # Login credentials info
    LOGIN_CREDENTIALS = "#login_credentials"
    LOGIN_PASSWORD = ".login_password"

    # Page elements
    LOGIN_LOGO = ".login_logo"
    LOGIN_CONTAINER = "#login_button_container"
