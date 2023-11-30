import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ListCustomerPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    firstName = "Hermoine"

    def __init__(self, driver=None):
        super(ListCustomerPage, self).__init__(driver=driver)

    def is_url_list_customer(self):
        return self.is_url(self.url)

    def open_customer_list_menu(self):
        self.wait_visible_element(By.XPATH, '//button[@ng-class="btnClass3"]')
        self.driver.find_element(By.XPATH, '//button[@ng-class="btnClass3"]').click()

    def search_customer(self, name=firstName):
        self.wait_visible_element(By.XPATH, "//input[@placeholder='Search Customer']", 5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search Customer']").send_keys(name)

    def is_customer_listed(self):
        self.wait_visible_element(By.TAG_NAME, 'tbody')
        list = self.driver.find_elements(By.TAG_NAME, 'tr')
        return len(list) > 1

    def is_customer_not_listed(self):
        self.wait_visible_element(By.TAG_NAME, 'tbody')
        list = self.driver.find_elements(By.TAG_NAME, 'tr')
        return len(list) > 0


    def delete_customer(self):
        ##self.wait_visible_element(By.XPATH, '//button[text()="Delete"]', 5)
        ##self.driver.find_element(By.XPATH, '//button[text()="Delete"]').click()
        self.wait_visible_element(By.XPATH, '//button[@ng-click="deleteCust(cust)"]', 5)
        self.driver.find_element(By.XPATH, '//button[@ng-click="deleteCust(cust)"]').click()