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

# Bejelentkezes


def test_001_sign_in():

    time.sleep(5)

    sign_in = driver.find_element_by_xpath("//a[@href='#/login']")
    #sign_in = driver.find_element_by_xpath("//a[normalize-space()='Sign in']")
    sign_in.click()

    email = driver.find_element_by_xpath("//input[@placeholder='Email']")
    password = driver.find_element_by_xpath("//input[@placeholder='Password']")

    email.send_keys(test_user_1[1])
    password.send_keys(test_user_1[2])

    bt_sign_in = driver.find_element_by_xpath("//button[normalize-space()='Sign in']")
    bt_sign_in.click()
    time.sleep(3)


def test_002_user_check():
    assert test_user_1[0] == driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[4]/a").text


time.sleep(1)

# driver.close()
