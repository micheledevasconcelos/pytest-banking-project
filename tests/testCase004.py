import pytest

from pages.TransactionsPage import TransactionsPage


class TestCase004:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_list_transactions(self, login_app_customer):
        login_p = login_app_customer
        transact_p = TransactionsPage(login_p.driver)
        transact_p.open_transactions_menu()
        transact_p.select_account()
