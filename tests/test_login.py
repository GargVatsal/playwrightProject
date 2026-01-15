from playwright.sync_api import expect

def test_login(context):
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.get_by_text("Swag Labs").is_visible()
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name= "Login").click()
    expect(page.get_by_text("Products")).to_be_visible()