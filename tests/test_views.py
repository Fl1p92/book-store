from django.test import TestCase
from django.shortcuts import reverse
from django.template.loader import render_to_string

from apps.store.models import Book
from apps.store.forms import SortedByDateForm as sorted_form


class StoreViewTests(TestCase):

    def setUp(self):
        Book.objects.create(
            book_title='Test book1',
            authors_info='Test author1',
            ISBN='111-1111111111',
            price=41,
            publish_date='2018-11-01',
        )
        Book.objects.create(
            book_title='Test book2',
            authors_info='Test author2',
            ISBN='222-2222222222',
            price=42,
            publish_date='2018-11-02',
        )
        Book.objects.create(
            book_title='Test book3',
            authors_info='Test author3',
            ISBN='333-3333333333',
            price=43,
            publish_date='2018-11-03',
        )

    def test_index_view(self):
        response = self.client.get(reverse("store:index"))
        response_asc = self.client.get(reverse("store:index"), {"sorted_by": "ascending_date"})
        response_desc = self.client.get(reverse("store:index"), {"sorted_by": "descending_date"})
        rendered_page = render_to_string(
            "store/index.html",
            {"book_list": Book.objects.all(), "sorted_by_date_form": sorted_form}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["book_list"]), Book.objects.count())
        self.assertEqual(response_asc.context["book_list"][0], Book.objects.order_by("publish_date").first())
        self.assertEqual(response_desc.context["book_list"][0], Book.objects.order_by("-publish_date").first())
        self.assertTemplateUsed(response, "store/index.html")
        self.assertContains(response, render_to_string("footer.html"))
        self.assertEqual(response.content.decode("utf-8"), rendered_page)
