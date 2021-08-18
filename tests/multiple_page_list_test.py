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

global nbr_of_page_link
global pnr_step


def test_001_sign_in():
    sign_in = driver.find_element_by_xpath("//a[@href='#/login']")
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


def test_003_user_page():
    # Find and Click user page
    user_page = driver.find_element_by_xpath("//div/ul/li/a[normalize-space()='testuser1']")
    user_page.click()
    time.sleep(2)


def test_004_pages():
    global nbr_of_page_link
    global pnr_step
    pages = driver.find_elements_by_xpath('//div/nav/ul/li')
    page_link = driver.find_elements_by_xpath('//div/nav/ul/li/a')
    nbr_of_page_link = len(pages)
    print(nbr_of_page_link)

    for pnr in page_link:
        global pnr_step
        article_title = driver.find_elements_by_xpath("//div/div[2]/div/div/div[2]/div/div/div/a/h1")
        article_nbr = len(article_title)
        pnr.click()
        print(pnr.text)
        pnr_step = int(pnr.text)
        print(article_nbr)


def test_005_check_page_numbers():
    global nbr_of_page_link
    global pnr_step
    print(nbr_of_page_link)
    print(pnr_step)
    assert nbr_of_page_link == int(pnr_step)


time.sleep(4)

