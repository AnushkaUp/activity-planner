# Generated by Django 5.0 on 2024-02-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0008_rename_attchmentgroup_attachmentgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='attachments'),
        ),
        migrations.AddField(
            model_name='transporttype',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='attachments'),
        ),
    ]
