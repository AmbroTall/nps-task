# Generated by Django 4.0.5 on 2022-07-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nps', '0003_response_product_name_alter_response_brand_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='brand_name',
            field=models.CharField(blank=True, default='tall', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='response',
            name='product_name',
            field=models.CharField(blank=True, default='product', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='response',
            name='user',
            field=models.CharField(blank=True, default='user', max_length=500),
            preserve_default=False,
        ),
    ]
