# Generated by Django 5.0 on 2024-01-31 17:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0007_attchmentgroup_attachment_group_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AttchmentGroup',
            new_name='AttachmentGroup',
        ),
    ]
