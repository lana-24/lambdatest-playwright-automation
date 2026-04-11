from src.config.config import UI_BASE_URL

class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, endpoint=None):
        if endpoint:
            self.page.goto(f'UI_BASE_URL{endpoint}', wait_until='commit')
        else:
            self.page.goto(UI_BASE_URL, wait_until='commit')
