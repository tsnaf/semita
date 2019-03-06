from django.db import models
from django.urls import reverse


class Organisation(models.Model):
    TYPES = [
        ('SMALL_BUSINESS', 'Small Business'),
        ('LARGE_BUSINESS', 'Large Business'),
        ('SOLETRADER', 'Soletrader'),
    ]
    organisation_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    county = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPES, default='SMALL_BUSINESS')
    website = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return self.organisation_name

    def get_absolute_url(self):
        return reverse('organisation-detail', kwargs={'pk': self.pk})


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
