from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

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

    email.send_keys(test_user_4[1])
    password.send_keys(test_user_4[2])

    bt_sign_in = driver.find_element_by_xpath("//button[normalize-space()='Sign in']")
    bt_sign_in.click()
    time.sleep(3)


def test_002_user_check():
    assert test_user_4[0] == driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[4]/a").text


def test_003_save_data():

    # Find and Click user page
    user_page = driver.find_element_by_xpath("//div/ul/li/a[normalize-space()='testuser4']")
    user_page.click()
    time.sleep(2)

    # Find elements
    article_title = driver.find_elements_by_xpath("//div/div[2]/div/div/div[2]/div/div/div/a/h1")
    article_link = driver.find_elements_by_xpath("//div/div[2]/div/div/div[2]/div/div/div/a[@href]")
    article_nbr = len(article_title)

    res_dict = {}
    for row in article_title:
        for link_row in article_link:
            res_dict[row.text] = link_row.get_attribute("href")
            article_link.remove(link_row)
            break

    with open('tests/saved_data.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in res_dict.items():
            writer.writerow([key, value])

    with open('tests/saved_data.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        lines = len(list(reader))

    assert lines == article_nbr
