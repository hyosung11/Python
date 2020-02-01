from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

# chrome_browser.maximize_window()
# chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# assert 'Selenium Easy Demo' in chrome_browser.title
# show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# # print(show_message_button.get_attribute('innerHTML'))

# assert 'Show Message' in chrome_browser.page_source

# user_message = chrome_browser.find_element_by_id('user-message')
# user_button = chrome_browser.find_element_by_css_selector('#get-input > .btn')
# print(user_button)
# user_message.clear()
# user_message.send_keys('Omi is alright right now')

# show_message_button.click()
# output_message = chrome_browser.find_element_by_id('display')

# assert 'Omi is alright right now' in output_message.text

chrome_browser.close()
chrome_browser.quit()

# Wait and Sleep