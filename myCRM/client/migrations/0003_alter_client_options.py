# Generated by Django 5.2.4 on 2025-07-13 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
    ]
