from playwright.sync_api import expect


class ProductPage:

    def __init__(self, page):
        self.page = page
        self.header = self.page.get_by_text("Products")

    def verify_loaded(self):
        expect(self.header).to_be_visible()