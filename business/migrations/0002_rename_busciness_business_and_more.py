# Generated by Django 5.1.7 on 2025-03-16 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Busciness',
            new_name='Business',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='social_midea',
            new_name='social_name',
        ),
    ]
