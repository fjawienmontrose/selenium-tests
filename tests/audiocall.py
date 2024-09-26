from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import selenium
from time import sleep
from selenium.webdriver.support.color import Color
import pytest  
 
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1, 
})
driver = webdriver.Chrome(options=options)

driver.get("https://inpatient-video-dev.nyumc.org/")

title = driver.title
assert title == "Bedside Connect"

driver.find_element(By.NAME, "userfname").clear()
driver.find_element(By.NAME, "userlname").clear()

driver.find_element(By.NAME, "patientfname").clear()
driver.find_element(By.NAME, "patientlname").clear()

driver.find_element(By.NAME, "userfname").send_keys("Selenium")
driver.find_element(By.NAME, "userlname").send_keys("Webdriver Doctor")

driver.find_element(By.NAME, "patientfname").send_keys("Selenium")
driver.find_element(By.NAME, "patientlname").send_keys("Webdriver Patient")

sleep(5)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

assert title == "Bedside Connect"
driver.find_element(By.CSS_SELECTOR, 'input').send_keys("eUV1yw0KQaefKvqJT-ES0w:APA91bERTirrX35AKSMWfBb0_MPQyv4-qiiEtkx53OYwVzG6KdmavjBWFnhDnFO81vnLYN56cAojIhYc-IpvdRvMnRi9gyq7I3Vz507DvrhQtGwogoJuld1E-QI_yH5uuSGkoz8N-7fJ")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

sleep(15)

camera_button_colour = Color.from_string(driver.find_element(By.CSS_SELECTOR,'#root > div._room_17y9i_1 > div._toolbar_10g91_1 > button:nth-child(1) > div._button_183cn_6._button-white-red_183cn_30').value_of_css_property('color'))
assert camera_button_colour.rgba == 'rgba(220, 38, 37, 1)'
mic_button_colour = Color.from_string(driver.find_element(By.CSS_SELECTOR, "#root > div._room_17y9i_1 > div._toolbar_10g91_1 > button:nth-child(2) > div._button_183cn_6._button-white_183cn_25").value_of_css_property('color'))
assert mic_button_colour.hex == "#000000"
sleep(1)

driver.quit()