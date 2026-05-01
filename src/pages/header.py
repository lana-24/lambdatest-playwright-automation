import logging
logger = logging.getLogger(__name__)

class HeaderComponent:
    def __init__(self, page):
        self.page = page

    def go_to_home(self):
        from src.pages.home_page import HomePage
        logger.info("click Home")
        self.page.get_by_role("link", name=" Home").click()
        return HomePage(self.page)

    def go_to_cart(self):
        from src.pages.cart_page import CartPage
        logger.info("click Cart")
        self.page.locator(".cart").click()
        return CartPage(self.page)

    def go_to_wishlist(self):
        from src.pages.wishlist_page import WishlistPage
        logger.info("click wishlist")
        self.page.get_by_role("link", name="Wishlist").click()
        return CartPage(self.page)

    
    def go_to_login(self):
        from src.pages.login_page import LoginPage
        logger.info("click Login")
        self.my_account.click()
        self.page.get_by_role("link", name=" Login").first.click() 
        return LoginPage(self.page)

    def go_to_register(self):
        from src.pages.register_page import RegisterPage
        logger.info("click Register")
        self.my_account.click()
        self.page.get_by_role("link", name=" Register").first.click()
        return RegisterPage(self.page)
    
