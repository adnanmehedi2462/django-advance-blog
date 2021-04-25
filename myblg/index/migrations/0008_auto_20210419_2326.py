# Generated by Django 3.1.6 on 2021-04-19 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20210412_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('post_comment', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.artical')),
            ],
        ),
    ]