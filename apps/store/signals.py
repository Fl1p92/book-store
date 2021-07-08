from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.store.models import Book
from apps.core.models import LogLine


@receiver(post_save, sender=Book)
def create_save_log_line(sender, instance, created, **kwargs):
    if created:
        log_type = LogLine.CREATE
        log_text = f"New Book {instance} is created!"
    else:
        log_type = LogLine.EDIT
        log_text = f"Book {instance} is edited!"
    LogLine.objects.create(logging_type=log_type, logging_text=log_text)


@receiver(post_delete, sender=Book)
def create_delete_log_line(sender, instance, **kwargs):
    log_type = LogLine.DELETE
    log_text = f"Book {instance} is deleted!"
    LogLine.objects.create(logging_type=log_type, logging_text=log_text)
