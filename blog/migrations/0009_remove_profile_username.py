# Generated by Django 3.1.3 on 2021-04-18 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]