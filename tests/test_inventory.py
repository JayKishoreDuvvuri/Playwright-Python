"""Inventory page tests."""

import pytest
from pages.inventory_page import InventoryPage


class TestInventory:
    """Test cases for inventory functionality."""

    def test_inventory_page_loads(self, authenticated_page):
        """Test that inventory page loads correctly."""
        inventory_page = InventoryPage(authenticated_page)

        assert inventory_page.is_on_inventory_page()
        assert inventory_page.get_page_title() == "Products"
        assert inventory_page.get_product_count() == 6

    def test_product_names_displayed(self, authenticated_page):
        """Test that all product names are displayed."""
        inventory_page = InventoryPage(authenticated_page)

        product_names = inventory_page.get_product_names()
        expected_products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ]

        for product in expected_products:
            assert product in product_names

    def test_add_single_product_to_cart(self, authenticated_page):
        """Test adding a single product to cart."""
        inventory_page = InventoryPage(authenticated_page)

        inventory_page.add_backpack_to_cart()

        assert inventory_page.get_cart_badge_count() == "1"
        assert inventory_page.is_product_added_to_cart("backpack")

    def test_add_multiple_products_to_cart(self, authenticated_page):
        """Test adding multiple products to cart."""
        inventory_page = InventoryPage(authenticated_page)

        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        inventory_page.add_bolt_tshirt_to_cart()

        assert inventory_page.get_cart_badge_count() == "3"

    def test_remove_product_from_cart(self, authenticated_page):
        """Test removing a product from cart."""
        inventory_page = InventoryPage(authenticated_page)

        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_badge_count() == "1"

        inventory_page.remove_backpack_from_cart()
        assert inventory_page.get_cart_badge_count() == "0"

    def test_product_prices_displayed(self, authenticated_page):
        """Test that product prices are displayed."""
        inventory_page = InventoryPage(authenticated_page)

        prices = inventory_page.get_product_prices()

        assert len(prices) == 6
        for price in prices:
            assert price.startswith("$")
            assert len(price) > 1
