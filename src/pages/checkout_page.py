from src.pages.base_page import BasePage
from src.pages.login_page import LoginPage
from src.pages.register_page import RegisterPage
from src.pages.checkout_confirm_page import CheckoutConfirmPage
import logging
from typing import Literal

logger = logging.getLogger(__name__)

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def select_login(self):
        logger.info("select Login option")
        self.page.get_by_role("radio", name="Login").click(force=True)
        logger.debug("switching LoginPage")
        # return LoginPage(self.page) # menyesal karna tidak pisah function

     def click_login(self):
        logger.info("click Login")
        self.page.get_by_role("button", name="Login").first.click()
    
    def select_register(self):
        logger.info("select Register option")
        self.page.get_by_role("radio", name="Register Account").click(force=True)
        logger.debug("switching LoginPage")
        return RegisterPage(self.page)

    def select_guest(self):
        logger.info("select Guest option")
        self.page.get_by_role("radio", name="Guest Checkout").click(force=True)

    def fill_fname_lname(self, fname:str, lname:str):
        logger.info(f"fill Firstname: {fname}")
        self.page.get_by_placeholder("First Name").nth(0).fill(fname)
        logger.info(f"fill Lastname: {lname}")
        self.page.get_by_placeholder("Last Name").nth(0).fill(lname)

    def fill_email(self, email:str, password:str=None):
        logger.info(f"fill Email: {email}")
        self.page.get_by_placeholder("E-mail").nth(0).fill(email)

        if password:
            logger.info("fill password")
            self.page.get_by_placeholder("Password").fill(password)
            logger.debug("fill password is done")

    def fill_phone(self,email:str, phone: str):
        logger.info(f"fill Telephone: {phone}")        
        self.page.get_by_placeholder("Telephone").fill(phone)


    def fill_company(self, company):
        logger.info(f"fill Company: {company}")
        self.page.get_by_placeholder("Company").nth(0).fill(company)

    def fill_address(self,address1:str, address2:str=None):
        logger.info(f"fill Address1: {address1}")
        self.page.get_by_placeholder("Address 1").nth(0).fill(address1)
        if address2:
            logger.info(f"fill Address2: {address2}")
            self.page.get_by_placeholder("Address 2").nth(0).fill(address2)

    def fill_city(self,city:str = "pasuruan", postcode:str = 76723):
        logger.info(f"fill City: {city}")
        self.page.get_by_placeholder("City").nth(0).fill(city)
        logger.info(f"fill Post Code: {postcode}")
        self.page.get_by_placeholder("Post Code").nth(0).fill(postcode)

    def fill_country_region(self):
        logger.info("select Country: pasuruan")
        self.page.get_by_label("Country").first.select_option("100")
        logger.info(f"select Region: country")
        self.page.get_by_label("Region / State").first.select_option("1537")

    def check_privacy_policy(self):
        logger.info("check Term & Condition")
        privacy_policy = self.page.get_by_role("checkbox", name="I have read and agree to the ")
        privacy_policy.nth(0).check(force=True)
        if privacy_policy.count() < 1:
            privacy_policy.nth(1).check(force=True)

    def click_continue(self):
        logger.debug("click Continue")
        self.page.get_by_role("button", name="Continue ").click()
        logger.debug("switch to CheckoutConfirmPage")
        return CheckoutConfirmPage(self.page)

    def get_error(self, error_type: Literal[
            "fname",
            "lname",
            "empty_email",
            "phone",
            "uncheck",
            "address1",
            "city",
            "postcode",
            "empty_region"
    ]):
        errors = {
            "fname" : "First Name must be between 1 and 32 characters!",
            "lname" : "Last Name must be between 1 and 32 characters!",
            "empty_email" : "E-Mail Address does not appear to be valid!",
            "phone" : "Telephone must be between 3 and 32 characters!",
            "uncheck" : "Warning: You must agree to the Terms & Conditions!",
            "address1" : "Address 1 must be between 3 and 128 characters!",
            "city" : "City must be between 2 and 128 characters!",
            "postcode" : "Postcode must be between 2 and 10 characters!",
            "empty_region" : "Please select a region / state!"
}
        error = errors.get(error_type)
        logger.debug(f"get error for {error_type}")
        return self.page.get_by_text(error)
