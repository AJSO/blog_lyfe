# Generated by Django 3.0.7 on 2020-06-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='day',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='month',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
    ]
