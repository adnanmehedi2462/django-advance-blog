# Generated by Django 3.1.6 on 2021-04-24 14:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20210424_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
