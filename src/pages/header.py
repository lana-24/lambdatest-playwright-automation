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

    def click_cart(self):        
        logger.info("click Cart")
        self.page.locator(".cart").click()

    def click_edit_cart(self):
        from src.pages.cart_page import CartPage
        logger.info("click edit cart")
        self.page.get_by_role("button",name=" Edit cart").click()
        return CartPage(self.page)
    
    def click_checkout(self):
        from src.pages.checkout_page import CheckoutPage
        logger.info("click checkout")
        self.page.get_by_role("button", name=" Checkout").click()
        logger.debug("switch to ChekcoutPage")
        return CheckoutPage(self.page)

    def go_to_wishlist(self):
        from src.pages.wishlist_page import WishlistPage
        logger.info("click wishlist")
        self.page.get_by_role("link", name="Wishlist").click()
        return WishlistPage(self.page)

    
    def go_to_login(self):
        from src.pages.login_page import LoginPage
        logger.info("click Login")
        self.page.get_by_role("button", name=" My account ").click()
        self.page.get_by_role("link", name=" Login").first.click() 
        return LoginPage(self.page)

    def go_to_register(self):
        from src.pages.register_page import RegisterPage
        logger.info("click Register")
        self.page.get_by_role("button", name=" My account ").click()
        self.page.get_by_role("link", name=" Register").first.click()
        return RegisterPage(self.page)
    
