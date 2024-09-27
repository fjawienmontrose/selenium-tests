import pytest  
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service as ChromeService  
# from webdriver_manager.chrome import ChromeDriverManager  

@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1, 
})
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
