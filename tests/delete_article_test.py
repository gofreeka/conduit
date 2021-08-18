import pytest
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


def test_003_new_blog_post():
    time.sleep(2)
    new_article = driver.find_element_by_xpath("//a[@href='#/editor']")
    new_article.click()
    time.sleep(3)

    article_title = driver.find_element_by_xpath("//input[@placeholder='Article Title']")
    article_about = driver.find_element_by_xpath("//input[contains(@placeholder, 'this article about?')]")
    article_markdown = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'markdown')]")
    tag = driver.find_element_by_xpath("//input[@placeholder='Enter tags']")

    bt_publish = driver.find_element_by_xpath("//button[normalize-space()='Publish Article']")

    test_data_blogpost = ["New Post", "This article is about...", "Once upon a time...", "YR"]

    article_title.send_keys(test_data_blogpost[0])
    time.sleep(1)
    article_about.send_keys(test_data_blogpost[1])
    time.sleep(1)
    article_markdown.send_keys(test_data_blogpost[2])
    time.sleep(1)
    tag.send_keys(test_data_blogpost[3])
    time.sleep(2)

    bt_publish.click()
    time.sleep(3)


def test_004_user_page():
    # Find and Click user page
    user_page = driver.find_element_by_xpath("//div/ul/li/a[normalize-space()='testuser3']")
    user_page.click()
    time.sleep(2)


def test_005_delete_article():
    title_list = driver.find_elements_by_xpath("//div/div[2]/div/div/div[2]/div/div/div/a/h1")
    time.sleep(1)
    last_item = title_list[-1]
    last_item.click()
    time.sleep(3)

    # Find Delete Article button
    delete_btn = driver.find_element_by_xpath("//div/div[1]/div/div/span/button")
    time.sleep(3)
    delete_btn.click()
    time.sleep(3)

    test_004_user_page()
    title_list_after = driver.find_elements_by_xpath("//div/div[2]/div/div/div[2]/div/div/div/a/h1")

    # assert not title_list_after == title_list
    assert len(title_list) == len(title_list_after)+1
