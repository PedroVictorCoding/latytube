# Generated by Django 3.0.4 on 2020-04-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200405_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='location',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='video',
            name='longitude',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]