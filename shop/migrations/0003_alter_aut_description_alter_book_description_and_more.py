# Generated by Django 4.0.3 on 2022-03-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_pub_remove_book_capacity_aut_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aut',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pub',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tr',
            name='description',
            field=models.TextField(null=True),
        ),
    ]