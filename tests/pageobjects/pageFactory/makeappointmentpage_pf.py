from seleniumpagefactory.Pagefactory import PageFactory

class makeapp(PageFactory):
    def __init__(self,driver):
        self.driver=driver
        self.highlight=True

    locators={
        'makeapp':('ID',"btn-make-appointment")
    }

    def makeappointment(self):
        self.makeapp.click_button()