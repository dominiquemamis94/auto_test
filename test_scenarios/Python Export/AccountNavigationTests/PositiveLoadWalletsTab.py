# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PositiveLoadWalletsTab(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_positive_load_wallets_tab(self):
        driver = self.driver
        startTime = driver.execute_script("window.startTime = new Date().getTime(); return startTime;")
        driver.find_element_by_link_text("Account").click()
        driver.find_element_by_xpath("//div[@id='nav-tabs-account-center-section']/div[2]/a[3]/div[2]").click()
        elementFound = driver.execute_script("var element = document.evaluate(\"//div[@id='walletView']\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; window.found = element !== null;return element !== null;`")
        driver.execute_script("var userAgent = navigator.userAgent; var os = \"Unknown OS\"; var osVersion = \"Unknown version\"; if (userAgent.indexOf(\"Windows NT 10.0\") !== -1) {     os = \"Windows\";     osVersion = \"10\"; } else if (userAgent.indexOf(\"Windows NT 6.1\") !== -1) {     os = \"Windows\";     osVersion = \"7\"; } else if (userAgent.indexOf(\"Macintosh\") !== -1) {     os = \"MacOS\";     var match = userAgent.match(/Mac OS X (\\d+_\\d+_\\d+)/);     if (match) osVersion = match[1].replace(/_/g, '.'); } else if (userAgent.indexOf(\"Linux\") !== -1) {     os = \"Linux\"; } else if (userAgent.indexOf(\"Android\") !== -1) {     os = \"Android\";     var match = userAgent.match(/Android (\\d+\\.\\d+)/);     if (match) osVersion = match[1]; } else if (userAgent.indexOf(\"iPhone\") !== -1 || userAgent.indexOf(\"iPad\") !== -1) {     os = \"iOS\";     var match = userAgent.match(/OS (\\d+_\\d+)/);     if (match) osVersion = match[1].replace(/_/g, '.'); } var browser = \"Unknown\"; if (userAgent.indexOf(\"Chrome\") !== -1) {     browser = \"Chrome\"; } else if (userAgent.indexOf(\"Firefox\") !== -1) {     browser = \"Firefox\"; } else if (userAgent.indexOf(\"Safari\") !== -1) {     browser = \"Safari\"; } else if (userAgent.indexOf(\"Edge\") !== -1) {     browser = \"Edge\"; } else if (userAgent.indexOf(\"MSIE\") !== -1 || userAgent.indexOf(\"Trident\") !== -1) {     browser = \"Internet Explorer\"; } var browserVersion = userAgent.match(/(Chrome|Firefox|Safari|Edge|MSIE|Trident)\\/(\\d+\\.\\d+)/); var version = browserVersion ? browserVersion[2] : \"Unknown\"; var xhr = new XMLHttpRequest(); if(window.found){ xhr.open('GET', 'http://127.0.0.1:8080/insert_test_result?' + new URLSearchParams({     test_case: '[Positive] - Load Wallets Tab',     path: window.location.href,     test_suite: 'Account Navigation Test',     profile: 'Profile 1',     os: os,     os_version: osVersion,     browser: browser,     browser_version: version,     status: 'Passed',     error_message: '',     duration: '500' }).toString(), true); }else{   xhr.open('GET', 'http://127.0.0.1:8080/insert_test_result?' + new URLSearchParams({     test_case: '[Positive] - Load Wallets Tab',     path: window.location.href,     test_suite: 'Account Navigation Test',     profile: 'Profile 1',     os: os,     os_version: osVersion,     browser: browser,     browser_version: version,     status: 'Failed',     error_message: 'Wallet View not found',     duration: '500' }).toString(), true); } xhr.onreadystatechange = function() {     if (xhr.readyState === 4 && xhr.status === 200) {       console.log('Response:', xhr.responseText);     } else if (xhr.readyState === 4) {       console.error('Error:', xhr.statusText);     } }; xhr.send();");
    
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
