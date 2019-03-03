from django.db import models
from django.urls import reverse


class Organisation(models.Model):
    TYPES = (
        ('Small Business'),
        ('Large Business'),
        ('Soletrader'),
    )
    organisation_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    county = models.CharField(max_length=50, choices=TYPES)
    type = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return self.organisation_name

    def get_absolute_url(self):
        return reverse('organisation-detail', kwargs={'pk': self.pk})
