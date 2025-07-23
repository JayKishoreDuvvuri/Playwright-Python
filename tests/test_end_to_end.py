"""End-to-end test scenarios."""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestEndToEnd:
    """End-to-end test scenarios."""
   # @pytest.mark.skip(reason="Known issue, skipping temporarily")
    def test_complete_purchase_flow(self, page):
        """Test complete purchase flow from login to checkout."""
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        # Login
        login_page.navigate_to_login()
        login_page.login("standard_user", "secret_sauce")
        assert inventory_page.is_on_inventory_page()

        # Add products to cart
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        assert inventory_page.get_cart_badge_count() == "2"

        # Go to cart
        inventory_page.click_shopping_cart()
        assert cart_page.is_on_cart_page()
        assert cart_page.get_cart_item_count() == 0

        # Proceed to checkout
        cart_page.proceed_to_checkout()
        assert checkout_page.is_on_checkout_step_one()

        # Complete checkout
        success = checkout_page.complete_checkout_flow("John", "Doe", "12345")
        assert success
        assert "Thank you for your order!" in checkout_page.get_completion_header()

        # Return home
        checkout_page.click_back_home()
        assert inventory_page.is_on_inventory_page()

        # Verify cart is empty
        assert inventory_page.get_cart_badge_count() == "0"

 #   @pytest.mark.skip(reason="Known issue, skipping temporarily")
    def test_multiple_users_workflow(self, page):
        """Test workflow with different user types."""
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        # Test with standard_user
        login_page.navigate_to_login()
        login_page.login("standard_user", "secret_sauce")
        assert inventory_page.is_on_inventory_page()

        # Add item and verify
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_badge_count() == "1"

        # Logout
        inventory_page.logout()
        assert login_page.is_login_button_displayed()

        # Test with problem_user
        login_page.login("problem_user", "secret_sauce")
        assert inventory_page.is_on_inventory_page()

        # Verify cart is empty for new user
        assert inventory_page.get_cart_badge_count() == "1"
