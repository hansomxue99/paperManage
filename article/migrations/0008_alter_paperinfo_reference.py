# Generated by Django 4.2.8 on 2024-01-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_paperinfo_reference_alter_paperinfo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperinfo',
            name='reference',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
