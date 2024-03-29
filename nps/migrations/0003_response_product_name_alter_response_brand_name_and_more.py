# Generated by Django 4.0.5 on 2022-07-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nps', '0002_remove_response_category_response_brand_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='product_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='brand_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='user',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
