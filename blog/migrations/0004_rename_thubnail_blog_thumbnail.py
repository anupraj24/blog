# Generated by Django 3.2.9 on 2021-12-06 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211206_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='thubnail',
            new_name='thumbnail',
        ),
    ]