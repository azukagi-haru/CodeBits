# Generated by Django 4.2.1 on 2023-05-25 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='content',
            new_name='description',
        ),
    ]
