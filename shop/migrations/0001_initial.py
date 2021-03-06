# Generated by Django 4.0.3 on 2022-03-12 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('published_year', models.IntegerField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('ISBN', models.IntegerField(null=True)),
                ('type', models.CharField(blank=True, choices=[('T', 'text'), ('V', 'voice')], max_length=1)),
                ('pages', models.IntegerField(null=True)),
                ('Capacity', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='images/product/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('author', models.ManyToManyField(to='shop.aut')),
            ],
            options={
                'ordering': ('create_time',),
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField(auto_now_add=True)),
                ('authority', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('failed', 'Failed'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.order'),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, to='shop.cat'),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.ManyToManyField(blank=True, to='shop.tr'),
        ),
    ]
