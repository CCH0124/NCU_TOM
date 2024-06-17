# Generated by Django 4.2.6 on 2024-06-17 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('targets', '0003_target_hashed_sed_target_hashed_simbad_target_sed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to=settings.AUTH_USER_MODEL),
        ),
    ]
