import pytest
from selenium import webdriver



# from selenium.webdriver import FirefoxOptions as Options


# hook for pytest plugin
def pytest_html_report_title(report):
    report.title = "Inpatient Test Automation Report"


# fixture for tests
@pytest.fixture
def inpatient_app():

    # #Headless browser - necessary for CI/CD
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)

    driver = webdriver.Firefox()

    # 1. Prestep. Navigate to GithubAPP

    # generators in python


    # PostStep. Close the App

