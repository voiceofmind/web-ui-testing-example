from selenium.webdriver.common.by import By
from pages.main_page_object import MainPageObject


class HomePage(MainPageObject):
    URL = "https://www.onliner.by"
    SEARCH_INPUT = (By.NAME, "query")
    SEARCH_RESULTS = (By.CLASS_NAME, "search__result")
    SEARCH_INPUT_POP_UP = (By.CLASS_NAME, "search__input")

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(self.URL)
