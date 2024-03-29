# Generated by Django 5.0 on 2023-12-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('public_user', 'User'), ('vendor', 'Vendor'), ('admin', 'Admin')], max_length=255, null=True),
        ),
    ]
