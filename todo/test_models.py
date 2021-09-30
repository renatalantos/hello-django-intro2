from django.test import TestCase
from .models import Item


# Test if todo items are created with the default status of False

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name = 'Test Todo Item')
        self.assertFalse(item.done)