from selenium import webdriver
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
        # She is invited to enter a to-do item

        # She types "Buy fruit" into a text box

        # When she hits enter, the page updates, and she now sees page lists
        # "1: Buy fruit" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Make fruit salad"

        # The page updates again, and now shows both items on her list

        # Bali wonders whether the site will remember her list.

        # Then she sees that the site has generated a unique URL for her

        # She visits that URL - her to-do list is still there

        # Satisfied Bali closes the browser

if __name__ == '__main__':
    unittest.main()