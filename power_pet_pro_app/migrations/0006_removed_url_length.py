# Generated by Django 3.2.6 on 2022-07-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power_pet_pro_app', '0005_bug_owner_user_notunique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='actual_product',
            field=models.URLField(),
        ),
    ]
