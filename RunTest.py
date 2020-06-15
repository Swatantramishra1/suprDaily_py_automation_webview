import unittest
import argparse
import sys

from driverutil.Browser import Browser
from pages.loginPage import LoginPage


class RunTest(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().getbrowser(browsername)
        self.driver.get("http://localhost:3000")
        self.loginPage = LoginPage(self.driver)

    def testExample(self):
        self.loginPage.suprLogin()
        self.loginPage.suprLogout()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    browser = argparse.ArgumentParser()
    browser.add_argument("-b", "--browser", required=False,
                         help="name of the browser", default="chrome")
    browser.add_argument('unittest_args', nargs='*')
    args = browser.parse_args()
    sys.argv[1:] = args.unittest_args
    browsername = vars(args)["browser"]
    unittest.main()
