# Generated by Django 2.2 on 2019-12-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_book_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.AddField(
            model_name='book',
            name='liked_users',
            field=models.ManyToManyField(default=None, related_name='liked_books', to='favorite_book_app.User'),
        ),
    ]