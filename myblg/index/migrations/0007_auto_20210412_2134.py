# Generated by Django 3.1.6 on 2021-04-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20210412_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='github',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='author',
            name='stack_overflow',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
