# Generated by Django 2.2 on 2020-11-23 08:32

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.custom_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('categories', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=164)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_keywords', models.CharField(blank=True, help_text='Separate keywords with commas.', max_length=255, null=True, verbose_name='Keywords')),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('meta_author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Author')),
                ('meta_copyright', models.CharField(blank=True, max_length=255, null=True, verbose_name='Copyright')),
                ('title', models.CharField(max_length=132, verbose_name='نام محصول')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='قیمت محصول')),
                ('second_price', models.FloatField(blank=True, null=True, verbose_name='بازه دوم قیمت')),
                ('discount_price', models.FloatField(blank=True, null=True, verbose_name='قیمت تخفیف')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_alt', models.CharField(blank=True, max_length=225, null=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('stock', models.IntegerField(default=1, verbose_name='موجودی')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات محصول')),
                ('minimum_order', models.CharField(blank=True, max_length=32, null=True, verbose_name='حداقل تعداد جهت سفارش')),
                ('payment_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='روش پرداخت')),
                ('packing', models.CharField(blank=True, max_length=32, null=True, verbose_name='بسته بندی')),
                ('shipping', models.CharField(blank=True, max_length=32, null=True, verbose_name='نحوه ارسال')),
                ('origin', models.CharField(blank=True, max_length=32, null=True, verbose_name='اصالت کالا')),
                ('made_in', models.CharField(blank=True, max_length=32, null=True, verbose_name='تولید کشور')),
                ('delivery', models.CharField(blank=True, max_length=32, null=True, verbose_name='بازه زمانی ارسال')),
                ('samples', models.CharField(blank=True, choices=[('خیر', '0'), ('رایگان', '1'), ('اعمال هزینه', '2 ')], max_length=24, null=True, verbose_name='ارائه نمونه')),
                ('remarks', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='ملاحظات')),
                ('date_addded', models.DateTimeField(auto_now_add=True, null=True)),
                ('orderd_times', models.IntegerField(default=1, null=True)),
                ('short_discription', models.TextField(verbose_name='توضیحات')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='categories.Category')),
                ('label_try', models.ManyToManyField(blank=True, to='products.Label')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ProducerProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'unique_together': {('product', 'name')},
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_alt', models.CharField(blank=True, max_length=225, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(limit_choices_to={'model': 'product'}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=50, null=True)),
                ('attachment', models.ImageField(blank=True, null=True, upload_to='')),
                ('selectable', models.BooleanField(blank=True, default=False, null=True)),
                ('yes_or_no', models.BooleanField(blank=True, default=False, null=True)),
                ('products', models.ManyToManyField(to='products.Product')),
                ('variation', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.Variation')),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('content', models.TextField(verbose_name='متن نظر')),
                ('username', models.CharField(blank=True, max_length=132, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='MetaDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('fake_content', models.CharField(max_length=1234)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', products.custom_fields.IntegerRangeField(verbose_name='امتیاز')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(limit_choices_to={'model': 'product'}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'object_id')},
                'index_together': {('user', 'object_id')},
            },
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('attachment', models.ImageField(blank=True, upload_to='')),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Variation')),
            ],
            options={
                'unique_together': {('variation', 'value')},
            },
        ),
    ]
