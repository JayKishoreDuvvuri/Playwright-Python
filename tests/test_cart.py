"""Shopping cart tests."""

import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:
    """Test cases for shopping cart functionality."""

 #   @pytest.mark.skip(reason="Known issue, skipping temporarily")
    def test_empty_cart(self, authenticated_page):
        """Test empty cart state."""
        cart_page = CartPage(authenticated_page)

        cart_page.navigate_to_cart()

        assert cart_page.is_on_cart_page()
        assert cart_page.get_page_title() == "Your Cart"
        assert cart_page.is_cart_empty()

    def test_cart_with_items(self, authenticated_page):
        """Test cart with items."""
        inventory_page = InventoryPage(authenticated_page)
        cart_page = CartPage(authenticated_page)

        # Add products to cart
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()

        # Navigate to cart
        cart_page.navigate_to_cart()

        assert not cart_page.is_cart_empty()
        assert cart_page.get_cart_item_count() == 1

        item_names = cart_page.get_cart_item_names()
        assert "Sauce Labs Backpack" in item_names
        assert "Sauce Labs Bike Light" in item_names

    def test_continue_shopping(self, authenticated_page):
        """Test continue shopping functionality."""
        inventory_page = InventoryPage(authenticated_page)
        cart_page = CartPage(authenticated_page)

        cart_page.navigate_to_cart()
        cart_page.continue_shopping()

        assert inventory_page.is_on_inventory_page()


    def test_cart_item_quantities(self, authenticated_page):
        """Test cart item quantities."""
        inventory_page = InventoryPage(authenticated_page)
        cart_page = CartPage(authenticated_page)

        inventory_page.add_backpack_to_cart()
        cart_page.navigate_to_cart()

        quantities = cart_page.get_cart_item_quantities()
        print( "Quantities is:", quantities )
        assert quantities[0] == "1"
