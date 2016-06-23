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
