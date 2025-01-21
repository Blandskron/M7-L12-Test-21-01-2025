from django.test import TestCase, Client
from unittest.mock import patch
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Item 1", description="Description 1", price=10.0)
        Item.objects.create(name="Item 2", description="Description 2", price=20.0)

    def test_item_creation(self):
        item = Item.objects.get(name="Item 1")
        self.assertEqual(item.description, "Description 1")
        self.assertEqual(item.price, 10.0)

class ItemViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Item.objects.create(name="Item 1", description="Description 1", price=10.0)

    def test_item_list_view_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,  200)
        self.assertContains(response, "Item 1")

    @patch('app_test.models.Item.objects.all')
    def test_item_list_view_error(self, mock_items):
        mock_items.side_effect = Exception("Database error")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 500)
        self.assertJSONEqual(response.content, {'error': 'An error occurred while fetching items.'})

class ItemDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.item = Item.objects.create(name="Item 1", description="Description 1", price=10.0)

    def test_item_detail_view_success(self):
        response = self.client.get(f'/item/{self.item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.name)

    def test_item_detail_view_not_found(self):
        response = self.client.get('/item/55/')
        self.assertEqual(response.status_code, 404)
