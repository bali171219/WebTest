import unittest
import time
from src.WebTestSample.WebTestResources.CommonFunctions import CommonFlows
common = CommonFlows()


class TestCases(unittest.TestCase):
    def setUp(self):
        print('Setting up the test')
        self.driver = common.get_or_create_web_driver()

    def tearDown(self):
        print('Tearing down the test')
        # Close the web browser
        self.driver.quit()

    def testGoogleSearch(self):
        print('************Testing Google News************')
        common.google_search('abc stock price')

    def testGoogleNews(self):
        print('************Testing Google News************')
        common.google_search('Kilimanjaro')
        common.element('News').click()

    def testGoogleMaps(self):
        print('************Testing Google Maps************')
        common.google_search('Kilimanjaro')
        common.element('Maps').click()

    def testGoogleVideos(self):
        print('************Testing Google Videos************')
        common.google_search('Kilimanjaro hang gliding')
        common.element('Videos').click()

    def testGoogleShopping(self):
        print('************Testing Google Shopping************')
        common.google_search('High elevation hiking gear')
        common.element('Shopping').click()

    def testGoogleBooks(self):
        print('************Testing Google Books************')
        common.google_search('High elevation hiking books')
        common.element('Books').click()

    def testGoogleFlights(self):
        print('************Testing Google Flights************')
        common.google_search('BOS to Kilimanjaro')
        common.element('Flights').click()

    def testGoogleApps(self):
        print('************Testing Google Apps************')
        common.google_search('Python')
        common.element('Apps').click()

    def testGoogleImages(self):
        print('************Testing Google Images************')
        common.google_search('Python')
        common.element('Images').click()

if __name__ == '__main__':
    unittest.main()
