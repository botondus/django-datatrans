"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.test import TestCase, TransactionTestCase
from django.core.management import call_command

from datatrans.models import KeyValue

from test_project.testapp.models import Option



class ObjectCreateTest(TestCase):
    '''
    This is mostly just added at this point to have 1 test
    that does "something".
    '''
    def test_multiple_obj_in_one_transaction(self):
        o1 = Option.objects.create(name="a new option")
        o1.save()
        o2 = Option.objects.create(name="another new option")
        o2.save()
        kv = KeyValue.objects.get(value="a new option")
