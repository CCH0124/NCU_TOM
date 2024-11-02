# Generated by Django 4.2.6 on 2024-11-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0002_alter_target_dec_alter_target_ra_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='target',
            constraint=models.UniqueConstraint(condition=models.Q(('deleted_at__isnull', True)), fields=('user', 'name'), name='unique_target_name_per_user'),
        ),
    ]