# Generated by Django 3.2.6 on 2022-07-19 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('power_pet_pro_app', '0004_added_owner_name_to_submitbug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitbug',
            name='bug_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
