# Generated by Django 3.0.2 on 2023-08-05 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]