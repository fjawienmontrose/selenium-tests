from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException
import time

class FcmPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def static_sleep(self, seconds=5):
        time.sleep(seconds)

    def long_sleep(self, seconds=15):
        time.sleep(seconds)

    def enter_token(self, token):
        self.driver.find_element(By.CSS_SELECTOR, 'input').send_keys(token)

    def click_call(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()