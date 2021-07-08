from datetime import date

from django.db import models


class Book(models.Model):
    book_title = models.CharField("Book title", max_length=100)
    authors_info = models.CharField("Authors info", max_length=200)
    ISBN = models.CharField("ISBN", max_length=17)
    price = models.PositiveIntegerField("Price")
    publish_date = models.DateField('Publish date', default=date.today)

    def __str__(self):
        return f'"{self.book_title}" [ISBN: {self.ISBN}]'

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
