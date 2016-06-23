from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        response = home_page(request)
        expected_content = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_content)

    def test_home_page_can_remember_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'

        response = home_page(request)

        self.assertIn('A new item', response.content.decode())

        expected_content = render_to_string('home.html', {'new_item_text': 'A new item'})
        self.assertEqual(response.content.decode(), expected_content)
