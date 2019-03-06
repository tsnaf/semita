from django.db import models
from django.urls import reverse
from organisations.models import Organisation
from funds.models import Fund


class Grant(models.Model):
    TYPES = [
        ('APPLIED', 'Applied'),
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
        ('CONTRACTED', 'Contracted'),
        ('COMPLETED', 'Completed'),
    ]
    organisation = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, blank=True, null=True, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=TYPES, default='Pending')
    notes = models.TextField()

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse('grant-detail', kwargs={'pk': self.pk})
