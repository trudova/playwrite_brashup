import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="server selection"
    )


@pytest.fixture(scope='session')
def user_creds(request):
    return request.param

@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption('browser_name')
    url_name = request.config.getoption('url_name')
    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url_name)
    yield page
    context.close()
    browser.close()