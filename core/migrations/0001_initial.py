# Generated by Django 2.1.7 on 2019-03-10 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50, null=True)),
                ("last_name", models.CharField(blank=True, max_length=50)),
                ("job_title", models.CharField(blank=True, max_length=50)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(blank=True, max_length=50)),
                ("updated", models.DateField(auto_now=True, null=True)),
                ("notes", models.TextField(blank=True)),
                ("slug", models.SlugField(default="contact", editable=False)),
            ],
        ),
        migrations.CreateModel(
            name="Fund",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, null=True)),
                ("amount", models.PositiveIntegerField(blank=True, null=True)),
                ("open_date", models.DateField(blank=True, null=True)),
                ("close_date", models.DateField(blank=True, null=True)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Strategic", "Strategic"),
                            ("Open", "Open"),
                            ("Investment", "Investment"),
                        ],
                        default="Strategic",
                        max_length=50,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Open", "Open"),
                            ("Closed", "Closed"),
                            ("Pending", "Pending"),
                        ],
                        default="Pending",
                        max_length=50,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                ("slug", models.SlugField(default="fund", editable=False)),
            ],
        ),
        migrations.CreateModel(
            name="Grant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_title", models.CharField(max_length=50, null=True)),
                ("amount", models.PositiveIntegerField(blank=True, null=True)),
                ("date", models.DateField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Applied", "Applied"),
                            ("Accepted", "Accepted"),
                            ("Declined", "Declined"),
                            ("Contracted", "Contracted"),
                            ("Completed", "Completed"),
                        ],
                        default="Pending",
                        max_length=50,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                ("slug", models.SlugField(default="grant", editable=False)),
                (
                    "fund",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Fund",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("organisation_name", models.CharField(max_length=50, null=True)),
                ("address_1", models.CharField(blank=True, max_length=50)),
                ("address_2", models.CharField(blank=True, max_length=50)),
                ("postcode", models.CharField(blank=True, max_length=10)),
                ("county", models.CharField(blank=True, max_length=50)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Small Business", "Small Business"),
                            ("Large Business", "Large Business"),
                            ("Soletrader", "Soletrader"),
                        ],
                        default="Small Business",
                        max_length=50,
                    ),
                ),
                ("website", models.URLField(blank=True, max_length=50, null=True)),
                ("notes", models.TextField(blank=True)),
                ("slug", models.SlugField(default="organisation", editable=False)),
            ],
        ),
        migrations.AddField(
            model_name="grant",
            name="organisation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.Organisation",
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="organisation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.Organisation",
            ),
        ),
    ]
