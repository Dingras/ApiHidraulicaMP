# Generated by Django 5.1 on 2025-01-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_category_name_alter_category_url_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url_img',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
