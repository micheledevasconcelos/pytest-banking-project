import time

import pytest

from pages.AddCustomerPage import AddCustomerPage
from pages.ListCustomerPage import ListCustomerPage
from pages.LoginPage import LoginPage
from pages.OpenAccountPage import OpenAccountPage


class TestCase003:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_open_account(self, login_app_bank_manager):
        login_p = login_app_bank_manager
        openAccount_p = OpenAccountPage(login_p.driver)
        openAccount_p.open_open_account_menu()
        openAccount_p.process_open_account()
        assert openAccount_p.is_account_open(), 'Account not open!'
