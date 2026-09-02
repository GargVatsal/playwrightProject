from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_login(context):
    page = context.new_page()
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    login_page.navigate()
    login_page.verify_loaded()
    login_page.perform_login("standard_user", "secret_sauce")
    product_page.verify_loaded()

def test_failed_login(context):
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.perform_login("standard_user", "incorrect_password")
    login_page.verify_error_message()