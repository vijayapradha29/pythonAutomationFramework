from seleniumpagefactory.Pagefactory import PageFactory
class LoginPage(PageFactory):
    def __init__(self,driver):
        self.driver=driver
        self.highlight=True
#page locators
    locators={
            'username':('NAME',"username"),
            'password':('NAME',"password"),
            'login':('ID',"btn-login"),
            'error':('XPATH',"//p[contains(text(),'Login failed!')]")
        }
#page actions
    def login_to_katalon(self,user,pas):
        self.username.set_text(user)
        self.password.set_text(pas)
        self.login.click_button()

    def error_msg(self):
        return self.error.get_text()
