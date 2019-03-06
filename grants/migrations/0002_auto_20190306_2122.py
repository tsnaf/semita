# Generated by Django 2.1.7 on 2019-03-06 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0002_auto_20190306_2059'),
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='fund',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='funds.Fund'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.Organisation'),
        ),
    ]
