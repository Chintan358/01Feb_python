# Generated by Django 5.0.3 on 2024-04-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_publication_book_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='img', upload_to='my_image'),
        ),
    ]