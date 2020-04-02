from pages.home_page import HomePage
from pages.catalog_product import CatalogProductDescription, CatalogProductOffers
from pages.module_top_bar import Search, TopBar
from pages.catalog_cart import Cart


def test_search_product_add_to_cart_and_remove(browser):
    phrase = 'google pixel 4'

    # Given the onliner.by home page is displayed
    main_page = HomePage(browser)
    main_page.load()
    search_module = Search(browser)

    # When the user inputs the search phrase
    search_module.search_basic_input(phrase[0])
    search_module.switch_to_search_results_iframe()
    search_module.search_popup_input(phrase[1:])

    # Then search results contain proper products
    assert phrase in search_module.search_popup_get_value()
    assert search_module.count_results() >= 5
    for _ in search_module.found_products():
        assert phrase in _.casefold()

    # When user clicks on the first result
    search_module.click_on_first_search_result()
    product_page = CatalogProductDescription(browser)

    # Then the product page is opened
    assert phrase in product_page.page_title().casefold()
    assert phrase in product_page.product_title().casefold()

    # When user clicks on offers link
    product_page.click_on_offers()

    # Then offers page is opened
    offers_page = CatalogProductOffers(browser)
    assert 'цены' in offers_page.page_title().casefold()
    assert phrase in offers_page.content_title().casefold()

    # When the user adds first offer to cart
    offers_page.click_add_to_cart_first_offer()

    # Then the product is added to cart
    assert 'В корзине' in offers_page.link_text_add_to_cart_first_offer()
    top_bar = TopBar(browser)
    assert '1' == top_bar.num_of_products_in_cart()

    # When user clicks on cart
    top_bar.click_on_cart()

    # Then cart page is opened
    cart_page = Cart(browser)
    assert 'корзина' in cart_page.page_title().casefold()
    assert 'корзина' in cart_page.content_title().casefold()

    # When user removes the product from cart
    cart_page.click_remove_single_product()

    # Then the page shows removed status
    assert 'удал' in cart_page.product_removed_text().casefold()

