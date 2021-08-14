import selenium
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("http://localhost:1667")

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# print("Current session is {}".format(driver.session_id))
# driver.quit()
# try:
#     driver.get("http://localhost:1667")
# except Exception as e:
#     print(e.message)
#



###
#driver = webdriver.Chrome(executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')


# REGISTRATION - CON_TC008
def test_registration():
    reg_data = {
        "data_username": "com1",
        "data_email": "com1@com.com",
        "data_password": "Abcd1234"
    }
    driver.get("http://localhost:1667/")
    time.sleep(2)

    sign_up = driver.find_element_by_xpath("//a[@href='#/register']")
    time.sleep(1)
    sign_up.click()
    username = driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(
        reg_data.get("data_username"))
    email = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(reg_data.get("data_email"))
    password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(
        reg_data.get("data_password"))

    bt_signup = driver.find_element_by_xpath("//button[normalize-space()='Sign up']").click()
    time.sleep(4)

    reg_success = driver.find_element_by_xpath("//div[@class='swal-text']")
    assert reg_success.text == "Your registration was successful!"
    # print(reg_success.text)

    bt_ok = driver.find_element_by_xpath("//button[normalize-space()='OK']").click()
    time.sleep(3)

    def user_check():
        driver.find_element_by_xpath(
            "//a[contains(@href,'" + reg_data.get("data_username") + "')]").click()

    user_check()
    time.sleep(3)

    # LOGOUT
    def test_log_out():
        if reg_data.get("data_username") in driver.current_url:
            log_out = driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[5]/a").click()
            time.sleep(2)

    test_log_out()


# SIGN IN - CON-TC002
def test_sign_in():
    driver.get("http://localhost:1667/")
    time.sleep(2)

    reg_data = {
        "data_username": "com1",
        "data_email": "com1@com.com",
        "data_password": "Abcd1234"
    }

    sign_in = driver.find_element_by_xpath("//a[contains(text(),\'Sign in\')]")
    sign_in.click()
    email = driver.find_element_by_xpath("//input[@placeholder='Email']")
    email.send_keys(reg_data.get("data_email"))
    password = driver.find_element_by_xpath("//input[@placeholder='Password']")
    password.send_keys(reg_data.get("data_password"))

    bt_sign_in = driver.find_element_by_xpath("//button[normalize-space()='Sign in']")
    bt_sign_in.click()
    time.sleep(3)

    def user_check():
        driver.find_element_by_xpath(
            "//a[contains(@href,'" + reg_data.get("data_username") + "')]").click()

    user_check()
    time.sleep(1)


# NEW BLOG POST - CON-TC004
def test_new_blogpost():
    # user_check()
    time.sleep(1)

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

    #
    edit = driver.find_element_by_xpath("//a[contains(@href, '#/editor/')]").click()
    time.sleep(2)

    blog_post_mod = ({
        'data_article_title': "My modified post",
        "data_article_about": "How to mod",
        "data_article_markdown": "Line after line",
        "data_tag": "2st"
    })

    article_title.click()
    article_title.clear()
    article_title.send_keys(blog_post_mod.get("data_article_title"))

    article_about.click()
    article_about.clear()
    article_about.send_keys(blog_post_mod.get("data_article_about"))

    article_markdown.click()
    article_markdown.clear()
    article_markdown.send_keys(blog_post_mod.get("data_article_markdown"))

    tag.click()
    tag.clear()
    tag.send_keys(blog_post_mod.get("data_tag"))

    bt_publish = driver.find_element_by_xpath("//button[normalize-space()='Publish Article']").click()
    time.sleep(4)

