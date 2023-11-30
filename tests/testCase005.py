import pytest

from pages.DepositPage import DepositPage

class TestCase005:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_make_deposit(self, login_app_customer):
        login_p = login_app_customer
        deposit_p = DepositPage(login_p.driver)
        deposit_p.open_deposit_menu()
        deposit_p.select_account()
        deposit_p.enter_amount()
        deposit_p.is_deposit_successful(), "No deposit made"
