"""Base locators class for common elements across pages."""


class BaseLocators:
    """Common locators used across multiple pages."""

    # Navigation and header elements
    BURGER_MENU_BUTTON = "button#react-burger-menu-btn"
    CLOSE_MENU_BUTTON = "[data-test='close-menu']"
    SHOPPING_CART_LINK = "[data-test='shopping-cart-link']"
    SHOPPING_CART_BADGE = "[data-test='shopping-cart-badge']"

    # Menu items
    ALL_ITEMS_LINK = "[data-test='inventory-sidebar-link']"
    ABOUT_LINK = "[data-test='about-sidebar-link']"
    LOGOUT_LINK = "[data-test='logout-sidebar-link']"
    RESET_APP_STATE_LINK = "[data-test='reset-sidebar-link']"

    # Footer
    FOOTER = "[data-test='footer']"
    TWITTER_LINK = "[data-test='social-twitter']"
    FACEBOOK_LINK = "[data-test='social-facebook']"
    LINKEDIN_LINK = "[data-test='social-linkedin']"
