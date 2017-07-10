from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
from lists.models import Item
# Create your tests here.

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_item = Item()
	
		text1 = 'The first (ever) list item'
		first_item.text = text1
		first_item.save()

		second_item = Item()
		text2 = 'Item the second'
		second_item.text = text2
		second_item.save()
		
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]

		self.assertEqual(first_saved_item.text, text1)
		self.assertEqual(second_saved_item.text, text2)

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()

		response = home_page(request)
		expected_html = render_to_string('home.html')

		self.assertTrue(response.content.decode(), expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		itemtext = 'A new list item'
		request.POST['item_text'] = itemtext		

		response = home_page(request)

		self.assertIn(itemtext, response.content.decode())
		expected_html = render_to_string('home.html', {'new_item_text': itemtext })
		self.assertEqual(response.content.decode(), expected_html)
