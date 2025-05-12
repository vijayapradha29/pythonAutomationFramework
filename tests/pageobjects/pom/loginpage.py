from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utils.commonUtils import wait

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    username_element=(By.NAME,"username")
    password_element=(By.NAME,"password")
    login_element=(By.ID,"btn-login")
    error_msg=(By.XPATH,"//p[contains(text(),'Login failed!')]")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username_element)
    def get_password(self):
        return self.driver.find_element(*LoginPage.password_element)
    def get_login(self):
        return self.driver.find_element(*LoginPage.login_element)
    def get_error(self):
        wait(driver=self.driver, element_tuple=self.username_element)
        return self.driver.find_element(*LoginPage.error_msg)

    def katalon_login(self,user,pas):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pas)
        self.get_login().click()

    def error_msg_text(self):
        return self.get_error().text