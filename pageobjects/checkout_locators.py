"""Locators for the checkout pages."""

class CheckoutLocators:
    """Locators specific to checkout pages."""
    
    # Checkout step one (information)
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    POSTAL_CODE_INPUT = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    CANCEL_BUTTON = "[data-test='cancel']"
    
    # Checkout step two (overview)
    PAYMENT_INFO = "[data-test='payment-info-label']"
    SHIPPING_INFO = "[data-test='shipping-info-label']"
    PRICE_TOTAL = "[data-test='total-info-label']"
    ITEM_TOTAL = "[data-test='subtotal-label']"
    TAX_LABEL = "[data-test='tax-label']"
    TOTAL_LABEL = "[data-test='total-label']"
    FINISH_BUTTON = "[data-test='finish']"
    
    # Checkout complete
    COMPLETE_HEADER = "[data-test='complete-header']"
    COMPLETE_TEXT = "[data-test='complete-text']"
    BACK_HOME_BUTTON = "[data-test='back-to-products']"
    PONY_EXPRESS_IMG = "[data-test='pony-express']"
    
    # Error messages
    ERROR_MESSAGE_CONTAINER = "[data-test='error']"
    ERROR_MESSAGE_TEXT = "h3[data-test='error']"