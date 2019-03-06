from django.db import models
from django.urls import reverse
from organisations.models import Organisation


class Contact(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    updated = models.DateField(auto_now=True)
    notes = models.TextField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})
