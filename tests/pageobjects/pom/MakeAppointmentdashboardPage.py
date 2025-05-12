from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utils.commonUtils import wait
class dashboardPage:
    def __init__(self,driver):
        self.driver=driver

    page_title_text=(By.LINK_TEXT,"Make Appointment")

    def get_page_text(self):
        wait(driver=self.driver,element_tuple=self.page_title_text)
        return self.driver.find_element(*dashboardPage.page_title_text)

    def title_page_text(self):
        return self.get_page_text().text