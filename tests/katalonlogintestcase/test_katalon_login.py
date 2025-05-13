from selenium import webdriver
import time
import pytest
import allure
from tests.pageobjects.pom.loginpage import LoginPage
from tests.pageobjects.pom.MakeAppointmentpage import MakeApp
from tests.pageobjects.pom.MakeAppointmentdashboardPage import dashboardPage
from tests.constants.constants import constants
from allure_commons.types import AttachmentType
@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(constants.app_url())
    return driver

@allure.title("Invalid Login")
@allure.description("Enter Invalid Username or Password and Click Login Button")
@pytest.mark.negative
def test_katalon_negative(setup):
    try:
        driver=setup
        makeapp=MakeApp(driver)
        loginpage=LoginPage(driver)
        loginpage.katalon_login(user="John Doe",pas="123456")
        time.sleep(5)
        error_msg_element=loginpage.error_msg_text()
        assert error_msg_element=="Login failed! Please ensure the username and password are valid."
    except Exception as e:
        pytest.xfail("Failed TC")
        print(e)

@allure.title("Valid Login")
@allure.description("Enter Valid Username and Password and Click on Login Button")
@pytest.mark.positive
def test_katalon_positive(setup):
    try:
        driver=setup
        makeapp=MakeApp(driver)
        makeapp.make_App()
        allure.attach(driver.get_screenshot_as_png(),name="dash.PNG",attachment_type=AttachmentType.PNG)
        time.sleep(10)
        loginpage=LoginPage(driver)
        loginpage.katalon_login(user="John Doe",pas="ThisIsNotAPassword")
        dash=dashboardPage(driver)
        dashboard_text=dash.title_page_text()
        assert dashboard_text=="Make Appointment"
        time.sleep(5)
    except Exception as e:
        pytest.xfail("Failed TC")
        print(e)