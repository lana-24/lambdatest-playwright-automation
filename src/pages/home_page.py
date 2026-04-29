from src.pages.base_page import BasePage
from src.pages.login_page import LoginPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.navigate()
        return self

    def go_to_login(self):
        self.page.get_by_role("button", name=" My account ").click()
        # self.page.get_by_role("link", name=" Login").click() 
        return LoginPage(self.page)
