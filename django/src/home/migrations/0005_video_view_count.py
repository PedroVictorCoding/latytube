# Generated by Django 3.0.4 on 2020-04-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200405_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='view_count',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
