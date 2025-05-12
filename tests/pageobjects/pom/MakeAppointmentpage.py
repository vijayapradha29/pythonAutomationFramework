from selenium import webdriver
from selenium.webdriver.common.by import By


class MakeApp:
    def __init__(self,driver):
        self.driver=driver

    make_Appointment_element=(By.ID,"btn-make-appointment")

    def get_make_Appointment(self):
        return self.driver.find_element(*MakeApp.make_Appointment_element)

    def make_App(self):
        self.get_make_Appointment().click()