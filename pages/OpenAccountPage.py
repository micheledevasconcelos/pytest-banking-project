import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class OpenAccountPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    customerDefault = 'Harry Potter'
    currencyDefault = 'Dollar'

    def __init__(self, driver=None):
        super(OpenAccountPage, self).__init__(driver=driver)

    def is_url_open_account(self):
        return self.is_url(self.url)

    def open_open_account_menu(self):
        self.wait_visible_element(By.CSS_SELECTOR, 'div.ng-scope > div > div.center > button:nth-child(2)')
        self.driver.find_element(By.CSS_SELECTOR, 'div.ng-scope > div > div.center > button:nth-child(2)').click()

    def process_open_account(self, customer=customerDefault, currency=currencyDefault):
        self.wait_visible_element(By.ID, "userSelect", 5)
        self.driver.find_element(By.ID, "userSelect").click()

        path_customer = "//option[text()='"+customer+"']"
        self.wait_visible_element(By.XPATH, path_customer)
        self.driver.find_element(By.XPATH, path_customer).click()

        self.driver.find_element(By.ID, "currency").click()

        path_currency = "//option[text()='"+currency+"']"
        self.wait_visible_element(By.XPATH, path_currency)
        self.driver.find_element(By.XPATH, path_currency).click()

        self.wait_visible_element(By.XPATH, '//button[text()="Process"]')
        self.driver.find_element(By.XPATH, '//button[text()="Process"]').click()

    def get_account_id(self):
        message = self.driver.switch_to.alert.text
        id = message.split(':')
        return id[1]

    def is_account_open(self):
        message = self.driver.switch_to.alert.text
        return 'Account created successfully' in message
