# Generated by Django 4.2.7 on 2023-11-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_alter_product_options_product_created_at_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={},
        ),
        migrations.AddField(
            model_name="product",
            name="thumbnail",
            field=models.ImageField(default=1, upload_to="thumbnail/"),
        ),
    ]