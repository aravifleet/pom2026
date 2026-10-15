import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
  """Dedicated Playwright page fixture for each test iteration."""
  with sync_playwright() as p:
    # Launch browser (headless=False to watch execution live)
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    # Yield the actual page object to the test function
    yield page

    # Teardown: Close browser after test
    context.close()
    browser.close()