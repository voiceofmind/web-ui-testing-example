from selenium.webdriver.common.by import By
from pages.main_page_object import MainPageObject


class CatalogProductDescription(MainPageObject):
    PRODUCT_TITLE = (By.CLASS_NAME, "catalog-masthead__title")
    PRODUCT_SPECS = (By.CLASS_NAME, "product-specs")
    OFFERS_LINK = (By.CSS_SELECTOR, ".offers-description__part a.button")

    def __init__(self, browser):
        super().__init__(browser)

    def product_title(self):
        r = self.browser.find_element(*self.PRODUCT_TITLE)
        return r.get_attribute('innerHTML')

    def product_specs(self):
        r = self.browser.find_element(*self.PRODUCT_SPECS)
        return r.get_attribute('innerHTML')

    def click_on_offers(self):
        r = self.browser.find_element(*self.OFFERS_LINK)
        r.click()


class CatalogProductOffers(MainPageObject):
    CONTENT_TITLE = (By.CLASS_NAME, "catalog-masthead__title")
    FIRST_TO_CART_BUTTON = (By.CSS_SELECTOR, "tr:nth-child(1) td.b-cell-3 a.button")

    def __init__(self, browser):
        super().__init__(browser)

    def content_title(self):
        r = self.browser.find_element(*self.CONTENT_TITLE)
        return r.get_attribute('innerHTML')

    def click_add_to_cart_first_offer(self):
        r = self.browser.find_element(*self.FIRST_TO_CART_BUTTON)
        return r.click()

    def link_text_add_to_cart_first_offer(self):
        return self.browser.find_element(*self.FIRST_TO_CART_BUTTON).get_attribute('innerHTML')
