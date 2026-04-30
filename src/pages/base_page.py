from src.config.config import UI_BASE_URL
from src.pages.header import HeaderComponent

class BasePage:
    def __init__(self, page):
        self.page = page
        self.header = HeaderComponent(self.page)

    def navigate(self, endpoint=None):
        if endpoint:
            self.page.goto(f'UI_BASE_URL{endpoint}', wait_until='commit')
        else:
            self.page.goto(UI_BASE_URL, wait_until='commit')

    """def get_header(self):
        return self.header"""
