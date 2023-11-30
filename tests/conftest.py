import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.AddCustomerPage import AddCustomerPage

def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser')

@pytest.fixture()
def open_browser(request):
    select_browser = request.config.getoption("--browser_selenium").lower()
    if select_browser not in ['chrome', 'safari', 'firefox']:
        raise Exception('Browser not supported')
    login_p = LoginPage(browser=select_browser)
    login_p.open_page()
    yield login_p
    login_p.close()


@pytest.fixture()
def run_all_browser(all_browsers):
    login_p = LoginPage(browser=all_browsers)
    login_p.open_page()
    yield login_p
    login_p.close()


@pytest.fixture()
def login_app_customer(all_browsers):
    login_p = LoginPage(browser=all_browsers)
    login_p.open_page()
    login_p.login_as_customer()
    yield login_p

@pytest.fixture()
def login_app_bank_manager(all_browsers):
    login_p = LoginPage(browser=all_browsers)
    login_p.open_page()
    login_p.login_as_bank_manager()
    yield login_p
