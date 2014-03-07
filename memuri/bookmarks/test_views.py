from django.test.client import Client
from django.test import TestCase


#class HomeTest(TestCase):
#    fixtures = ["testdata.json"]
#
#    def test_has_bookmark(self):
#        c = Client()
#
#        response = c.get('/bookmarks/')
#        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, "Bookmarks")
#
#    def test_has_minktoast(self):
#        c = Client()
#
#        response = c.get('/bookmarks/')
#        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, "Minktoast")