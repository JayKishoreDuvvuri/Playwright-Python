"""Locators for the shopping cart page."""


class CartLocators:
    """Locators specific to the cart page."""

    # Page header
    PAGE_TITLE = "[data-test='title']"

    # Cart contents
    CART_LIST = "[data-test='cart-list']"
    CART_ITEM = "[data-test='shopping-cart-badge']"
    CART_ITEM_LABEL = "[data-test='inventory-item-name']"
    CART_ITEM_DESC = "[data-test='inventory-item-desc']"
    CART_ITEM_PRICE = "[data-test='inventory-item-price']"
    CART_QUANTITY = "[data-test='item-quantity']"

    # Cart actions
    CONTINUE_SHOPPING_BUTTON = "[data-test='continue-shopping']"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    REMOVE_BUTTON = "[data-test*='remove']"

    # Quantity label
    QTY_LABEL = ".cart_quantity_label"
