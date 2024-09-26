from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException

class DevPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def sleep(self):
        sleep(10)

    def clear_userfname(self):
        self.driver.find_element(By.NAME, 'userfname').clear()

    def clear_userlname(self):
        self.driver.find_element(By.NAME, 'userlname').clear()

    def clear_patientfname(self):
        self.driver.find_element(By.NAME, 'patientfname').clear()

    def clear_patientlname(self):
        self.driver.find_element(By.NAME, 'patientlname').clear()

    def enter_userfname(self, userfname):
       self.driver.find_element(By.NAME, 'userfname').send_keys(userfname)

    def enter_userlname(self, userlname):
       self.driver.find_element(By.NAME, 'userlname').send_keys(userlname)
    
    def enter_patientfname(self, patientfname):
       self.driver.find_element(By.NAME, 'patientfname').send_keys(patientfname)

    def enter_patientlname(self, patientlname):
       self.driver.find_element(By.NAME, 'patientlname').send_keys(patientlname)

    def click_next(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
         
    def video_dev_toggle(self):
        self.driver.find_element(By.ID, 'radix-:r0:-trigger-video').click()

    def audio_dev_toggle(self):
        self.driver.find_element(By.ID, 'radix-:r0:-trigger-audio').click()

    def teardown(driver):
        driver.quit()
