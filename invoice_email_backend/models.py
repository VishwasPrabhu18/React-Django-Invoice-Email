from django.db import models

class InvoiceEmail(models.Model):
    name = models.CharField("Name", max_length=240)
    toEmail = models.EmailField()
    subject = models.CharField("Subject", max_length=240)

    def __str__(self):
        return self.name