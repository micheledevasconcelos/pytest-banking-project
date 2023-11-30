import time

import pytest

from pages.AddCustomerPage import AddCustomerPage
from pages.DepositPage import DepositPage
from pages.HomePage import HomePage
from pages.ListCustomerPage import ListCustomerPage
from pages.LoginPage import LoginPage
from pages.OpenAccountPage import OpenAccountPage
from pages.TransactionsPage import TransactionsPage
from pages.WithdrawlPage import WithdrawlPage


class TestCaseAddAndSearch:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_add_and_search(self, login_app_bank_manager):
        login_p = login_app_bank_manager

        addCust_p = AddCustomerPage(login_p.driver)
        addCust_p.open_add_customer_menu()
        addCust_p.enter_customer_data("José")
        login_p.driver.switch_to.alert.accept()

        listCust_p = ListCustomerPage(addCust_p.driver)
        listCust_p.open_customer_list_menu()
        listCust_p.search_customer("José")

        assert listCust_p.is_customer_listed(), 'Customer not found!'
