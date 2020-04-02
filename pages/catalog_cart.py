from selenium.webdriver.common.by import By
from pages.main_page_object import MainPageObject


class Cart(MainPageObject):
    CONTENT_TITLE = (By.CLASS_NAME, "cart-form__title")
    REMOVE_PRODUCT_BTN = (By.CLASS_NAME, "cart-form__button_remove")
    PRODUCT_REMOVED_TEXT = (By.CLASS_NAME, "cart-form__description_condensed-extra")

    def __init__(self, browser):
        super().__init__(browser)

    def content_title(self):
        r = self.browser.find_element(*self.CONTENT_TITLE)
        return r.get_attribute('innerHTML')

    def click_remove_single_product(self):
        r = self.browser.find_element(*self.REMOVE_PRODUCT_BTN)
        self.browser.execute_script("arguments[0].click();", r)  # simple click doesn't work here

    def product_removed_text(self):
        r = self.browser.find_element(*self.PRODUCT_REMOVED_TEXT)
        return r.get_attribute('innerHTML')
