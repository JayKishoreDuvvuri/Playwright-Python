"""Checkout page object."""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pageobjects.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):
    """Page object for the checkout pages."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_locators = CheckoutLocators()

    def is_on_checkout_step_one(self) -> bool:
        """Check if currently on checkout step one."""
        return "checkout-step-one.html" in self.get_current_url()

    def is_on_checkout_step_two(self) -> bool:
        """Check if currently on checkout step two."""
        return "checkout-step-two.html" in self.get_current_url()

    def is_on_checkout_complete(self) -> bool:
        """Check if currently on checkout complete page."""
        return "checkout-complete.html" in self.get_current_url()

    # Checkout Step One methods
    def enter_first_name(self, first_name: str):
        """Enter first name."""
        self.fill_input(self.checkout_locators.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str):
        """Enter last name."""
        self.fill_input(self.checkout_locators.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code: str):
        """Enter postal code."""
        self.fill_input(self.checkout_locators.POSTAL_CODE_INPUT, postal_code)

    def fill_checkout_information(
        self, first_name: str, last_name: str, postal_code: str
    ):
        """Fill all checkout information fields."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        """Click continue button."""
        self.click_element(self.checkout_locators.CONTINUE_BUTTON)

    def click_cancel(self):
        """Click cancel button."""
        self.click_element(self.checkout_locators.CANCEL_BUTTON)

    # Checkout Step Two methods
    def get_payment_information(self) -> str:
        """Get payment information text."""
        return self.get_text(self.checkout_locators.PAYMENT_INFO)

    def get_shipping_information(self) -> str:
        """Get shipping information text."""
        return self.get_text(self.checkout_locators.SHIPPING_INFO)

    def get_item_total(self) -> str:
        """Get item total amount."""
        return self.get_text(self.checkout_locators.ITEM_TOTAL)

    def get_tax_amount(self) -> str:
        """Get tax amount."""
        return self.get_text(self.checkout_locators.TAX_LABEL)

    def get_total_amount(self) -> str:
        """Get total amount."""
        return self.get_text(self.checkout_locators.TOTAL_LABEL)

    def click_finish(self):
        """Click finish button."""
        self.click_element(self.checkout_locators.FINISH_BUTTON)

    # Checkout Complete methods
    def get_completion_header(self) -> str:
        """Get completion header text."""
        return self.get_text(self.checkout_locators.COMPLETE_HEADER)

    def get_completion_text(self) -> str:
        """Get completion message text."""
        return self.get_text(self.checkout_locators.COMPLETE_TEXT)

    def click_back_home(self):
        """Click back home button."""
        self.click_element(self.checkout_locators.BACK_HOME_BUTTON)

    def is_pony_express_image_displayed(self) -> bool:
        """Check if pony express image is displayed."""
        return self.is_element_visible(self.checkout_locators.PONY_EXPRESS_IMG)

    # Error handling
    def get_error_message(self) -> str:
        """Get error message text."""
        if self.is_element_visible(self.checkout_locators.ERROR_MESSAGE_TEXT):
            return self.get_text(self.checkout_locators.ERROR_MESSAGE_TEXT)
        return ""

    def is_error_displayed(self) -> bool:
        """Check if error message is displayed."""
        return self.is_element_visible(self.checkout_locators.ERROR_MESSAGE_CONTAINER)

    # Complete checkout flow
    def complete_checkout_flow(self, first_name: str, last_name: str, postal_code: str):
        """Complete the entire checkout flow."""
        if self.is_on_checkout_step_one():
            self.fill_checkout_information(first_name, last_name, postal_code)
            self.click_continue()

        if self.is_on_checkout_step_two():
            self.click_finish()

        return self.is_on_checkout_complete()
