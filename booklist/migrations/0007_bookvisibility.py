# Generated by Django 4.0.2 on 2022-03-01 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0006_alter_author_slug_alter_book_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookVisibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
