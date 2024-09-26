import pytest
from tests.pages.dev_page import DevPage
from tests.pages.fcm_page import FcmPage
from tests.pages.call_page import CallPage
from tests.pages.end_popup import EndPopup

@pytest.mark.calls

def test_videocall(driver):

    url = "https://inpatient-video-dev.nyumc.org/"
    dev_page = DevPage(driver)

    dev_page.open_page(url)

    dev_page.video_dev_toggle()

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

    call_page = CallPage(driver)

    assert call_page.identity_name() == 1
    # assert call_page.thumbnail() == 0
    
    actual_identity = "Selenium Webdriver Doctor"
    call_page.identity_name_check(actual_identity)

    call_page.end_call()
    call_page.static_sleep()

    end_popup = EndPopup(driver)
    end_popup.wait_for_popup()