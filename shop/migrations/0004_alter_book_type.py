# Generated by Django 4.0.3 on 2022-03-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_aut_description_alter_book_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.CharField(blank=True, choices=[('T', 'text'), ('V', 'voice')], max_length=1),
        ),
    ]
