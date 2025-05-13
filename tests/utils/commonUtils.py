from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait(driver,element_tuple):
    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located(element_tuple))

