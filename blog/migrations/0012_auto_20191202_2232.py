# Generated by Django 2.1.14 on 2019-12-03 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191202_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsvp',
            old_name='title',
            new_name='name',
        ),
    ]
