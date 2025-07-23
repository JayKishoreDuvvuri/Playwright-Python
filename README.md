# Playwright Python Page Object Model for SauceDemo

This project implements a comprehensive Page Object Model (POM) structure for testing [SauceDemo](https://www.saucedemo.com/) using Playwright with Python.

#### Application Under Test

We are using https://www.saucedemo.com/ as the Application Under Test. This App is a **React.js** Frontend

- URL: https://www.saucedemo.com/
- OS : macOS
- IDE : Visual Studio Code

## Project Structure

```
├── pageobjects/              # Separated locator classes
│   ├── base_locators.py
│   ├── login_locators.py
│   ├── inventory_locators.py
│   ├── cart_locators.py
│   └── checkout_locators.py
├── pages/                    # Page object classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                    # Test files
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_end_to_end.py
├── reports/                  # Test reports (generated)
├── conftest.py               # Pytest fixtures and configuration
├── pytest.ini                # Pytest configuration
└── requirements.txt          # Python dependencies
```

## Setup Instructions

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Playwright and Playwright browsers:**
   ```bash
   pip install playwright
   playwright install
   ```

## Key Features

### Separated Locators
- **Base Locators**: Common elements like navigation, cart, menu
- **Page-specific Locators**: Elements specific to each page
- **Maintainable**: Easy to update when UI changes

### Page Object Model
- **Base Page**: Common functionality across all pages
- **Inheritance**: All page objects inherit from BasePage
- **Encapsulation**: Page-specific actions and validations
- **Reusable**: Methods can be used across multiple tests

### Test Organization
- **Login Tests**: Authentication scenarios
- **Inventory Tests**: Product browsing and cart operations
- **Cart Tests**: Shopping cart functionality
- **Checkout Tests**: Purchase flow validation
- **End-to-End Tests**: Complete user journeys

## Running Tests

### Run all tests:
```bash
pytest 
```

### Run specific test file:
```bash
pytest tests/test_login.py -s -v
```

### Run tests with specific markers:
```bash
pytest -m smoke
pytest -m regression
```

### Run tests in headed mode (visible browser):
```bash
pytest --headed
```

### Generate HTML report:
- Run specific test file: `pytest tests/test_login.py --html=reports/report.html`
- Run for all tests: `pytest --html=reports/report.html`

### Remove pycache from your folders
```bash
Run on Terminal: 
1. find . -type d -name "__pycache__" -exec rm -r {} +
2. rm -rf .pytest_cache/
3. rm -rf .vscode/
```

## Available User Credentials

- **standard_user** / secret_sauce (normal user)
- **locked_out_user** / secret_sauce (locked account)
- **problem_user** / secret_sauce (has UI issues)
- **performance_glitch_user** / secret_sauce (slow performance)

## Usage Examples

### Basic Login Test
```python
def test_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    assert inventory_page.is_on_inventory_page()
```

### Add Products to Cart
```python
def test_add_to_cart(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    
    assert inventory_page.get_cart_badge_count() == "2"
```

### Complete Checkout Flow
```python
def test_checkout(cart_with_items):
    checkout_page = CheckoutPage(cart_with_items)
    
    success = checkout_page.complete_checkout_flow(
        "John", "Doe", "12345"
    )
    
    assert success
    assert checkout_page.is_on_checkout_complete()
```

## Best Practices Implemented

1. **Separation of Concerns**: Locators, page objects, and tests are in separate modules
2. **DRY Principle**: Common functionality in base classes
3. **Explicit Waits**: Proper waiting strategies for elements
4. **Error Handling**: Graceful handling of missing elements
5. **Fixtures**: Reusable test setup with pytest fixtures
6. **Reporting**: HTML test reports with screenshots on failure
7. **Maintainability**: Easy to extend and modify

## Configuration

### Browser Options
The `conftest.py` file is configured to run tests in headed mode with slow motion for better visibility. Modify these settings as needed:

```python
browser = p.chromium.launch(headless=False, slow_mo=500)
```

### Test Markers
Use pytest markers to categorize tests:
- `@pytest.mark.smoke` - Critical functionality tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.slow` - Long-running tests
-  Add this line for skipping tests `@pytest.mark.skip(reason="Known issue, skipping temporarily")` for ex: in
   test_end_to_end.py

## Extending the Framework

To add new pages or functionality:

1. Create locator class in `pageobjects/`
2. Create page object class in `pages/` inheriting from `BasePage`
3. Write tests in `tests/`
4. Add fixtures in `conftest.py` if needed

This framework provides a solid foundation for scalable, maintainable web automation testing.