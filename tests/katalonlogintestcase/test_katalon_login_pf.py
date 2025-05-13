from selenium import webdriver
import pytest
import allure
import time
from tests.constants.constants import constants
from tests.constants.constants import constants
from tests.pageobjects.pageFactory.loginpage_pf import LoginPage
# from tests.pageobjects.pom.MakeAppointmentpage import MakeApp
from tests.pageobjects.pageFactory.makeappointmentpage_pf import makeapp
# from tests.pageobjects.pom.MakeAppointmentdashboardPage import dashboardPage
from tests.pageobjects.pageFactory.makeappointmentdashboardpage_pf import makeappointmentdashboard


class TestKatalonLogin:
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_katalon_login_negative_test_case(self,setup):
        driver=setup
        driver.get(constants.app_url())
        makeappobject=makeapp(driver)
        loginpage=LoginPage(driver)
        loginpage.login_to_katalon(user=self.username,pas="123")
        time.sleep(5)
        error_msg=loginpage.error_msg()
        assert error_msg=="Login failed! Please ensure the username and password are valid."
        constants.take_Screenshot(driver,"test_katalon_login_negative_test_case1")

    def test_katalon_login_positive_test_case(self,setup):
        driver=setup
        driver.get(constants.app_url())
        makeappobject=makeapp(driver)
        makeappobject.makeappointment()
        constants.take_Screenshot(driver,"dash")
        time.sleep(5)
        loginpage=LoginPage(driver)
        loginpage.login_to_katalon(user=self.username,pas=self.password)
        time.sleep(5)
        dash=makeappointmentdashboard(driver)
        dash_text=dash.linktext()
        print(driver.current_url)
        assert dash_text=="Make Appointment"
        assert "Make Appointment" in dash_text
        constants.take_Screenshot(driver,"test_katalon_login_positive_test_case01")
        time.sleep(5)