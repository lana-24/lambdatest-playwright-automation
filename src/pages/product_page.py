from src.pages.base_page import BasePage
from src.pages.checkout_page import CheckoutPage
import logging

logger = logging.getLogger(__name__)

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open(self, product_id = 99):
        logger.debug("open the url")
        self.navigate(f"/index.php?route=product/product&product_id={product_id}")

    def input_quantity(self, qty: int):
        logger.info(f"fill Quantity: {qty}")
        self.page.get_by_role("textbox",name="Qty").fill(qty)
        
    def click_buy(self):
        logger.info("click Buy Now")
        self.page.get_by_role("button", name="Buy now").click()
        logger.debug("switch to ChekcoutPage")
        return CheckoutPage(self.page)

    def add_to_favorite(self):
        logger.info("add products to favorite")
        self.page.locator(".btn-wishlist[title='add to Wish List']").click()



        
