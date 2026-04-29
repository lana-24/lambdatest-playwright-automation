from src.pages.base_page import BasePage
from src.pages.login_page import LoginPage
from src.pages.register_page import RegisterPage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_account = self.page.get_by_role("button", name=" My account ")
        
    def open(self):
        self.navigate()
        return self

    def go_to_login(self):
        self.my_account.click()
        self.page.get_by_role("link", name=" Login").click() 
        return LoginPage(self.page)

    def go_to_register(self):
        self.my_account.click()
        self.page.get_by_role("link", name=" Register").first.click()
        return RegisterPage(self.page)
    
