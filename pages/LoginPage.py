import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    customerDefault = "Hermoine Granger"

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)

    def open_page(self):
        self.driver.get(self.url)

    def login_as_customer(self, customer=customerDefault):
        self.wait_visible_element(By.XPATH, '//button[text()="Customer Login"]')
        self.driver.find_element(By.XPATH, '//button[text()="Customer Login"]').click()
        self.wait_visible_element(By.NAME, 'userSelect')
        self.driver.find_element(By.NAME, 'userSelect').click()

        path_customer = "//option[text()='"+customer+"']"
        self.wait_visible_element(By.XPATH, path_customer)
        self.driver.find_element(By.XPATH, path_customer).click()

        self.wait_visible_element(By.XPATH, '//button[text()="Login"]')
        self.driver.find_element(By.XPATH, '//button[text()="Login"]').click()
        time.sleep(2)

    def login_as_bank_manager(self):
        self.wait_visible_element(By.XPATH, '//button[text()="Bank Manager Login"]')
        self.driver.find_element(By.XPATH, '//button[text()="Bank Manager Login"]').click()
        time.sleep(2)

    def is_url_login(self):
        return self.is_url(self.url)
