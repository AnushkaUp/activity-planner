# Generated by Django 5.0 on 2024-01-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0003_activityplan_activityplanitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='extra',
            field=models.JSONField(blank=True, null=True, verbose_name='Extra Info'),
        ),
    ]
