# Generated by Django 3.0.7 on 2020-06-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blogpost_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
