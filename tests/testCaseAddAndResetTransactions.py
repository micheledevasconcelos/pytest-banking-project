import pytest

from pages.AddCustomerPage import AddCustomerPage
from pages.DepositPage import DepositPage
from pages.HomePage import HomePage
from pages.OpenAccountPage import OpenAccountPage
from pages.TransactionsPage import TransactionsPage
from pages.WithdrawlPage import WithdrawlPage
from tests.conftest import login_app_bank_manager


class TestCaseAddAndResetTransactions:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_add_and_reset_transactions(self, login_app_customer):
        login_p = login_app_bank_manager

        addCust_p = AddCustomerPage(login_p.driver)
        addCust_p.open_add_customer_menu()
        addCust_p.enter_customer_data("Maria")
        login_p.driver.switch_to.alert.accept()

        openAccount_p = OpenAccountPage(addCust_p.driver)
        openAccount_p.open_open_account_menu()
        openAccount_p.process_open_account("Maria José")
        acc_id = openAccount_p.get_account_id()
        addCust_p.driver.switch_to.alert.accept()

        home_p = HomePage(openAccount_p.driver)
        home_p.click_home_button()

        login_p.login_as_customer("Maria José")

        deposit_p = DepositPage(openAccount_p.driver)
        deposit_p.open_deposit_menu()
        deposit_p.select_account(acc_id)
        deposit_p.enter_amount("2000")

        withdrawl_p = WithdrawlPage(deposit_p.driver)
        withdrawl_p.open_withdrawl_menu()
        withdrawl_p.select_account(acc_id)
        withdrawl_p.enter_amount("800")

        transact_p = TransactionsPage(login_p.driver)
        transact_p.open_transactions_menu()
        transact_p.select_account()
        transact_p.reset_extract()

        assert transact_p.is_transactions_not_listed(), "Transactions not reset!"





