# Generated by Django 2.1.7 on 2019-03-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190312_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='grants/'),
        ),
    ]