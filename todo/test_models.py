from django.test import TestCase
from .models import Item


# Test if todo items are created with the default status of False

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name = 'Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name = 'Test Todo Item') 
        self.assertEqual(str(item), 'Test Todo Item')
        # we assume that item will be returned as a string 