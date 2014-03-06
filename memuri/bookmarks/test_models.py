from django.test import TestCase

from bookmarks.models import Bookmark

#class BookmarkTestCase(TestCase):
#    def setUp(self):
#        Bookmark.objects.create(name="lion", sound="roar")
#        Boomark.objects.create(name="cat", sound="meow")
#
#    def test_animals_can_speak(self):
#        """Boomarks that can speak are correctly identified"""
#        lion = Boomark.objects.get(name="lion")
#        cat = Boomark.objects.get(name="cat")
#        self.assertEqual(lion.speak(), 'The lion says "roar"')
#        self.assertEqual(cat.speak(), 'The cat says "meow"')