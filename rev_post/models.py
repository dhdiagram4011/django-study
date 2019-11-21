from django.db import models
from django.utils import timezone
from django import forms

class rev_post(models.Model):
    id = models.CharField(max_lenght=100)
    email = models.EmailField(max_lenght=300)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email

