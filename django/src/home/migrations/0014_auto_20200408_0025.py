# Generated by Django 3.0.4 on 2020-04-08 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200408_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(max_length=150),
        ),
    ]
