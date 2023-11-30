import pytest

from pages.ListCustomerPage import ListCustomerPage
from pages.TransactionsPage import TransactionsPage
from tests.conftest import login_app_bank_manager


class TestCase008:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_reset_extract(self, login_app_bank_manager):
        login_p = login_app_bank_manager
        transact_p = TransactionsPage(login_p.driver)
        transact_p.open_transactions_menu()
        transact_p.reset_extract()

        assert transact_p.is_transactions_not_listed(), "Transactions not reset!"





