# Generated by Django 3.0.4 on 2020-04-07 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200406_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='thumbnail',
        ),
    ]
