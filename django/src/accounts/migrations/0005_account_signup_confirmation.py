# Generated by Django 3.0.5 on 2020-09-29 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200604_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='signup_confirmation',
            field=models.BooleanField(default=False),
        ),
    ]