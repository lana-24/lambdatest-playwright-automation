import pytest
from playwright.sync_api import expect
import logging
from src.pages.register_page import Register
from src.config.config import EMAIL
from src.utils.test_data_generator import TestData


logger = logging.getLogger(__name__)


# RGT-01
def test_register(page, max_attempts=3):
    logger.info("start test register")
    register = Register(page)
    register.click_register()
    for _ in range(max_attempts):
        register.fill_name(TestData.first_name(), TestData.last_name())
        register.fill_email(TestData.valid_email())
        register.fill_telephone(TestData.phone_number())
        password = TestData.valid_password()
        register.fill_password(password, password)
        register.check()
        register.submit()

        error = register.email_already()
        if not error.is_visible():
            logger.debug("nothing error")
            break

    locator = register.verifying_success()
    logger.info("verifying success register")
    expect(locator[0]).to_be_visible()
    expect(locator[1]).to_be_enabled()

# RGT-02
def test_firstname_less_than_min(page):
    logger.info("start test firstname less than min")
    register = Register(page)
    register.click_register()    
    register.fill_name(lastname=TestData.last_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    register.submit()
    message = register.firstname_error()
    logger.info("verifying firstname error")
    expect(message).to_be_visible()

# RGT-03
def test_firstname_more_than_max(page):
    logger.info("start test firstname more than max")
    register = Register(page)
    register.click_register()
    register.fill_name(TestData.long_text(), TestData.last_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    register.submit()
    message = register.firstname_error()
    logger.info("verifying firstname error")
    expect(message).to_be_visible()


# RGT-04
def test_lastname_less_than_min(page):
    logger.info("start test lastname less than min")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    register.submit()
    message = register.lastname_error()
    logger.info("verifying lastname error")
    expect(message).to_be_visible()


# RGT-05
def test_lastname_more_than_max(page):
    logger.info("start test lastname more than max")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.long_text())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    register.submit()
    message = register.lastname_error()
    logger.info("verifying lastname error")
    expect(message).to_be_visible()


# RGT-06
def test_invalid_email(page):
    current_url = page.url
    logger.info("start test invalid email")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email(TestData.invalid_email())
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    current_url = page.url
    register.submit()
    message = register.invalid_email()
    logger.info("verifying invalid email error")
    assert page.url == current_url
    

# RGT-07
def test_empty_email(page):
    logger.info("start test invalid email")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email()
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    register.submit()
    message = register.empty_email()
    logger.info("verifying invalid email error")
    expect(message).to_be_visible()


# RGT-08
def test_email_already_registered(page):
    logger.info("start test  email already registered")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email(EMAIL)
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    register.submit()
    message = register.email_already()
    logger.info("verifying email already registered error")
    expect(message).to_be_visible()


# RGT-09
def test_telephone_less_than_min(page):
    logger.info("start test number telephone less than min")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone("01")
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    register.submit()
    message = register.telephone_error()
    logger.info("verifying telephone error")
    expect(message).to_be_visible()


# RGT-10
def test_telephone_more_than_max(page):
    logger.info("start test number telephone more than max")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.long_phone())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.check()
    register.submit()
    message = register.telephone_error()
    logger.info("verifying telephone error")
    expect(message).to_be_visible()


# RGT-11
def test_password_less_than_min(page):
    logger.info("start test password less than min")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.phone_number())
    register.fill_password("no", "no")
    register.check()
    register.submit()
    message = register.password_error()
    logger.info("verifying password error")
    expect(message).to_be_visible()

@pytest.mark.xfail(reason="Bug: register success")
# RGT-12
def test_password_more_than_max(page):
    logger.info("start test password more than max")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.phone_number())
    register.fill_password(TestData.long_text(), TestData.long_text())
    register.check()
    register.submit()
    message = register.password_error()
    logger.info("verifying password error")
    expect(message).to_be_visible()


# RGT-13
def test_wrong_password_confirm(page):
    logger.info("start test wrong password confirm")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, "invalidpassword")
    register.check()
    register.submit()
    message = register.password_confirm_error()
    logger.info("verifying password confirm error")
    expect(message).to_be_visible()


# RGT-14
def test_uncheck_privay_policy(page):
    logger.info("start test uncheck Privacy Policy")
    register = Register(page)
    register.click_register()    
    register.fill_name(TestData.first_name(), TestData.last_name())
    register.fill_email(TestData.valid_email())
    register.fill_telephone(TestData.phone_number())
    password = TestData.valid_password()
    register.fill_password(password, password)
    register.submit()
    message = register.uncheck_error()
    logger.info("verifying uncheck error message")
    expect(message).to_be_visible()



