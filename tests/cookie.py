import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

driver.get(URL)
time.sleep(3)

# Adatvedelmi nyilatkozat hasznalata


def cookie():

    def check_cookies():
        cookies = driver.get_cookies()
        for coo in cookies:
            print(coo)

    check_cookies()

    cookie_bar = driver.find_element_by_id("cookie-policy-panel")
    assert cookie_bar.is_displayed()
    accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')

    accept.click()
    driver.refresh()
    check_cookies()
    driver.delete_all_cookies()

    driver.refresh()
    check_cookies()

    decline = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[1]')
    decline.click()
    check_cookies()
