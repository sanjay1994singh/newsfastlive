# Generated by Django 5.1 on 2024-09-10 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_streaming', '0002_livestreaming_views_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestreaming',
            name='switch_button',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
