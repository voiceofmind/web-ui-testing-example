from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('../../chromedriver')


# examples of commands to browser
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# example of assertions
assert 'Selenium Easy Demo' in chrome_browser.title
assert 'Show Message' in chrome_browser.page_source

# example of class locator
show_message_btn = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_btn.get_attribute('innerHTML'))

# input text in the form, submit and assert result
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Entering some text here ...')
show_message_btn.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'Entering some text here ...' in output_message.text


time.sleep(5)
chrome_browser.close()  # may not work on some versions of Chrome
# chrome_browser.quit()  # this will quit all sessions
