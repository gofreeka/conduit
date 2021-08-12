from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = 'http://localhost:1667/'
driver.get(URL)

test_user_1 = ["testuser1", "testuser1@example.com", "Abcd123$"]
test_user_2 = ["testuser2", "testuser2@example.com", "Abcd123$"]
test_user_3 = ["testuser3", "testuser3@example.com", "Abcd123$"]
test_user_4 = ["testuser4", "testuser4@example.com", "Abcd123$"]
test_user_5 = ["testuser5", "testuser5@example.com", "Abcd123$"]

# LOGOUT


def test_log_out():
    username = driver.find_element_by_xpath("//div/nav/div/ul/li[4]/a").text
    assert "testuser1" == username

    log_out_bt = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    log_out_bt.click()

    # if test_user_1[0] in driver.current_url:
    #     log_out = driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[5]/a").click()
    #     time.sleep(2)
