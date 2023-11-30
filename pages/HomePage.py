import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class HomePage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def __init__(self, driver=None):
        super(HomePage, self).__init__(driver=driver)

    def open_page(self):
        self.driver.get(self.url)

    def click_home_button(self):
        self.wait_visible_element(By.XPATH, '//button[text()="Home"]')
        self.driver.find_element(By.XPATH, '//button[text()="Home"]').click()
        time.sleep(2)
