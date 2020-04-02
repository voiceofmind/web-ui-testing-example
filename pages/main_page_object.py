class MainPageObject:

    def __init__(self, browser):
        self.browser = browser

    def page_title(self):
        return self.browser.title
