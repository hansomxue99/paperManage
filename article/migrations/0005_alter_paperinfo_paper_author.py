# Generated by Django 4.2.8 on 2024-01-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_paperinfo_column_paperinfo_paper_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperinfo',
            name='paper_author',
            field=models.CharField(max_length=50),
        ),
    ]
