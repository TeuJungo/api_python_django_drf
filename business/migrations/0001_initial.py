# Generated by Django 5.1.7 on 2025-03-16 06:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busciness',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('social_midea', models.CharField(max_length=500)),
                ('nif', models.CharField(max_length=15)),
                ('phone', models.CharField(default=True, max_length=15)),
                ('is_active', models.CharField(default=True, max_length=20)),
                ('address', models.CharField(default=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'businesses',
            },
        ),
    ]
