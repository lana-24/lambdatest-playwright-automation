from playwright.sync_api import expect
import logging
from src.pages.login_page import Login
from src.config.config import EMAIL, PASSWORD
logger = logging.getLogger(__name__)

# LGN-01
def test_login(page):
    logger.info("starting test login")
    login = Login(page)
    login.click_login()
    login.fill_form(EMAIL, PASSWORD)
    success = login.get_success()
    logger.info("try login verification successful")
    expect(success).to_be_visible()
    logger.info("test login success")
    
# LGN-02
def test_login_invalid_email(page):
    logger.info("starting login with invalid email")
    login = Login(page)
    login.click_login()
    login.fill_form("userqa@qa.com", PASSWORD)
    error1 = login.invalid_email_passw_error()
    error2 = login.email_has_exceeded()
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
    login = Login(page)
    login.click_login()
    login.fill_form(EMAIL, "password")
    error = login.invalid_email_passw_error()
    logger.info("try login verification error")
    expect(error).to_be_visible()
    logger.info("test done, login error")
    
# LGN-04
def test_logout(page):
    logger.info("starting logout test")
    login = Login(page)
    login.click_login()
    login.fill_form(EMAIL, PASSWORD)
    success = login.get_success()
    logger.info("verification login success")
    expect(success).to_be_visible()
    logout = login.click_logout()
    logger.info("verification logout success")
    expect(logout).to_be_visible()
    logger.info("test done, user have logout")
