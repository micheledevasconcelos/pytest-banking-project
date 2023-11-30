import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.ListCustomerPage import ListCustomerPage
from pages.PageObject import PageObject


class WithdrawlPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    amountDefault = 1
    balance = 0
    account_number = '1001'

    def __init__(self, driver=None):
        super(WithdrawlPage, self).__init__(driver=driver)

    def is_url_withdrawl(self):
        return self.is_url(self.url)

    def select_account(self, account=account_number):
        self.wait_visible_element(By.ID, 'accountSelect')
        picklist = self.driver.find_element(By.ID, 'accountSelect')
        picklist.click()
        picklist.find_element(By.XPATH, '//option[@label='+account+']').click()

    def open_withdrawl_menu(self):
        self.wait_visible_element(By.XPATH, '//button[@ng-class="btnClass3"]')
        self.driver.find_element(By.XPATH, '//button[@ng-class="btnClass3"]').click()
        self.balance = self.get_balance()

    def enter_amount(self, amount=amountDefault):
        time.sleep(1)
        self.wait_visible_element(By.XPATH, '//input[@type="number"]')
        self.driver.find_element(By.XPATH, '//input[@type="number"]').send_keys(amount)
        self.wait_visible_element(By.XPATH, '//button[text()="Withdraw"]')
        self.driver.find_element(By.XPATH, '//button[text()="Withdraw"]').click()
        self.amountDefault = float(amount)

    def get_balance(self):
        self.wait_visible_element(By.XPATH, '//strong[@class="ng-binding"][2]')
        return float(self.driver.find_element(By.XPATH, '//strong[@class="ng-binding"][2]').text)

    def validate_final_balance(self):
        new_balance = self.get_balance()
        return new_balance == self.balance - self.amountDefault

    def is_withdrawl_successful(self):
        self.wait_visible_element(By.XPATH, '//span[@class="error ng-binding"]')
        message = self.driver.find_element(By.XPATH, '//span[@class="error ng-binding"]').text

        if self.balance < self.amountDefault:
            return "Transaction Failed. You can not withdraw amount more than the balance." in message
        else:
            return "Transaction successful" in message
