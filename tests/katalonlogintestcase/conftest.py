from selenium import webdriver
import pytest
import allure
from dotenv import load_dotenv
load_dotenv()
import os

@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    username=os.getenv("USERNAME_1")
    password=os.getenv("PASSWORD")
    request.cls.driver=driver
    request.cls.username=username
    request.cls.password=password
    yield driver
    driver.quit()