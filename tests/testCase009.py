import pytest

from pages.AddCustomerPage import AddCustomerPage
from tests.conftest import login_app_bank_manager


class TestCase008:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_add_duplicate_customer(self, login_app_bank_manager):

            login_p = login_app_bank_manager
            addCust_p = AddCustomerPage(login_p.driver)
            addCust_p.open_add_customer_menu()
            addCust_p.enter_customer_data()
            assert addCust_p.is_customer_added(), "Customer not added!"
            addCust_p.accept_alert()
            addCust_p.enter_customer_data()
            assert addCust_p.is_not_customer_added(), "Duplicate customer added!"

