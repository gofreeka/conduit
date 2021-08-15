from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = 'http://localhost:1667/'
driver.get(URL)

# REGISTRATION - CON_TC008


def test_registration():

    test_data_registration = ["RegUser1", "reguser1@example.com", "Abcd123$"]

    sign_up = driver.find_element_by_xpath("//a[@href='#/register']")
    time.sleep(1)
    sign_up.click()

    username = driver.find_element_by_xpath("//input[@placeholder='Username']")
    email = driver.find_element_by_xpath("//input[@placeholder='Email']")
    password = driver.find_element_by_xpath("//input[@placeholder='Password']")

    username.send_keys(test_data_registration[0])
    email.send_keys(test_data_registration[1])
    password.send_keys(test_data_registration[2])

    bt_signup = driver.find_element_by_xpath("//button[normalize-space()='Sign up']")
    bt_signup.click()
    time.sleep(4)

    reg_success = driver.find_element_by_xpath("//div[@class='swal-text']")
    assert reg_success.text == "Your registration was successful!"

    bt_ok = driver.find_element_by_xpath("//button[normalize-space()='OK']")
    bt_ok.click()
    time.sleep(3)

    def user_check():
        assert test_data_registration[0] == driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[4]/a").text

    user_check()
    time.sleep(3)
