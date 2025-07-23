"""Shopping cart page object."""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pageobjects.cart_locators import CartLocators


class CartPage(BasePage):
    """Page object for the shopping cart page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_locators = CartLocators()

    def navigate_to_cart(self):
        """Navigate to the cart page."""
        self.click_shopping_cart()

    def is_on_cart_page(self) -> bool:
        """Check if currently on the cart page."""
        return "cart.html" in self.get_current_url()

    def get_page_title(self) -> str:
        """Get the page title."""
        return self.get_text(self.cart_locators.PAGE_TITLE)

    def get_cart_item_count(self) -> int:
        """Get the number of items in the cart."""
        return len(self.page.locator(self.cart_locators.CART_ITEM).all())

    def get_cart_item_names(self) -> list:
        """Get all item names in the cart."""
        elements = self.page.locator(self.cart_locators.CART_ITEM_LABEL).all()
        return [element.text_content() for element in elements]

    def get_cart_item_prices(self) -> list:
        """Get all item prices in the cart."""
        elements = self.page.locator(self.cart_locators.CART_ITEM_PRICE).all()
        return [element.text_content() for element in elements]

    def get_cart_item_quantities(self) -> list:
        """Get all item quantities in the cart."""
        elements = self.page.locator(self.cart_locators.CART_QUANTITY).all()
        return [element.text_content() for element in elements]

    def continue_shopping(self):
        """Click continue shopping button."""
        self.click_element(self.cart_locators.CONTINUE_SHOPPING_BUTTON)

    def proceed_to_checkout(self):
        """Click checkout button."""
        self.click_element(self.cart_locators.CHECKOUT_BUTTON)

    def is_cart_empty(self) -> bool:
        """Check if the cart is empty."""
        return self.get_cart_item_count() == 0

    def clear_cart(self):
        """Remove all items from the cart."""
        while not self.is_cart_empty():
            remove_buttons = self.page.locator(self.cart_locators.REMOVE_BUTTON).all()
            if remove_buttons:
                remove_buttons[0].click()
            else:
                break
