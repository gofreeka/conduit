import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import IEDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver = webdriver.Ie(IEDriverManager().install())

driver.get("http://localhost:1667/")

# REGISTRATION

# TODO: Check no user is logged in
# TODO: Check/rename definition names: test_ or _test
# TODO: Implement test data load from .csv

reg_data = {
    "data_username": "com2",
    "data_email": "com2@com.com",
    "data_password": "Abcd1234"
}

blog_post_data = {
    "data_article_title": "My 1st post",
    "data_article_about": "About the beginning",
    "data_article_markdown": "There was nothing.",
    "data_tag": "1st"
}


def user_check():
    check_user = driver.find_element_by_xpath("//a[contains(@href,'" + reg_data.get("data_username") + "')]").click()


def test_registration(data):
    sign_up = driver.find_element_by_xpath("//a[@href='#/register']").click()
    username = driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(reg_data.get("data_username"))
    email = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(reg_data.get("data_email"))
    password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(reg_data.get("data_password"))

    bt_signup = driver.find_element_by_xpath("//button[normalize-space()='Sign up']").click()
    time.sleep(7)

    reg_success = driver.find_element_by_xpath("//div[@class='swal-text']")
    assert reg_success.text == "Your registration was successful!"
    # print(reg_success.text)

    bt_ok = driver.find_element_by_xpath("//button[normalize-space()='OK']").click()

    user_check()
    time.sleep(1)


# LOGOUT


def test_log_out():
    if reg_data.get("data_username") in driver.current_url:
        log_out = driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[5]/a").click()
        time.sleep(2)


# SIGN IN


def test_sign_in():
    sign_in = driver.find_element_by_xpath("//a[@href='#/login']").click()
    email = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(reg_data.get("data_email"))
    password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(reg_data.get("data_password"))

    bt_sign_in = driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
    time.sleep(3)

    user_check()
    time.sleep(1)


# NEW BLOG POST


def test_new_blogpost():
    new_article = driver.find_element_by_xpath("//a[@href='#/editor']").click()
    time.sleep(2)
    article_title = driver.find_element_by_xpath("//input[@placeholder='Article Title']") \
        .send_keys(blog_post_data.get("data_article_title"))
    article_about = driver.find_element_by_xpath("//input[contains(@placeholder, 'this article about?')]") \
        .send_keys(blog_post_data.get("data_article_about"))
    article_markdown = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'markdown')]") \
        .send_keys(blog_post_data.get("data_article_markdown"))
    tag = driver.find_element_by_xpath("//input[@placeholder='Enter tags']") \
        .send_keys(blog_post_data.get("data_tag"))

    bt_publish = driver.find_element_by_xpath("//button[normalize-space()='Publish Article']").click()
    time.sleep(4)


# # EDIT BLOG POST
#
#     article_title = driver.find_element_by_xpath("//input[@placeholder='Article Title']")
#     article_about = driver.find_element_by_xpath("//input[contains(@placeholder, 'this article about?')]")
#     article_markdown = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'markdown')]")
#     tag = driver.find_element_by_xpath("//input[@placeholder='Enter tags']")
#
#
# def test_edit_blogpost(article_title, article_about, article_markdown, tag):
#     edit = driver.find_element_by_xpath("//a[contains(@href, '#/editor/')]").click()
#     time.sleep(2)
#
#     def post_clear():
#         article_title.clear()
#         article_about.clear()
#         article_markdown.clear()
#         tag.clear()
#
#     def post_mod():
#
#         blog_post_data.update({
#             'data_article_title': "My modified post",
#             "data_article_about": "How to mod",
#             "data_article_markdown": "Line after line",
#             "data_tag": "2st"
#         })
#
#         article_title.send_keys(blog_post_data.get("data_article_title"))
#         article_about.send_keys(blog_post_data.get("data_article_about"))
#         article_markdown.send_keys(blog_post_data.get("data_article_markdown"))
#         tag.send_keys(blog_post_data.get("data_tag"))
#
#     post_clear()
#     time.sleep(2)
#     post_mod()

    # bt_pub = driver.find_element_by_xpath("//button[@type='Submit']").click()

    # NoSuchElementException:
    # Message: no such element:
    # Unable to locate element: {"method":"xpath","selector":"//button[normalize-space()='Publish Article']"}


test_registration(reg_data)
test_log_out()
test_sign_in()
test_new_blogpost()
# test_edit_blogpost()
time.sleep(2)
driver.close()
