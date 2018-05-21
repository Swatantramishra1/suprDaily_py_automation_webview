import unittest
import argparse
import sys
from driverutil.Browser import Browser
from pageobjects.GoogleSearchPage import GoogleSearchPage
from pageobjects.SearchResultsPage import SearchResultsPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().getbrowser(browsername)
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()

    def testExample(self):
        self.googlesearchpage = GoogleSearchPage(self.driver)
        self.googlesearchpage.searchfor("Selenium")
        self.searchresultspage = SearchResultsPage(self.driver)
        self.searchresultspage.link_selenium_present()

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


