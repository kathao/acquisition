# Generated by Django 2.1.14 on 2019-11-22 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191118_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
