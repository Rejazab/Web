# Generated by Django 5.0.1 on 2024-02-09 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front_page', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Experiences',
            new_name='Experience',
        ),
        migrations.RenameModel(
            old_name='Formations',
            new_name='Formation',
        ),
    ]