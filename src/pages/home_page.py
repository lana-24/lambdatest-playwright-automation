from src.pages.base_page import BasePage
from src.pages.product_page import ProductPage
from typing import Literal
import logging

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_account = self.page.get_by_role("button", name=" My account ")
        
    def open(self):
        logger.debug("open the url")
        self.navigate()
        return self
    
    def click_product(self, product_name: Literal[""]):
        logger.info(f"click product: {product_name}")
        self.page.get_by_role(product_name)
        return ProductPage(self.page)
