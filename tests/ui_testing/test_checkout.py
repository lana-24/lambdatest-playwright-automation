from playwright.sync_api import expect
import logging
from src.pages.home_page import HomePage
from src.config.config import EMAIL, PASSWORD
from src.utils.test_data_generator import TestData
logger = logging.getLogger(__name__)

# CHK-01
def test_checkout_guest_account(page):
    logger.info("starting test checkout(guest account)")
    home_page = HomePage(page)
    home_page.open()
    product_page = home_page.click_product("HP LP3065")
    checkout_page = product_page.click_buy()
    checkout_page.select_guest()
    checkout_page.fill_fname_lname(TestData.firstname(), TestData.lastname())
    checkout_page.fill_phone(TestData.phone_number())
    checkout_page.fill_email(TestData.valid_email())
    checkout_page.fill_address("jalan erlangga")
    checkout_page.fill_city("pass")
    checkout_page.fill_country_region()
    checkout_page.check_privacy_policy()
    checkout_confirm_page = checkout.click_continue()
    checkout_confirm_page.click_confirm_order()
    success = checkout_confirm_page.verifying_checkout_success()
    logger.info("try checkout success verification ")
    expect(success).to_be_visible()
    logger.info("test checkout(guest) success")

# CHK-02
def test_checkout_register_account(page):
    logger.info("starting test checkout(register account)")
    home_page = HomePage(page)
    home_page.open()
    product_page = home_page.click_product("HP LP3065")
    checkout_page = product_page.click_buy()
    register_page = checkout_page.select_register()
    register_page.fill_name(TestData.firstname(), TestData.lastname())
    register_page.fill_email(TestData.valid_email())
    register_page.fill_telephone(TestData.phone_number())
    register_page.fill_password(TestData.valid_password(), TestData.valid_password())
    checkout_page.fill_address("jalan erlangga")
    checkout_page.fill_city("pass")
    checkout_page.fill_country_region()
    checkout_page.check_privacy_policy()
    checkout_confirm_page = checkout.click_continue()
    checkout_confirm_page.click_confirm_order()
    success = checkout_confirm_page.verifying_checkout_success()
    logger.info("try checkout success verification ")
    expect(success).to_be_visible()
    logger.info("test checkout(register) success")

# CHK-03
def test_checkout_login_account(page):
    logger.info("starting test checkout(login account)")
    home_page = HomePage(page)
    home_page.open()
    product_page = home_page.click_product("HP LP3065")
    checkout_page = product_page.click_buy()
    checkout_page.select_login()
    checkout_page.fill_email(EMAIL, PASSWORD)
    checkout_page.click_login()
    checkout_page.fill_address("jalan erlangga")
    checkout_page.fill_city("pass")
    checkout_page.fill_country_region()
    checkout_page.check_privacy_policy()
    checkout_confirm_page = checkout.click_continue()
    checkout_confirm_page.click_confirm_order()
    success = checkout_confirm_page.verifying_checkout_success()
    logger.info("try checkout success verification ")
    expect(success).to_be_visible()
    logger.info("test checkout(login) success")
