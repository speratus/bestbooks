# Generated by Django 4.0.1 on 2022-01-15 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0003_author_slug_book_slug_category_slug_genre_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]