from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        response = home_page(request)
        expected_content = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_content)

    def test_home_page_shows_items_in_database(self):
        Item.objects.create(text='Item 1')
        Item.objects.create(text='Item 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('Item 1', response.content.decode())
        self.assertIn('Item 2', response.content.decode())

    def test_home_page_can_save_post_requests_to_database(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'

        response = home_page(request)

        item_from_db = Item.objects.all()[0]
        self.assertEqual(item_from_db.text, 'A new item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/')

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items_to_the_database(self):
        first_item = Item()
        first_item.text = 'Item the first'
        first_item.save()

        second_item = Item()
        second_item.text = 'second item'
        second_item.save()

        first_item_from_db = Item.objects.all()[0]
        self.assertEqual(first_item_from_db.text, 'Item the first')

        second_item_from_db = Item.objects.all()[1]
        self.assertEqual(second_item_from_db.text, 'second item')