# Generated by Django 4.1.7 on 2023-03-02 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Testing 321')]},
        ),
    ]
