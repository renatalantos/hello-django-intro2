from django.test import TestCase
from .models import Item  # imported for testing CRUD operations

# Create your tests here.


class TestViews(TestCase):
    # tests if we get the right http response, use the proper templates and what our views do:
    # add, edit, toggle, delete
    

    def test_get_todo_list(self):
        response = self.client.get('/')
        # this is inbuilt in django, we use "/" for homepage
        self.assertEqual(response.status_code, 200) 
        # reponse status code is 200, which is a successful response
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        # we assume that the template used is 'todo_list.html'


    def test_get_add_item_page(self):
        response = self.client.get('/add')
        # this is inbuilt in django, we use "/" for homepage
        self.assertEqual(response.status_code, 200) 
        # reponse status code is 200, which is a successful response
        self.assertTemplateUsed(response, 'todo/add_item.html')
        # we assume that the template used is 'add_item.html'    
            

    def test_get_edit_item_page(self):
        item = Item.objects.create(name="Test Todo Item")
        # we create an item to use in this test
        response = self.client.get(f'/edit/{item.id}')
        # edit is followed by an item id
        # this is inbuilt in django, we use "/" for homepage (client.get())
        self.assertEqual(response.status_code, 200) 
        # reponse status code is 200, which is a successful response
        self.assertTemplateUsed(response, 'todo/edit_item.html')
        # we assume that the template used is 'edit_item.html'      


        # The following tests evaluate if we were able to create, toggle or delete items

    def test_can_add_item(self):  
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # To test creating an item we can set the response equal to self.client.post on the add URL
        # Give a name to the item as if we've just submitted the item form.
        self.assertRedirects(response, '/')
        # If the item is added successfully. The view should redirect back to the home page.
        # use assert redirects to confirm that it redirects back to slash.


    def test_can_delete_item(self):
        item = Item.objects.create(name="Test Todo Item")
        # we create an item to use in this test
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # view must redirect us
        existing_items = Item.objects.filter(id=item.id)
        # check if item is in fact deleted by searching for it in database by item id
        self.assertEqual(len(existing_items), 0)
        # we assume that the length of the existing items is 0 

    def test_can_toggle_item(self):
        item = Item.objects.create(name="Test Todo Item", done=True)
        # we call an item with the done status of true
        # we create an item to use in this test
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        # view must redirect us
        # after asserting that the view redirects us, we call the item again
        updated_item = Item.objects.get(id = item.id)
        self.assertFalse(updated_item.done)
        # use assert false to check it's done status.
   