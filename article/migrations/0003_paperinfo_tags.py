# Generated by Django 4.2.8 on 2024-01-08 05:06

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('article', '0002_papercolumn_paperinfo_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperinfo',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]