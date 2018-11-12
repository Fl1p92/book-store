from django.db import models


class LogLine(models.Model):

    CREATE = "create"
    EDIT = "edit"
    DELETE = "delete"

    LOGGING_TYPES = (
        (CREATE, "Create"),
        (EDIT, "Edit"),
        (DELETE, "Delete"),
    )

    logging_time = models.DateTimeField("Logging time", auto_now_add=True)
    logging_type = models.CharField("Product color", max_length=6, choices=LOGGING_TYPES, db_index=True)
    logging_text = models.TextField("Logging text")

    def __str__(self):
        return f"{self.logging_time.strftime('%d.%m.%y %H:%M:%S %Z')} -- [{self.get_logging_type_display()}] -- {self.logging_text}"

    class Meta:
        verbose_name = "Log line"
        verbose_name_plural = "Log lines"
