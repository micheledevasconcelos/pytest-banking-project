import time

import pytest

from pages.ListCustomerPage import ListCustomerPage


class TestCase007:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_delete_customer(self, login_app_bank_manager, name="Neville"):
        login_p = login_app_bank_manager
        listCust_p = ListCustomerPage(login_p.driver)
        listCust_p.open_customer_list_menu()
        listCust_p.search_customer(name)
        listCust_p.delete_customer()
        assert listCust_p.is_customer_not_listed(), 'Customer found!'
