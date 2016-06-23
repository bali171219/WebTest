from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        # Bali has heard about a cool new to do lists app.
        # She goes to the home page
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            "1: Buy fruit",
            [row.text for row in rows]
        )

        # There is still a text box inviting her to add another item.
        # She enters "Make fruit salad"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make fruit salad')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(
            "1: Buy fruit",
            [row.text for row in rows]
        )
        self.assertIn(
            "2: Make Fruit salad",
            [row.text for row in rows]
        )
        # Bali wonders whether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her
        self.fail('Finish the test')

        # She visits that URL - her to-do list is still there

        # Satisfied Bali closes the browser

if __name__ == '__main__':
    unittest.main()