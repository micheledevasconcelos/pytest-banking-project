import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.ListCustomerPage import ListCustomerPage
from pages.PageObject import PageObject


class DepositPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    amountDefault = 999
    account_number = '1001'
    balance = 0

    def __init__(self, driver=None):
        super(DepositPage, self).__init__(driver=driver)

    def is_url_deposit(self):
        return self.is_url(self.url)

    def select_account(self, account=account_number):
        self.wait_visible_element(By.ID, 'accountSelect')
        picklist = self.driver.find_element(By.ID, 'accountSelect')
        picklist.click()
        picklist.find_element(By.XPATH, '//option[@label='+account+']').click()

    def open_deposit_menu(self):
        self.wait_visible_element(By.XPATH, '//button[@ng-class="btnClass2"]')
        self.driver.find_element(By.XPATH, '//button[@ng-class="btnClass2"]').click()
        self.balance = self.get_balance()

    def enter_amount(self, amount=amountDefault):
        self.wait_visible_element(By.TAG_NAME, 'Input')
        self.driver.find_element(By.TAG_NAME, 'Input').send_keys(amount)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        self.amountDefault = float(amount)

    def get_balance(self):
        self.wait_visible_element(By.XPATH, '//strong[@class="ng-binding"][2]')
        return float(self.driver.find_element(By.XPATH, '//strong[@class="ng-binding"][2]').text)

    def validate_final_balance(self):
        new_balance = self.get_balance()
        return new_balance == self.balance + self.amountDefault

    def is_deposit_successful(self):
        self.wait_visible_element(By.XPATH, '//span[text()="Deposit Successful"]')
        return self.driver.find_element(By.XPATH, '//span[text()="Deposit Successful"]').is_displayed()