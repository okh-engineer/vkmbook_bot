# Generated by Django 4.2.1 on 2023-06-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='document_filename',
            field=models.CharField(max_length=255, verbose_name='Document Nomii'),
        ),
    ]