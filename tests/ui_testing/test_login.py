from playwright.sync_api import expect
import logging
# from src.pages.login_page import LoginPage
from src.pages.login_page import HomePage
from src.config.config import EMAIL, PASSWORD
logger = logging.getLogger(__name__)

# LGN-01
def test_login(page):
    logger.info("starting test login")
    home_page = HomePage(page)
    login_page = home_page.open().go_to_login()
    login_page.fill_form(EMAIL, PASSWORD)
    success = login_page.get_success()
    logger.info("try login verification successful")
    expect(success).to_be_visible()
    logger.info("test login success")
    
# LGN-02
def test_login_invalid_email(page):
    logger.info("starting login with invalid email")
    home_page = HomePage(page)
    login_page = home_page.open().go_to_login()
    login_page.fill_form("userqa@qa.com", PASSWORD)
    error1 = login_page.invalid_email_passw_error()
    error2 = login_page.email_has_exceeded()
    logger.info("try login verification error")
    if error1.is_visible():
        expect(error1).to_be_visible()
        logger.info("email invalid, login error ")
    else:
        expect(error2).to_be_visible()
        logger.info("email has exceeded, login error ")

# LGN-03
def test_login_invalid_password(page):
    logger.info("starting login with invalid password")
    home_page = HomePage(page)
    login_page = home_page.open().go_to_login()
    login_page.fill_form(EMAIL, "password")
    error = login_page.invalid_email_passw_error()
    logger.info("try login verification error")
    expect(error).to_be_visible()
    logger.info("test done, login error")
    
# LGN-04
def test_logout(page):
    home_page = HomePage(page)
    login_page = home_page.open().go_to_login()
    login_page.click_login()
    login_page.fill_form(EMAIL, PASSWORD)
    success = login_page.get_success()
    logger.info("verification login success")
    expect(success).to_be_visible()
    logout = login_page.click_logout()
    logger.info("verification logout success")
    expect(logout).to_be_visible()
    logger.info("test done, user have logout")
