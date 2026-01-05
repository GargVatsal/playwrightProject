
def test_login(context):
    page = context.new_page()
    page.goto("https://google.com")
    assert page.title() == "Google"