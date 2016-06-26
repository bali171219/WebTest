from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/blennox/PyCharmProjects/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table(self, expected_row):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            expected_row,
            [row.text for row in rows]
        )

    def test_starting_a_new_todo_list(self):
        # Bali has heard about a cool new to do lists app.
        # She goes to the home page
        self.browser.get(self.live_server_url)

        # Bali notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # She is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy fruit" into a text box
        inputbox.send_keys('Buy fruit')

        # When she hits enter, the page updates, and she now sees page lists
        # "1: Buy fruit" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_table("1: Buy fruit")

        # There is still a text box inviting her to add another item.
        # She enters "Make fruit salad"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make fruit salad')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_table("2: Make fruit salad")
        self.check_for_row_in_table("1: Buy fruit")

        # Bali sees that she has a unique url
        bali_list_url = self.browser.current_url
        self.assertRegex(bali_list_url, '/lists/.+')

        # Bali closes the browser
        self.browser.quit

        # Now Ethel (an new user), comes along and opens a fresh browser
        # # this is to simulate a new user, ensuring all sessions cookies are removed
        self.browser = webdriver.Chrome('/Users/blennox/PyCharmProjects/chromedriver')

        # Ethel visits the site and see none of the items created by Bali
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy fruit', page_text)
        self.assertNotIn('Make fruit salad', page_text)

        # Ethel starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy all purpose flower')
        inputbox.send_keys(Keys.ENTER)

        # Ethel gets a unique url for her list
        ethel_list_url = self.browser.current_url
        self.assertRegex(ethel_list_url, '/lists/.+')
        self.assertNotEqual(ethel_list_url, bali_lists_url)

        # There are still no items from Bali's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy fruit', page_text)
        self.assertNotIn('Make fruit salad', page_text)

        # Bali wonders whether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her
        self.fail('Current tests pass - Add more tests')

        # She visits that URL - her to-do list is still there

if __name__ == '__main__':
    unittest.main()