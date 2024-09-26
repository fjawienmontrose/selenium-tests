from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
import pdb, time


class DeclinedPage:
    def __init__(self, driver):
        self.driver = driver

    def static_sleep(self, seconds=20):
        time.sleep(seconds)

    def open_page(self, url):
        self.driver.get(url)

    def decline_reason_name(self, caller_name_text):
        actual_decline_name = self.driver.find_element(By.CLASS_NAME, '_thumbnail-identity_vx4wz_9')
        assert actual_decline_name.text == caller_name_text

    def decline_reason(self, decline_reason_text):
        actual_decline_reason = self.driver.find_element(By.CLASS_NAME, '_decline-reason_1ynjg_43')
        assert actual_decline_reason.text == decline_reason_text

    def decline_status(self, decline_status_text):
        actual_decline_status = self.driver.find_element(By.CLASS_NAME, '_end-reason_1di1z_1')
        assert actual_decline_status.text == decline_status_text