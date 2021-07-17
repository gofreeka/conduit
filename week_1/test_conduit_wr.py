# import time
#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# # from webdriver_manager.firefox import GeckoDriverManager
# # from webdriver_manager.microsoft import IEDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# # driver = webdriver.Ie(IEDriverManager().install())
#
# driver.get("http://localhost:1667/")
# time.sleep(2)
#
#
# reg_data = {
#             "data_username": "com2",
#             "data_email": "com2@com.com",
#             "data_password": "Abcd1234"
#             }
#
# blog_post_data = {
#     "data_article_title": "My 1st post",
#     "data_article_about": "About the beginning",
#     "data_article_markdown": "There was nothing.",
#     "data_tag": "1st"
# }


# def user_check():
#     check_user = driver.find_element_by_xpath("//a[contains(@href,'" + reg_data.get("data_username") + "')]").click()
#

# REGISTRATION - CON-TC008
# TODO: Check no user is logged in


def test_registration():
    import time

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    # from webdriver_manager.firefox import GeckoDriverManager
    # from webdriver_manager.microsoft import IEDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver = webdriver.Ie(IEDriverManager().install())

    driver.get("http://localhost:1667/")
    time.sleep(2)

    reg_data = {
        "data_username": "com2",
        "data_email": "com2@com.com",
        "data_password": "Abcd1234"
    }

    sign_up = driver.find_element_by_xpath("//a[@href='#/register']")
    time.sleep(1)
    sign_up.click()
    username = driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(reg_data.get("data_username"))
    email = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(reg_data.get("data_email"))
    password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(reg_data.get("data_password"))

    bt_signup = driver.find_element_by_xpath("//button[normalize-space()='Sign up']").click()
    time.sleep(5)

    reg_success = driver.find_element_by_xpath("//div[@class='swal-text']")
    assert reg_success.text == "Your registration was successful!"
    # print(reg_success.text)

    bt_ok = driver.find_element_by_xpath("//button[normalize-space()='OK']").click()

    def user_check():
        check_user = driver.find_element_by_xpath(
            "//a[contains(@href,'" + reg_data.get("data_username") + "')]").click()

    user_check()
    time.sleep(1)
    driver.close()


# LOG OUT
#
#
# def test_log_out():
#     if reg_data.get("data_username") in driver.current_url:
#         log_out = driver.find_element_by_xpath("//div[@id='app']/nav/div/ul/li[5]/a").click()
#         time.sleep(2)
#
#

# SIGN IN - CON-TC002


def test_sign_in():
    import time

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    # from webdriver_manager.firefox import GeckoDriverManager
    # from webdriver_manager.microsoft import IEDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver = webdriver.Ie(IEDriverManager().install())

    driver.get("http://localhost:1667/")
    time.sleep(2)

    reg_data = {
        "data_username": "com2",
        "data_email": "com2@com.com",
        "data_password": "Abcd1234"
    }

    # sign_in = driver.find_element_by_xpath("//a[@href='#/login']")
    sign_in = driver.find_element_by_xpath("//a[contains(text(),\'Sign in\')]")
    # sign_in = driver.find_element_by_xpath("//a[contains(@text,'Sign in')]")
    sign_in.click()
    email = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(reg_data.get("data_email"))
    password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(reg_data.get("data_password"))

    bt_sign_in = driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
    time.sleep(3)

    def user_check():
        check_user = driver.find_element_by_xpath(
            "//a[contains(@href,'" + reg_data.get("data_username") + "')]").click()

    user_check()
    time.sleep(1)
    driver.close()

# NEW BLOG POST - CON-TC004


def test_new_blogpost():

    import time

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    # from webdriver_manager.firefox import GeckoDriverManager
    # from webdriver_manager.microsoft import IEDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver = webdriver.Ie(IEDriverManager().install())

    driver.get("http://localhost:1667/")
    time.sleep(2)

    reg_data = {
        "data_username": "com2",
        "data_email": "com2@com.com",
        "data_password": "Abcd1234"
    }

    # sign_in = driver.find_element_by_xpath("//a[@href='#/login']")
    sign_in = driver.find_element_by_xpath("//a[contains(text(),\'Sign in\')]")
    # sign_in = driver.find_element_by_xpath("//a[contains(@text,'Sign in')]")
    sign_in.click()
    email = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(reg_data.get("data_email"))
    password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(reg_data.get("data_password"))

    bt_sign_in = driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
    time.sleep(3)

    def user_check():
        check_user = driver.find_element_by_xpath(
            "//a[contains(@href,'" + reg_data.get("data_username") + "')]").click()

    user_check()
    time.sleep(1)

    blog_post_data = {
        "data_article_title": "My 1st post",
        "data_article_about": "About the beginning",
        "data_article_markdown": "There was nothing.",
        "data_tag": "1st"
    }

    new_article = driver.find_element_by_xpath("//a[@href='#/editor']")
    new_article.click()
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
    driver.close()

# test_registration()
# test_log_out()
# test_sign_in()
# test_new_blogpost()
