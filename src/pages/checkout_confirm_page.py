from src.pages.base_page import BasePage
from src.pages.checkout_page import CheckoutPage
import logging

logger = logging.getLogger(__name__)

class CheckoutConfirmPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def click_confirm_order(self):
        logger.info("click Confirm Order ")
        self.page.get_by_role("button", name="Confirm Order ").click()

    def click_edit(self):        
        logger.info("click Edit")
        self.page.get_by_role("button", name=" Edit")
        return CheckoutPage(self.page)

    def verifying_checkout_success(self):
        logger.debug("return self page")
        return self.page.get_by_text("Your order has been successfully processed!")
    
