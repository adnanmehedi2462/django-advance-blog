# Generated by Django 3.1.6 on 2021-04-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_author_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='facebook',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='instagram',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='linkedin',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.TextField(blank=True),
        ),
    ]