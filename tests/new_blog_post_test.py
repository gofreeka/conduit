import pytest
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


def test_001_login():
    sign_in = driver.find_element_by_xpath("//a[@href='#/login']")
    sign_in.click()

    email = driver.find_element_by_xpath("//input[@placeholder='Email']")
    password = driver.find_element_by_xpath("//input[@placeholder='Password']")

    email.send_keys(test_user_2[1])
    password.send_keys(test_user_2[2])

    bt_sign_in = driver.find_element_by_xpath("//button[normalize-space()='Sign in']")
    bt_sign_in.click()
    time.sleep(3)


global title_nbr


def test_002_user_page():
    # Find and Click user page
    global title_nbr
    user_page = driver.find_element_by_xpath("//div/ul/li/a[normalize-space()='testuser2']")
    user_page.click()
    time.sleep(2)
    title_list = driver.find_elements_by_xpath("//div/div[2]/div/div/div[2]/div/div/div/a/h1")
    title_nbr = len(title_list)


def test_003_new_blog_post():

    time.sleep(2)
    new_article = driver.find_element_by_xpath("//a[@href='#/editor']")
    time.sleep(1)
    new_article.click()
    time.sleep(2)

    article_title = driver.find_element_by_xpath("//input[@placeholder='Article Title']")
    article_about = driver.find_element_by_xpath("//input[contains(@placeholder, 'this article about?')]")
    article_markdown = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'markdown')]")
    tag = driver.find_element_by_xpath("//input[@placeholder='Enter tags']")

    bt_publish = driver.find_element_by_xpath("//button[normalize-space()='Publish Article']")

    def find_and_clear_by_xpath():
        article_title.click()
        article_title.clear()
        time.sleep(1)
        article_about.click()
        article_about.clear()
        time.sleep(1)
        article_markdown.click()
        article_markdown.clear()
        time.sleep(1)
        tag.click()
        tag.clear()
        time.sleep(1)

    with open('tests/test_data_blogpost.csv', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)

        for row in csvreader:
            print(row)
            find_and_clear_by_xpath()
            article_title.send_keys(row[0])
            time.sleep(1)
            article_about.send_keys(row[1])
            time.sleep(1)
            article_markdown.send_keys(row[2])
            time.sleep(1)
            tag.send_keys(row[3])
            time.sleep(3)

            bt_publish.click()
            time.sleep(5)
            new_article.click()
            time.sleep(3)
            find_and_clear_by_xpath()
            time.sleep(3)


def test_004_user_page_after():
    # Find and Click user page
    global title_nbr
    user_page = driver.find_element_by_xpath("//div/ul/li/a[normalize-space()='testuser2']")
    user_page.click()
    time.sleep(2)
    new_title_list = driver.find_elements_by_xpath("//div/div[2]/div/div/div[2]/div/div/div/a/h1")
    new_title_nbr = len(new_title_list)
    assert new_title_nbr != title_nbr
