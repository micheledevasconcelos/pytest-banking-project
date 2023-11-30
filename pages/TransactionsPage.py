import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.ListCustomerPage import ListCustomerPage
from pages.PageObject import PageObject


class TransactionsPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    account_number = '1001'

    def __init__(self, driver=None):
        super(TransactionsPage, self).__init__(driver=driver)

    def is_url_transactions_list(self):
        return self.is_url(self.url)

    def open_transactions_menu(self):
        self.wait_visible_element(By.XPATH, '//button[@ng-class="btnClass1"]')
        self.driver.find_element(By.XPATH, '//button[@ng-class="btnClass1"]').click()

    def select_account(self, account=account_number):
        self.wait_visible_element(By.ID, 'accountSelect')
        picklist = self.driver.find_element(By.ID, 'accountSelect')
        picklist.click()
        picklist.find_element(By.XPATH, '//option[@label=' + account + ']').click()