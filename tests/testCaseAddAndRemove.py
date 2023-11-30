import pytest

from pages.AddCustomerPage import AddCustomerPage
from pages.ListCustomerPage import ListCustomerPage


class TestCaseAddAndRemove:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_add_and_remove(self, login_app_bank_manager):
        login_p = login_app_bank_manager

        addCust_p = AddCustomerPage(login_p.driver)
        addCust_p.open_add_customer_menu()
        addCust_p.enter_customer_data("Maria")
        login_p.driver.switch_to.alert.accept()

        listCust_p = ListCustomerPage(addCust_p.driver)
        listCust_p.open_customer_list_menu()
        listCust_p.search_customer("Maria")
        listCust_p.delete_customer()

        assert listCust_p.is_customer_not_listed(), 'Customer found!'
