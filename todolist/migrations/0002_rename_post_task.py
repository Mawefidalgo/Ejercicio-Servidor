# Generated by Django 4.2.7 on 2023-11-14 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Task',
        ),
    ]
