# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCONTC002():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cONTC002(self):
    self.driver.get("http://localhost:1667/")
    self.driver.set_window_size(772, 1030)
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Sign in\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").send_keys("com1@com.com")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Abcd1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.XPATH, "//div/button").click()
  
