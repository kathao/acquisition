# Generated by Django 2.1.14 on 2019-12-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=True, max_length=100)),
                ('author', models.CharField(default=True, max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='acquisition_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]