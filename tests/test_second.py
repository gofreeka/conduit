from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import time
from cookie import cookie

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
URL = 'http://localhost:1667/'
driver.get(URL)

cookie()
