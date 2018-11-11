from django.test import TestCase
from django.shortcuts import reverse

from apps.store.models import Book


class StoreViewTests(TestCase):

    def setUp(self):
        self.post = Book.objects.create(
            book_title='Test book',
            authors_info='Test author',
            ISBN='111-2222222222',
            price=45,
            publish_date='2018-11-11',
        )

    def test_index_view(self):
        path = reverse('store:index')

        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/index.html")
