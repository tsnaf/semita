from django.db import models
from django.urls import reverse


class Organisation(models.Model):
    ORG_TYPES = [
        ('Small Business', 'Small Business'),
        ('Large Business', 'Large Business'),
        ('Soletrader', 'Soletrader'),
    ]
    organisation_name = models.CharField(max_length=50, null=True)
    address_1 = models.CharField(max_length=50, blank=True)
    address_2 = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    county = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, choices=ORG_TYPES, default='Small Business', blank=True)
    website = models.URLField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.organisation_name

    def get_absolute_url(self):
        return reverse('organisation-detail', kwargs={'pk': self.pk})


class Fund(models.Model):
    FUND_TYPES = [
        ('Strategic', 'Strategic'),
        ('Open', 'Open'),
        ('Investment', 'Investment'),
    ]
    STATUS_TYPES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Pending', 'Pending'),
    ]
    title = models.CharField(max_length=50, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    open_date = models.DateField(auto_now_add=False, blank=True, null=True)
    close_date = models.DateField(auto_now_add=False, blank=True, null=True)
    type = models.CharField(max_length=50, choices=FUND_TYPES, default='Strategic', blank=True)
    status = models.CharField(max_length=50, choices=STATUS_TYPES, default='Pending', blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fund-detail', kwargs={'pk': self.pk})


class Grant(models.Model):
    STATUS_TYPES = [
        ('APPLIED', 'Applied'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
        ('CONTRACTED', 'Contracted'),
        ('COMPLETED', 'Completed'),
    ]
    organisation = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, blank=True, null=True, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=50, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_TYPES, default='Pending', blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse('grant-detail', kwargs={'pk': self.pk})


class Contact(models.Model):
    organisation = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})
