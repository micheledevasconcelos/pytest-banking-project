import time

import pytest

from pages.AddCustomerPage import AddCustomerPage
from pages.DepositPage import DepositPage
from pages.ListCustomerPage import ListCustomerPage
from pages.LoginPage import LoginPage
from pages.OpenAccountPage import OpenAccountPage
from pages.TransactionsPage import TransactionsPage
from pages.WithdrawlPage import WithdrawlPage


class TestCase006:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_make_withdrawl(self, login_app_customer):
        login_p = login_app_customer
        withdrawl_p = WithdrawlPage(login_p.driver)
        withdrawl_p.open_withdrawl_menu()
        withdrawl_p.select_account()
        withdrawl_p.enter_amount()
        withdrawl_p.is_withdrawl_successful(), 'No withdrawl possible'