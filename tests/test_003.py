from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from test_002 import test_001_sign_in

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = 'http://localhost:1667/'
driver.get(URL)

# test_user_1 = ["testuser1", "testuser1@example.com", "Abcd123$"]
# test_user_2 = ["testuser2", "testuser2@example.com", "Abcd123$"]
# test_user_3 = ["testuser3", "testuser3@example.com", "Abcd123$"]
# test_user_4 = ["testuser4", "testuser4@example.com", "Abcd123$"]
# test_user_5 = ["testuser5", "testuser5@example.com", "Abcd123$"]

#
#
# def test_001_login():
#

# NEW BLOG POST - CON-TC004


def test_002_new_blog_post():

    # Bejelentkezes
    test_001_sign_in()
    blog_post_data = {
        "data_article_title": "My 1st post",
        "data_article_about": "About the beginning",
        "data_article_markdown": "There was nothing.",
        "data_tag": "1st"
    }

    new_article = driver.find_element_by_xpath("//a[@href='#/editor']")
    time.sleep(2)
    new_article.click()
    time.sleep(2)

    article_title = driver.find_element_by_xpath("//input[@placeholder='Article Title']")
    article_title.send_keys(blog_post_data.get("data_article_title"))

    article_about = driver.find_element_by_xpath("//input[contains(@placeholder, 'this article about?')]")
    article_about.send_keys(blog_post_data.get("data_article_about"))

    article_markdown = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'markdown')]")
    article_markdown.send_keys(blog_post_data.get("data_article_markdown"))

    tag = driver.find_element_by_xpath("//input[@placeholder='Enter tags']")
    tag.send_keys(blog_post_data.get("data_tag"))

    bt_publish = driver.find_element_by_xpath("//button[normalize-space()='Publish Article']")
    bt_publish.click()
    time.sleep(4)

time.sleep(1)


# LOGOUT


def test_003_log_out():
    username = driver.find_element_by_xpath("//div/nav/div/ul/li[4]/a")
    assert "#/@testuser1/" == username.get_property("href")

    log_out_bt = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    log_out_bt.click()

    # if test_user_1[0] in driver.current_url:
    #     log_out = driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[5]/a").click()
    #     time.sleep(2)
