from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from datetime import datetime


class Organisation(models.Model):
    ORG_TYPES = [
        ("Small Business", "Small Business"),
        ("Large Business", "Large Business"),
        ("Soletrader", "Soletrader"),
    ]
    organisation_name = models.CharField(max_length=50, null=True)
    address_1 = models.CharField(max_length=50, blank=True)
    address_2 = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    county = models.CharField(max_length=50, blank=True)
    type = models.CharField(
        max_length=50, choices=ORG_TYPES, default="Small Business", blank=True
    )
    website = models.URLField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True)
    slug = models.SlugField(default="organisation", editable=False)

    def __str__(self):
        return self.organisation_name

    def get_absolute_url(self):
        kwargs = {"slug": self.slug, "pk": self.pk}
        return reverse("organisation-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.organisation_name
        self.slug = slugify(value)
        super().save(*args, **kwargs)


class Fund(models.Model):
    FUND_TYPES = [
        ("Strategic", "Strategic"),
        ("Open", "Open"),
        ("Investment", "Investment"),
    ]
    title = models.CharField(max_length=50, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    open_date = models.DateField(auto_now_add=False, null=True)
    close_date = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(
        max_length=50, choices=FUND_TYPES, default="Strategic", blank=True
    )
    notes = models.TextField(blank=True)
    slug = models.SlugField(default="fund", editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {"slug": self.slug, "pk": self.pk}
        return reverse("fund-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def fund_status(self):
        todaysdate = datetime.now().date()
        if self.open_date <= todaysdate:
            if self.close_date >= todaysdate:
                return {"fund_status": "Open", "class_status": "alert-success"}
            elif self.close_date <= todaysdate:
                return {"fund_status": "Closed", "class_status": "alert-danger"}
        else:
            return {"fund_status": "Pending", "class_status": "alert-warning"}


class Grant(models.Model):
    STATUS_TYPES = [
        ("Applied", "Applied"),
        ("Accepted", "Accepted"),
        ("Declined", "Declined"),
        ("Contracted", "Contracted"),
        ("Completed", "Completed"),
    ]
    organisation = models.ForeignKey(
        Organisation, null=True, related_name="grantorgslist", on_delete=models.CASCADE
    )
    fund = models.ForeignKey(
        Fund, null=True, related_name="grantfundslist", on_delete=models.CASCADE
    )
    project_title = models.CharField(max_length=50, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_TYPES, default="Pending", blank=True
    )
    notes = models.TextField(blank=True)
    slug = models.SlugField(default="grant", editable=False)
    attachment = models.FileField(upload_to="grants/", blank=True, null=True)

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        kwargs = {"slug": self.slug, "pk": self.pk}
        return reverse("grant-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.project_title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    # class attachmentupload(models.Model):
    #     """ attachment """
    #     attachment = models.FileField(upload_to='grants/', blank=True, null=True)

    def class_status(self):
        if self.status == "Applied":
            return "alert-warning"
        elif self.status == "Accepted":
            return "alert-success"
        elif self.status == "Declined":
            return "alert-danger"
        elif self.status == "Contracted":
            return "alert-info"
        elif self.status == "Completed":
            return "alert-primary"


class Contact(models.Model):
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        related_name="contactorgslist",
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)
    notes = models.TextField(blank=True)
    slug = models.SlugField(default="contact", editable=False)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        kwargs = {"slug": self.slug, "pk": self.pk}
        return reverse("contact-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.first_name
        self.slug = slugify(value)
        super().save(*args, **kwargs)


class Dashboard(models.Model):
    dash = models.CharField(max_length=50, null=True)
