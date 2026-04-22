from src.pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class Register(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.navigate()
        self.my_account = self.page.get_by_role("button", name=" My account ")

    def click_register(self):
        self.my_account.click()
        self.page.get_by_role("link", name=" Register").first.click()

    def fill_name(self, firstname=None, lastname=None):
        if firstname:
            logger.info(f"fill firstname: {firstname}")
            self.page.get_by_role("textbox", name="First Name").fill(firstname)
        else:
            logger.info("fill empty firstname")
            self.page.get_by_role("textbox", name="First Name").focus()
            
        if lastname:
            logger.info(f"fill lastname: {lastname}")
            self.page.get_by_role("textbox", name="Last Name").fill(lastname)
        else:
            logger.info("fill empty lastname")
            self.page.get_by_role("textbox", name="Last Name").focus()

    def fill_email(self, email=None):
        if email:
            logger.info(f"fill email: {email}")
            self.page.get_by_role("textbox", name="E-Mail").fill(email)
        else:
            logger.info("fill empty email")
            self.page.get_by_role("textbox", name="E-Mail").focus()

    def fill_telephone(self, telephone=None):
        if telephone:
            logger.info(f"fill telephone: {telephone}")
            self.page.get_by_role("textbox", name="Telephone").fill(telephone)
        else:
            logger.info("fill empty telephone")
            self.page.get_by_role("textbox", name="Telephone").focus()

    def fill_password(self, password=None, confirm_pass=None):
        if password:
            logger.info("fill password")
            self.page.get_by_role("textbox", name="Password").first.fill(password)
        else:
            logger.info("fill empty password")
            self.page.get_by_role("textbox", name="Password").focus()

        if confirm_pass:
            logger.info("fill confirm password")
            self.page.get_by_role("textbox", name="Password Confirm").fill(confirm_pass)
        else:
            logger.info("fill empty confirm password")
            self.page.get_by_role("textbox", name="Password Confirm").focus()

    def check(self):
        logger.info("check Privacy and Policy")
        self.page.get_by_text("I have read and agree to the ").click()

    def submit(self):
        logger.info("submit")
        self.page.get_by_role("button", name="Continue").click()

    def verifying_success(self):
        success = " Your Account Has Been Created!"
        text = self.page.get_by_text(success)
        button = self.page.get_by_role("link", name="Continue")
        logger.debug(f"return 2 locator")
        return text, button
    
    def email_already(self):
        error = "Warning: E-Mail Address is already registered!"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error)

    def firstname_error(self):
        error = "First Name must be between 1 and 32 characters!"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error)

    def lastname_error(self):
        error = "Last Name must be between 1 and 32 characters!"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error)

    def empty_email(self):
        error = "E-Mail Address does not appear to be valid!"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error)

    def invalid_email(self):
        error = "Please include"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error, exact=False)


    def telephone_error(self):
        error = "Telephone must be between 3 and 32 characters!"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error)

    def password_error(self):
        error = "Password must be between 4 and 20 characters!"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error)

    def password_confirm_error(self):
        error = "Password confirmation does not match password!"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error)

    def uncheck_error(self):
        error = "Warning: You must agree to the Privacy Policy!"
        logger.debug(f"return {error}")
        return self.page.get_by_text(error)
