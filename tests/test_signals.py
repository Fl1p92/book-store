from django.test import TestCase

from apps.store.models import Book
from apps.core.models import LogLine


class CreateLogLineTests(TestCase):

    def test_create_logline(self):
        self.assertEqual(Book.objects.count(), 0)
        self.assertEqual(LogLine.objects.count(), 0)

        self.book = Book.objects.create(
            book_title='Test book1',
            authors_info='Test author1',
            ISBN='111-1111111111',
            price=40,
        )

        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(LogLine.objects.count(), 1)
        self.assertEqual(LogLine.objects.first().logging_type, LogLine.CREATE)
        self.assertEqual(LogLine.objects.first().logging_text, f"New Book {self.book} is created!")

        self.book.book_title='Updated Test book'
        self.book.save()

        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(LogLine.objects.count(), 2)
        self.assertEqual(LogLine.objects.first().logging_type, LogLine.EDIT)
        self.assertEqual(LogLine.objects.first().logging_text, f"Book {self.book} is edited!")

        self.book.delete()

        self.assertEqual(Book.objects.count(), 0)
        self.assertEqual(LogLine.objects.count(), 3)
        self.assertEqual(LogLine.objects.first().logging_type, LogLine.DELETE)
        self.assertEqual(LogLine.objects.first().logging_text, f"Book {self.book} is deleted!")
