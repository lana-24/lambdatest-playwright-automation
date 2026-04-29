import pytest
from playwright.sync_api import expect
import logging
# from src.pages.register_page import RegisterPage
from src.pages.home_page import HomePage
from src.config.config import EMAIL
from src.utils.test_data_generator import TestData


logger = logging.getLogger(__name__)


# RGT-01
def test_register(page, max_attempts=3):
    logger.info("start test register")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()
    for _ in range(max_attempts):
        register_page.fill_name(TestData.first_name(), TestData.last_name())
        register_page.fill_email(TestData.valid_email())
        register_page.fill_telephone(TestData.phone_number())
        password = TestData.valid_password()
        register_page.fill_password(password, password)
        register_page.check()
        register_page.submit()

        error = register_page.email_already()
        if not error.is_visible():
            logger.debug("nothing error")
            break

    locator = register_page.verifying_success()
    logger.info("verifying success register")
    expect(locator[0]).to_be_visible()
    expect(locator[1]).to_be_enabled()

# RGT-02
def test_firstname_less_than_min(page):
    logger.info("start test firstname less than min")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()
    register_page.fill_name(lastname=TestData.last_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    register_page.submit()
    message = register_page.firstname_error()
    logger.info("verifying firstname error")
    expect(message).to_be_visible()

# RGT-03
def test_firstname_more_than_max(page):
    logger.info("start test firstname more than max")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()
    register_page.fill_name(TestData.long_text(), TestData.last_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    register_page.submit()
    message = register_page.firstname_error()
    logger.info("verifying firstname error")
    expect(message).to_be_visible()


# RGT-04
def test_lastname_less_than_min(page):
    logger.info("start test lastname less than min")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    register_page.submit()
    message = register_page.lastname_error()
    logger.info("verifying lastname error")
    expect(message).to_be_visible()


# RGT-05
def test_lastname_more_than_max(page):
    logger.info("start test lastname more than max")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.long_text())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    register_page.submit()
    message = register_page.lastname_error()
    logger.info("verifying lastname error")
    expect(message).to_be_visible()


# RGT-06
def test_invalid_email(page):
    current_url = page.url
    logger.info("start test invalid email")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email(TestData.invalid_email())
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    current_url = page.url
    register_page.submit()
    message = register_page.invalid_email()
    logger.info("verifying invalid email error")
    assert page.url == current_url
    

# RGT-07
def test_empty_email(page):
    logger.info("start test invalid email")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email()
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    register_page.submit()
    message = register_page.empty_email()
    logger.info("verifying invalid email error")
    expect(message).to_be_visible()


# RGT-08
def test_email_already_registered(page):
    logger.info("start test  email already registered")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email(EMAIL)
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    register_page.submit()
    message = register_page.email_already()
    logger.info("verifying email already registered error")
    expect(message).to_be_visible()


# RGT-09
def test_telephone_less_than_min(page):
    logger.info("start test number telephone less than min")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone("01")
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    register_page.submit()
    message = register_page.telephone_error()
    logger.info("verifying telephone error")
    expect(message).to_be_visible()


# RGT-10
def test_telephone_more_than_max(page):
    logger.info("start test number telephone more than max")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.long_phone())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.check()
    register_page.submit()
    message = register_page.telephone_error()
    logger.info("verifying telephone error")
    expect(message).to_be_visible()


# RGT-11
def test_password_less_than_min(page):
    logger.info("start test password less than min")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    register_page.fill_password("no", "no")
    register_page.check()
    register_page.submit()
    message = register_page.password_error()
    logger.info("verifying password error")
    expect(message).to_be_visible()

@pytest.mark.xfail(reason="Bug: register success")
# RGT-12
def test_password_more_than_max(page):
    logger.info("start test password more than max")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    register_page.fill_password(TestData.long_text(), TestData.long_text())
    register_page.check()
    register_page.submit()
    message = register_page.password_error()
    logger.info("verifying password error")
    expect(message).to_be_visible()


# RGT-13
def test_wrong_password_confirm(page):
    logger.info("start test wrong password confirm")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, "invalidpassword")
    register_page.check()
    register_page.submit()
    message = register_page.password_confirm_error()
    logger.info("verifying password confirm error")
    expect(message).to_be_visible()


# RGT-14
def test_uncheck_privay_policy(page):
    logger.info("start test uncheck Privacy Policy")
    home_page = HomePage(page)
    register_page = home_page.open().go_to_register()    
    register_page.fill_name(TestData.first_name(), TestData.last_name())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register_page.fill_password(password, password)
    register_page.submit()
    message = register_page.uncheck_error()
    logger.info("verifying uncheck error message")
    expect(message).to_be_visible()



