from seleniumpagefactory.Pagefactory import PageFactory


class makeappointmentdashboard(PageFactory):
    def __init__(self,driver):
        self.driver=driver
        self.highlight=True

    locators={
        'pagetitle':('XPATH',"//h2[contains(text(),'Make')]")
    }

    def linktext(self):
        return self.pagetitle.get_text()