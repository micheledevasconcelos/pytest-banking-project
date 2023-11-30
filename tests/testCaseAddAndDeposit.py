import pytest

from pages.AddCustomerPage import AddCustomerPage
from pages.DepositPage import DepositPage
from pages.HomePage import HomePage
from pages.OpenAccountPage import OpenAccountPage


class TestCaseAddAndDeposit:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_add_and_deposit(self, login_app_bank_manager):
        login_p = login_app_bank_manager

        addCust_p = AddCustomerPage(login_p.driver)
        addCust_p.open_add_customer_menu()
        addCust_p.enter_customer_data("José")
        login_p.driver.switch_to.alert.accept()

        openAccount_p = OpenAccountPage(addCust_p.driver)
        openAccount_p.open_open_account_menu()
        openAccount_p.process_open_account("José Silva")
        acc_id = openAccount_p.get_account_id()
        addCust_p.driver.switch_to.alert.accept()

        home_p = HomePage(openAccount_p.driver)
        home_p.click_home_button()

        login_p.login_as_customer("José Silva")

        deposit_p = DepositPage(openAccount_p.driver)
        deposit_p.open_deposit_menu()
        deposit_p.select_account(acc_id)
        deposit_p.enter_amount()

        assert deposit_p.is_deposit_successful(), "No deposit made"
        assert deposit_p.validate_final_balance(), "Balance invalid!"



