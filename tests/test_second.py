from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = 'http://localhost:1667/'
driver.get(URL)

# Adatvedelmi nyilatkozat hasznalata


def test_cookie():

    def check_cookies():
        cookies = driver.get_cookies()
        for coo in cookies:
            print(coo)

    check_cookies()

    cookie_bar = driver.find_element_by_id("cookie-policy-panel")
    assert cookie_bar.is_displayed()
    accept = driver.find_element_by_xpath("//button[normalize-space()='I accept!']")

    accept.click()
    driver.refresh()
    check_cookies()
    driver.delete_all_cookies()

    driver.refresh()
    check_cookies()

    decline = driver.find_element_by_xpath("//button[normalize-space()='I decline!']")
    decline.click()
    check_cookies()

