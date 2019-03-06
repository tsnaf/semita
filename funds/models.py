from django.db import models
from django.urls import reverse


class Fund(models.Model):
    TYPES = [
        ('Strategic', 'Strategic'),
        ('Open', 'Open'),
        ('Investment', 'Investment'),
    ]
    title = models.CharField(max_length=50)
    amount = models.IntegerField()
    open_date = models.DateField(auto_now_add=False)
    close_date = models.DateField(auto_now_add=False)
    type = models.CharField(max_length=50, choices=TYPES, default='Strategic')
    notes = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fund-detail', kwargs={'pk': self.pk})
