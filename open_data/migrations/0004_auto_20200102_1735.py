# Generated by Django 2.2.6 on 2020-01-02 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('open_data', '0003_favoritecompany_favoriteshow_favoritestore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteshow',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='favoriteshow',
            name='favorite_user',
        ),
        migrations.RemoveField(
            model_name='favoritestore',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='favoritestore',
            name='favorite_user',
        ),
        migrations.DeleteModel(
            name='favoritecompany',
        ),
        migrations.DeleteModel(
            name='favoriteshow',
        ),
        migrations.DeleteModel(
            name='favoritestore',
        ),
    ]