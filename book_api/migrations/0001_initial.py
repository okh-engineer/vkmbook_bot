# Generated by Django 4.2.1 on 2023-06-14 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Muallif nomi')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Muallif',
                'verbose_name_plural': 'Mualliflar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FileBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_filename', models.CharField(max_length=255, verbose_name='Document Nomi')),
                ('description', models.TextField(verbose_name='Kitob nomi')),
                ('type', models.CharField(max_length=30, verbose_name='Kitob formati')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kitob yo'nalishi")),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Books_photo/%Y/%m/%d', verbose_name='Kitob Rasmi')),
                ('file_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Kitob file linki')),
                ('channel_name', models.CharField(max_length=255, verbose_name='Kanal nomi')),
                ('download_count', models.PositiveIntegerField(default=0, verbose_name='Yuklab olishlar soni')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_book_author', to='book_api.author')),
            ],
            options={
                'verbose_name': 'File Kitob',
                'verbose_name_plural': 'File Kitoblar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_filename', models.CharField(max_length=255, verbose_name='Document Nomi')),
                ('description', models.TextField(verbose_name='Kitob nomi')),
                ('type', models.CharField(max_length=30, verbose_name='Kitob formati')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kitob yo'nalishi")),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Books_photo/%Y/%m/%d', verbose_name='Kitob Rasmi')),
                ('audio_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Kitob audio linki')),
                ('channel_name', models.CharField(max_length=255, verbose_name='Kanal nomi')),
                ('download_count', models.PositiveIntegerField(default=0, verbose_name='Yuklab olishlar soni')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audio_book_author', to='book_api.author')),
            ],
            options={
                'verbose_name': 'Audio Kitob',
                'verbose_name_plural': 'Audio Kitoblar',
                'ordering': ['-created_at'],
            },
        ),
    ]
