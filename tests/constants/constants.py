import allure
from allure_commons.types import AttachmentType


class constants:

    def __init__(self):
        print("Constants Loaded")
    @staticmethod
    def app_url():
        return "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    @staticmethod
    def take_Screenshot(driver,name):
        allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)