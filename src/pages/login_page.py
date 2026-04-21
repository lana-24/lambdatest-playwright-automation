from src.pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class Login(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.navigate()
        self.my_account = self.page.get_by_role("button", name=" My account ")

    def click_login(self):
        self.my_account.click()
        self.page.get_by_role("link", name=" Login").click()
        
    def fill_form(self, email=None, password=None):        
        if email:
            logger.info(f"fill email {email} ")
            self.page.get_by_placeholder("E-Mail Address").fill(email) 

            logger.debug("fill login name is done")
        else:
            logger.info("fill empty login name")
            self.page.get_by_placeholder("E-Mail Address").focus()            
            
        if password:
            logger.info("fill password")
            self.page.get_by_placeholder("Password").fill(password)
            logger.debug("fill password is done")
        else:
            logger.info("fill empty password")
            self.page.get_by_placeholder("Password").focus()

        logger.info("click Login")
        self.page.get_by_role("button", name="Login").click()

    def get_success(self):
        return self.page.get_by_role("link", name=" Edit your account information")
        
    def invalid_email_passw_error(self):
        logger.debug("get invalid email error message")
        error_text= " Warning: No match for E-Mail Address and/or Password."
        invalid_email = self.page.get_by_text(error_text)        
        return invalid_email

    def email_has_exceeded(self):
        logger.debug("get  email has exceeded error message")
        error_text= " Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        exceeded_email = self.page.get_by_text(error_text)
        return exceeded_email
    
    def click_logout(self):
        # click sign out
        logger.info('click Sign out')
        self.page.get_by_role("link", name=" Logout").click()
        expect = self.page.get_by_role("heading", name=" Account Logout")
        logger.debug(f'return {expect}')
        return expect
