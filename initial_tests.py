
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://hyd.oz-tms.com/#/users-login")
        time.sleep(1)
        user = driver.find_element_by_id("mat-input-0")
        time.sleep(2)
        user.send_keys("sharon@dog-sec.com")
        user.send_keys(Keys.RETURN)
        time.sleep(1)
        password = driver.find_element_by_id("mat-input-1")
        password.send_keys("Ss102030")
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()













