# Generated by Django 3.1.3 on 2021-04-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210418_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
