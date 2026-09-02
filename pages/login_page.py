from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"
        self.header = self.page.get_by_text("Swag Labs")
        self.username_textbox = self.page.get_by_role("textbox", name="Username")
        self.password_textbox = self.page.get_by_role("textbox", name="Password")
        self.login_button = self.page.get_by_role("button", name= "Login")
        self.error_message = self.page.get_by_test_id("error")

    def verify_loaded(self):
        expect(self.header).to_be_visible()

    def perform_login(self, username, password):
        self.username_textbox.fill(username)
        self.password_textbox.fill(password)
        self.login_button.click()

    def navigate(self):
        self.page.goto(self.url)

    def verify_error_message(self):
        expect(self.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")
