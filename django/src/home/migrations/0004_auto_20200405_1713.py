# Generated by Django 3.0.4 on 2020-04-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200405_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='like_count',
            field=models.IntegerField(blank=True),
        ),
    ]
