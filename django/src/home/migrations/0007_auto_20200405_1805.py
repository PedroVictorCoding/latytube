# Generated by Django 3.0.4 on 2020-04-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200405_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(max_length=150),
        ),
    ]
