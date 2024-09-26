from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
import pdb, time


class CallPage:
    def __init__(self, driver):
        self.driver = driver

    def static_sleep(self, seconds=1):
        time.sleep(seconds)

    def open_page(self, url):
        self.driver.get(url)

    def video_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='video-toggle']").click()

    def audio_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='audio-toggle']").click()

    def end_call(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='disconnect-control']").click()

    def invite_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='invite-button']").click()

    def identity_name(self):
        try:
            identity_name = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='identity']")
            return 1
        except NoSuchElementException:
            return 0

    def identity_name_check(self, actual_identity):
        name = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='identity']")
        assert actual_identity == name.text
        
    def thumbnail(self):
        try: 
            thumbnail = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='thumbnail']")
            return 1
        except NoSuchElementException: 
            return 0

    def driver_quit(self):
        self.driver = driver
        driver.quit()

    def close_browser(self):
        self.browser.close()
