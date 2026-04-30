from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.register_page import RegisterPage
from src.pages.cart_page import CartPage
import logging

logger = logging.getLogger(__name__)



class HeaderComponent:
    def __init__(self, page):
        self.page = page

    def go_to_home(self):
        logger.info("click Home")
        self.page.get_by_role("link", name=" Home")
        return HomePage(self.page)

    def go_to_cart(self):
        logger.info("click Cart")
        self.page.locator(".cart").click()
        return CartPage(self.page)

    def go_to_wishlist(self):
        logger.info("click wishlist")
        self.page.get_by_role("link", name="Wishlist").click()
        return CartPage(self.page)

    
    def go_to_login(self):
        logger.info("click Login")
        self.my_account.click()
        self.page.get_by_role("link", name=" Login").first.click() 
        return LoginPage(self.page)

    def go_to_register(self):
        logger.info("click Register")
        self.my_account.click()
        self.page.get_by_role("link", name=" Register").first.click()
        return RegisterPage(self.page)
    
