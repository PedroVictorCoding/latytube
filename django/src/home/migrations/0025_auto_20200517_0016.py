# Generated by Django 3.0.5 on 2020-05-17 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20200513_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='latitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='longitude',
            field=models.IntegerField(),
        ),
    ]