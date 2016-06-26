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


class NewListViewTest(TestCase):

    def test_can_save_post_requests_to_database(self):
        self.client.post('/lists/new', data={'item_text': 'A new item'})
        item_from_db = Item.objects.all()[0]
        self.assertEqual(item_from_db.text, 'A new item')

    def test_redirects_to_list_url(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new item'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')


class ListViewTest(TestCase):

    def test_lists_page_shows_items_in_database(self):
        Item.objects.create(text='Item 1')
        Item.objects.create(text='Item 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        # Verify added text was added
        self.assertIn('Item 1', response.content.decode())
        self.assertIn('Item 2', response.content.decode())
        # Django specific way to verify that added text was added
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Item 2')

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')


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