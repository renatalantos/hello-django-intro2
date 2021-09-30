from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase): # the class inherits the TestCase
    
    
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        # we assume that form won't contain a name so no value after name key
        self.assertFalse(form.is_valid())
        # we assume that the form is not valid
        self.assertIn('name', form.errors.keys())
        # we assume that there is a name key in the form dictionary of errors
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        # we assume that error message on name field is "This field is required."
        # full stop needs to be there as this expression here must be the same as the actual error message.
        # zero index needed as form will return a list of errors in each field and this error message
        # will be the first item in this list
    

    def test_done_field_is_not_required(self):  # done field is false by default
        form = ItemForm({'name': 'Test Todo Item'})
        # form is only sending a name as it should be vaild even without the done status
        self.assertTrue(form.is_valid())
        # we assume form is valid without done status

    def  test_fields_are_explicit_in_form_metaclass(self):
        # test if form only shows name and done and nothing else
        form = ItemForm() # we instantiate an empty form
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        # check if attribute in parenthesis is equal to a list with name and done in it
        # form won't display information we don't want it to
        # items in fields cannot be reordered as they must match the list exactly
     