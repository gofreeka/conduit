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


def test_001_sign_in():

    time.sleep(2)

    sign_in = driver.find_element_by_xpath("//a[@href='#/login']")
    sign_in.click()

    email = driver.find_element_by_xpath("//input[@placeholder='Email']")
    password = driver.find_element_by_xpath("//input[@placeholder='Password']")

    email.send_keys(test_user_3[1])
    password.send_keys(test_user_3[2])

    bt_sign_in = driver.find_element_by_xpath("//button[normalize-space()='Sign in']")
    bt_sign_in.click()
    time.sleep(3)


def test_002_user_check():
    assert test_user_3[0] == driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[4]/a").text


def test_003_mod_data():

    test_data_short_bio = ["Short bio example 1", "Short bio example 2", "Short bio example 3"]

    # Find and Click user page
    driver.find_element_by_xpath("//div/ul/li/a[normalize-space()='testuser3']").click()

    # Edit Profile Settings Click:
    edit_prof_settings = driver.find_element_by_xpath("//a[@href='#/settings']")
    edit_prof_settings.click()
    time.sleep(2)

    # "Short bio about you"
    # Find:
    short_bio_txt_area = driver.find_element_by_xpath("//fieldset/textarea[@placeholder='Short bio about you']")

    # Clear
    def short_bio_clear():
        short_bio_txt_area.click()
        time.sleep(2)
        short_bio_txt_area.clear()

    short_bio_clear()

    # Fill out with test data
    short_bio_txt_area.send_keys(test_data_short_bio[0])
    time.sleep(2)

    # Update Settings:
    # Find button
    update_settings_btn = driver.find_element_by_xpath("//form/fieldset/button[normalize-space()='Update Settings']")

    # Click Update Settings button and click OK button
    def update_bio_settings():
        update_settings_btn.click()
        time.sleep(2)
        update_btn = driver.find_element_by_xpath("//div/button[normalize-space()='OK']")
        update_btn.click()
        time.sleep(2)

    update_bio_settings()

    # Assert test data == Short bio content
    assert test_data_short_bio[0] == short_bio_txt_area.get_attribute("value")

    # "Short bio about you" Click and Clear
    short_bio_clear()

    # Fill out with test data
    short_bio_txt_area.send_keys(test_data_short_bio[1])

    # Update Settings
    update_bio_settings()

    # Assert test data == Short bio content
    assert test_data_short_bio[1] == short_bio_txt_area.get_attribute("value")
