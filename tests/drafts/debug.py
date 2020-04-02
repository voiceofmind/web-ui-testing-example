from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('../../chromedriver')

# chrome_browser.maximize_window()
chrome_browser.get('https://www.onliner.by')


# # example of class locator
# show_message_btn = chrome_browser.find_element_by_class_name('btn-default')
# print(show_message_btn.get_attribute('innerHTML'))
#
# # input text in the form, submit and assert result
# user_message = chrome_browser.find_element_by_id('user-message')
# user_message.clear()
# user_message.send_keys('Entering some text here ...')
# show_message_btn.click()
# output_message = chrome_browser.find_element_by_id('display')
# assert 'Entering some text here ...' in output_message.text


search_input = chrome_browser.find_element_by_name('query')
# print(search_input)
search_input.send_keys('google pixel')

# print(chrome_browser.find_element_by_class_name('text_match').text())

time.sleep(1)
chrome_browser.switch_to.frame(chrome_browser.find_element_by_class_name('modal-iframe'))

print((chrome_browser.find_elements_by_class_name("product__title-link")))

found_element = chrome_browser.find_element_by_class_name("product__title-link")
found_element.click()

time.sleep(3)
chrome_browser.close()

