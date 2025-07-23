"""Pytest configuration and fixtures."""

import os
import pytest
from playwright.sync_api import Browser, Page, sync_playwright

# Headless and slowmo config from env vars (default: headless in CI)
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))


@pytest.fixture(scope="session")
def browser() -> Browser:
    """Create a browser instance for the test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    """Create a new page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """Create a page with authenticated user."""
    from pages.login_page import LoginPage

    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    yield page