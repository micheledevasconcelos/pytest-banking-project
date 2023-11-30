import time

import pytest

from pages.AddCustomerPage import AddCustomerPage
from pages.DepositPage import DepositPage
from pages.ListCustomerPage import ListCustomerPage
from pages.LoginPage import LoginPage
from pages.OpenAccountPage import OpenAccountPage
from pages.TransactionsPage import TransactionsPage


class TestCase005:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_make_deposit(self, login_app_customer):
        login_p = login_app_customer
        deposit_p = DepositPage(login_p.driver)
        deposit_p.open_deposit_menu()
        deposit_p.select_account()
        deposit_p.enter_amount()
        deposit_p.is_deposit_successful(), "No deposit made"
