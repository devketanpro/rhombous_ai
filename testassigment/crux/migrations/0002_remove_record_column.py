# Generated by Django 4.2.6 on 2024-03-20 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crux', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='column',
        ),
    ]