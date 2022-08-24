# Generated by Django 3.2.6 on 2022-07-15 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('power_pet_pro_app', '0003_submit_bug'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitbug',
            name='bug_owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='submitbug',
            name='bug_owner_name',
            field=models.CharField(default='justin', max_length=100),
            preserve_default=False,
        ),
    ]