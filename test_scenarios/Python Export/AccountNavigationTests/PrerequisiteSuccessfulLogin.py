# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PrerequisiteSuccessfulLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_prerequisite_successful_login(self):
        driver = self.driver
        startTime = driver.execute_script("window.startTime = new Date().getTime(); return startTime;")
        driver.get("http://localhost:8033/")
        driver.find_element_by_xpath("//div[3]/div/div/div/i").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='loginForm']"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("acc").click()
        driver.find_element_by_name("acc").clear()
        driver.find_element_by_name("acc").send_keys("CS05mem840")
        driver.find_element_by_name("pwd").click()
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("wawawawa")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        elementFound = driver.execute_script("var element = document.evaluate(\"//a[@class='logout']\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; window.found = element !== null;return element !== null;")
        driver.find_element_by_link_text("Account").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
