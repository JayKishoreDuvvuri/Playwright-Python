"""Inventory page object."""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pageobjects.inventory_locators import InventoryLocators


class InventoryPage(BasePage):
    """Page object for the inventory/products page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.inventory_locators = InventoryLocators()

    def is_on_inventory_page(self) -> bool:
        """Check if currently on the inventory page."""
        return "inventory.html" in self.get_current_url()

    def get_page_title(self) -> str:
        """Get the page title."""
        return self.get_text(self.inventory_locators.PAGE_TITLE)

    def get_product_count(self) -> int:
        """Get the number of products displayed."""
        return len(self.page.locator(self.inventory_locators.INVENTORY_ITEM).all())

    def get_product_names(self) -> list:
        """Get all product names."""
        elements = self.page.locator(self.inventory_locators.INVENTORY_ITEM_NAME).all()
        return [element.text_content() for element in elements]

    def get_product_prices(self) -> list:
        """Get all product prices."""
        elements = self.page.locator(self.inventory_locators.INVENTORY_ITEM_PRICE).all()
        return [element.text_content() for element in elements]

    def add_product_to_cart_by_name(self, product_name: str):
        """Add a product to cart by its name."""
        product_locator = f"[data-test='inventory-item-name'][text()='{product_name}']"
        product_container = self.page.locator(product_locator).locator("../..")
        add_button = product_container.locator(
            self.inventory_locators.ADD_TO_CART_BUTTON
        )
        add_button.click()

    def add_backpack_to_cart(self):
        """Add Sauce Labs Backpack to cart."""
        self.click_element(self.inventory_locators.ADD_BACKPACK_BUTTON)

    def add_bike_light_to_cart(self):
        """Add Sauce Labs Bike Light to cart."""
        self.click_element(self.inventory_locators.ADD_BIKE_LIGHT_BUTTON)

    def add_bolt_tshirt_to_cart(self):
        """Add Sauce Labs Bolt T-Shirt to cart."""
        self.click_element(self.inventory_locators.ADD_BOLT_TSHIRT_BUTTON)

    def add_fleece_jacket_to_cart(self):
        """Add Sauce Labs Fleece Jacket to cart."""
        self.click_element(self.inventory_locators.ADD_FLEECE_JACKET_BUTTON)

    def add_onesie_to_cart(self):
        """Add Sauce Labs Onesie to cart."""
        self.click_element(self.inventory_locators.ADD_ONESIE_BUTTON)

    def add_red_tshirt_to_cart(self):
        """Add Test.allTheThings() T-Shirt (Red) to cart."""
        self.click_element(self.inventory_locators.ADD_RED_TSHIRT_BUTTON)

    def remove_backpack_from_cart(self):
        """Remove Sauce Labs Backpack from cart."""
        self.click_element(self.inventory_locators.REMOVE_BACKPACK_BUTTON)

    def is_product_added_to_cart(self, product_name: str) -> bool:
        """Check if a product has been added to cart (button text changed)."""
        if "backpack" in product_name.lower():
            return self.is_element_visible(
                self.inventory_locators.REMOVE_BACKPACK_BUTTON
            )
        elif "bike-light" in product_name.lower():
            return self.is_element_visible(
                self.inventory_locators.REMOVE_BIKE_LIGHT_BUTTON
            )
        elif "bolt-t-shirt" in product_name.lower():
            return self.is_element_visible(
                self.inventory_locators.REMOVE_BOLT_TSHIRT_BUTTON
            )
        elif "fleece-jacket" in product_name.lower():
            return self.is_element_visible(
                self.inventory_locators.REMOVE_FLEECE_JACKET_BUTTON
            )
        elif "onesie" in product_name.lower():
            return self.is_element_visible(self.inventory_locators.REMOVE_ONESIE_BUTTON)
        elif "red" in product_name.lower():
            return self.is_element_visible(
                self.inventory_locators.REMOVE_RED_TSHIRT_BUTTON
            )
        return False

    def sort_products(self, sort_option: str):
        """Sort products using the dropdown."""
        self.page.select_option(
            self.inventory_locators.PRODUCT_SORT_CONTAINER, sort_option
        )
