# Generated by Django 5.1.4 on 2025-01-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=0, max_length=13, unique=True),
            preserve_default=False,
        ),
    ]