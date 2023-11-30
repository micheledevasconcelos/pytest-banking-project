from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageObject:
    class_title_page = 'XYZ Bank'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'safari':
                self.driver = webdriver.Safari()

    def is_url(self, url):
        return self.driver.current_url == url

    def wait_visible_element(self, by, value, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            return False
        return element.is_displayed()

    def is_title(self, title_text):
        title_element_text = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        return title_element_text == title_text

    def is_page(self, url, title_text):
        return self.is_title(title_text) and self.is_url(url)

    def close(self):
        #self.driver.quit()
        pass
