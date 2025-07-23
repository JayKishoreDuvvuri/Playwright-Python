"""Checkout functionality tests."""

import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    """Test cases for checkout functionality."""

    @pytest.fixture
    def cart_with_items(self, authenticated_page):
        """Setup cart with items for checkout tests."""
        inventory_page = InventoryPage(authenticated_page)
        cart_page = CartPage(authenticated_page)

        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        cart_page.navigate_to_cart()
        cart_page.proceed_to_checkout()

        return authenticated_page

    def test_checkout_step_one_validation(self, cart_with_items):
        """Test checkout step one form validation."""
        checkout_page = CheckoutPage(cart_with_items)

        assert checkout_page.is_on_checkout_step_one()

        # Try to continue without filling information
        checkout_page.click_continue()

        assert checkout_page.is_error_displayed()
        assert "Error: First Name is required" in checkout_page.get_error_message()

    def test_checkout_step_one_success(self, cart_with_items):
        """Test successful checkout step one."""
        checkout_page = CheckoutPage(cart_with_items)

        checkout_page.fill_checkout_information("John", "Doe", "12345")
        checkout_page.click_continue()

        assert checkout_page.is_on_checkout_step_two()

    def test_checkout_step_two_information(self, cart_with_items):
        """Test checkout step two displays correct information."""
        checkout_page = CheckoutPage(cart_with_items)

        checkout_page.fill_checkout_information("John", "Doe", "12345")
        checkout_page.click_continue()

        assert checkout_page.is_on_checkout_step_two()

        # Check that totals are displayed
        item_total = checkout_page.get_item_total()
        tax_amount = checkout_page.get_tax_amount()
        total_amount = checkout_page.get_total_amount()

        assert "Item total:" in item_total
        assert "Tax:" in tax_amount
        assert "Total:" in total_amount

    def test_complete_checkout_flow(self, cart_with_items):
        """Test complete checkout flow."""
        checkout_page = CheckoutPage(cart_with_items)

        success = checkout_page.complete_checkout_flow("John", "Doe", "12345")

        assert success
        assert checkout_page.is_on_checkout_complete()
        assert "Thank you for your order!" in checkout_page.get_completion_header()
        assert checkout_page.is_pony_express_image_displayed()

    def test_checkout_cancel(self, cart_with_items):
        """Test canceling checkout."""
        checkout_page = CheckoutPage(cart_with_items)
        cart_page = CartPage(cart_with_items)

        checkout_page.click_cancel()

        assert cart_page.is_on_cart_page()

    def test_back_home_from_complete(self, cart_with_items):
        """Test back home from checkout complete."""
        checkout_page = CheckoutPage(cart_with_items)
        inventory_page = InventoryPage(cart_with_items)

        checkout_page.complete_checkout_flow("John", "Doe", "12345")
        checkout_page.click_back_home()

        assert inventory_page.is_on_inventory_page()
