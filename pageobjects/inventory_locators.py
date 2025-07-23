"""Locators for the inventory/products page."""


class InventoryLocators:
    """Locators specific to the inventory page."""

    # Page header
    PAGE_TITLE = "[data-test='title']"
    PRODUCT_SORT_CONTAINER = "[data-test='product-sort-container']"

    # Product grid
    INVENTORY_CONTAINER = "[data-test='inventory-container']"
    INVENTORY_LIST = "[data-test='inventory-list']"
    INVENTORY_ITEM = "[data-test='inventory-item']"

    # Individual product elements
    INVENTORY_ITEM_NAME = "[data-test='inventory-item-name']"
    INVENTORY_ITEM_DESC = "[data-test='inventory-item-desc']"
    INVENTORY_ITEM_PRICE = "[data-test='inventory-item-price']"
    INVENTORY_ITEM_IMG = "[data-test='inventory-item-sauce-labs-backpack-img']"

    # Add to cart buttons (generic)
    ADD_TO_CART_BUTTON = "[data-test*='add-to-cart']"
    REMOVE_BUTTON = "[data-test*='remove']"

    # Specific product buttons
    ADD_BACKPACK_BUTTON = "[data-test='add-to-cart-sauce-labs-backpack']"
    ADD_BIKE_LIGHT_BUTTON = "[data-test='add-to-cart-sauce-labs-bike-light']"
    ADD_BOLT_TSHIRT_BUTTON = "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    ADD_FLEECE_JACKET_BUTTON = "[data-test='add-to-cart-sauce-labs-fleece-jacket']"
    ADD_ONESIE_BUTTON = "[data-test='add-to-cart-sauce-labs-onesie']"
    ADD_RED_TSHIRT_BUTTON = (
        "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']"
    )

    # Remove buttons
    REMOVE_BACKPACK_BUTTON = "[data-test='remove-sauce-labs-backpack']"
    REMOVE_BIKE_LIGHT_BUTTON = "[data-test='remove-sauce-labs-bike-light']"
    REMOVE_BOLT_TSHIRT_BUTTON = "[data-test='remove-sauce-labs-bolt-t-shirt']"
    REMOVE_FLEECE_JACKET_BUTTON = "[data-test='remove-sauce-labs-fleece-jacket']"
    REMOVE_ONESIE_BUTTON = "[data-test='remove-sauce-labs-onesie']"
    REMOVE_RED_TSHIRT_BUTTON = "[data-test='remove-test.allthethings()-t-shirt-(red)']"
