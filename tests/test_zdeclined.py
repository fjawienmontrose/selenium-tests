import pytest
from tests.pages.base_app import BaseApp
from tests.pages.dev_page import DevPage
from tests.pages.fcm_page import FcmPage
from tests.pages.call_page import CallPage
from tests.pages.end_popup import EndPopup
from tests.pages.declined_page import DeclinedPage

@pytest.mark.calls
def test_audiocall(driver):

    url = "https://inpatient-video-dev.nyumc.org/"
    dev_page = DevPage(driver)
    base_app = BaseApp(driver)

    dev_page.open_page(url)

    dev_page.clear_userfname()
    dev_page.clear_userlname()
    dev_page.clear_patientfname()
    dev_page.clear_patientlname()
    dev_page.enter_userfname("Selenium")
    dev_page.enter_userlname("Webdriver Doctor")
    dev_page.enter_patientfname("Selenium")
    dev_page.enter_patientlname("Webdriver Patient")

    dev_page.click_next()
    
    fcm_page = FcmPage(driver)
    fcm_page.enter_token("eUV1yw0KQaefKvqJT-ES0w:APA91bERTirrX35AKSMWfBb0_MPQyv4-qiiEtkx53OYwVzG6KdmavjBWFnhDnFO81vnLYN56cAojIhYc-IpvdRvMnRi9gyq7I3Vz507DvrhQtGwogoJuld1E-QI_yH5uuSGkoz8N-7fJ")
    fcm_page.click_call()
    fcm_page.static_sleep()
    driver.switch_to.new_window('tab')

    url = "https://inpatient-video-dev.nyumc.org/"
    dev_page = DevPage(driver)
    base_app = BaseApp(driver)
    fcm_page = FcmPage(driver)
    fcm_page.static_sleep()

    dev_page.open_page(url)

    dev_page.clear_userfname()
    dev_page.clear_userlname()
    dev_page.clear_patientfname()
    dev_page.clear_patientlname()

    dev_page.enter_userfname("Selenium")
    dev_page.enter_userlname("Webdriver Doctor")
    dev_page.enter_patientfname("Selenium")
    dev_page.enter_patientlname("Webdriver Patient")

    dev_page.click_next()

    fcm_page = FcmPage(driver)
    fcm_page.enter_token("eUV1yw0KQaefKvqJT-ES0w:APA91bERTirrX35AKSMWfBb0_MPQyv4-qiiEtkx53OYwVzG6KdmavjBWFnhDnFO81vnLYN56cAojIhYc-IpvdRvMnRi9gyq7I3Vz507DvrhQtGwogoJuld1E-QI_yH5uuSGkoz8N-7fJ")

    fcm_page.click_call()

    declined_page = DeclinedPage(driver)

    fcm_page.static_sleep()

    caller_name_text = "Selenium Webdriver Patient"
    decline_reason_text = 'We couldn\'t get the decline reason'
    decline_status_text = "Call Declined"
    
    declined_page.decline_reason_name(caller_name_text)
    declined_page.decline_reason(decline_reason_text)
    declined_page.decline_status(decline_status_text)