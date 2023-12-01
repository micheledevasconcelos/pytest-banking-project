import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.ListCustomerPage import ListCustomerPage
from pages.PageObject import PageObject


class AddCustomerPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    firstName = 'José'

    def __init__(self, driver=None):
        super(AddCustomerPage, self).__init__(driver=driver)

    def is_url_add_customer(self):
        return self.is_url(self.url)

    def open_add_customer_menu(self):
        self.wait_visible_element(By.CSS_SELECTOR, 'div.ng-scope > div > div.center > button:nth-child(1)')
        self.driver.find_element(By.CSS_SELECTOR, 'div.ng-scope > div > div.center > button:nth-child(1)').click()

    def enter_customer_data(self, name=firstName):
        self.wait_visible_element(By.CLASS_NAME, 'form-group')
        self.wait_visible_element(By.XPATH, '//input[@placeholder="First Name"]')
        self.driver.find_element(By.XPATH, '//input[@placeholder="First Name"]').send_keys(name)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys("Silva")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Post Code"]').send_keys("50123")

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def is_customer_added(self):
        message = self.driver.switch_to.alert.text
        return 'Customer added successfully' in message

    def is_not_customer_added(self):
        message = self.driver.switch_to.alert.text
        return 'Customer may be duplicate' in message

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
