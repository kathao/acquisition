# Generated by Django 2.1.14 on 2019-12-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acquisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('test1', 'test1'), ('test2', 'test2'), ('test3', 'test3'), ('test3', 'test4')], max_length=100)),
            ],
        ),
    ]
