# Generated by Django 4.0.3 on 2022-03-25 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=200, verbose_name='Tên')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=200, verbose_name='Tên')),
                ('price', models.IntegerField(verbose_name='Đơn giá')),
                ('image', models.ImageField(blank=True, upload_to='static/images', verbose_name='Ảnh')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category', verbose_name='Nhóm sản phẩm')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('priceUnit', models.IntegerField()),
                ('total', models.IntegerField()),
                ('customerName', models.CharField(max_length=50)),
                ('customerPhone', models.CharField(max_length=20)),
                ('customerAddress', models.CharField(max_length=200)),
                ('orderDate', models.DateTimeField()),
                ('deliverDate', models.DateTimeField(null=True)),
                ('status', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.product')),
            ],
        ),
    ]
