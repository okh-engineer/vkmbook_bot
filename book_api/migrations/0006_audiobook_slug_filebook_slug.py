# Generated by Django 4.2.1 on 2023-06-19 05:27

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0005_alter_filebook_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='document_filename', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filebook',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='document_filename', unique=True),
            preserve_default=False,
        ),
    ]
