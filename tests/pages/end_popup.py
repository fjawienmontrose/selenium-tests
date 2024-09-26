from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb, time


class EndPopup:
    def __init__(self, driver):
        self.driver = driver
        self.end_button = (By.CSS_SELECTOR, "[data-testid='confirm-button']")

    def static_sleep(self, seconds=1):
        time.sleep(seconds)

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_popup(self):
        button = WebDriverWait(self.driver, 1). until(
            EC.presence_of_element_located(self.end_button)
        )
        button.click()

    def endcall_pop(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='confirm-button']").click()

    def cancel_pop(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='cancel-button']").click()
