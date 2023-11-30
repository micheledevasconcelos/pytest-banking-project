import time

import pytest

from pages.AddCustomerPage import AddCustomerPage
from pages.ListCustomerPage import ListCustomerPage
from pages.LoginPage import LoginPage


class TestCase002:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_search_customer(self, login_app_bank_manager, name="Hermoine"):
        login_p = login_app_bank_manager
        listCust_p = ListCustomerPage(login_p.driver)
        listCust_p.open_customer_list_menu()
        listCust_p.search_customer(name)
        assert listCust_p.is_customer_listed(), 'Customer not found!'
