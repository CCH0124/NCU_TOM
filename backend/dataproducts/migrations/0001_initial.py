# Generated by Django 4.2.6 on 2024-10-01 07:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('targets', '0002_alter_target_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LulinDataProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('file_name', models.CharField(blank=True, max_length=100)),
                ('mjd', models.FloatField()),
                ('mag', models.FloatField()),
                ('source_ra', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)])),
                ('source_dec', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('exposure_time', models.FloatField()),
                ('zp', models.FloatField()),
                ('instrument_mag', models.FloatField()),
                ('photometric_band', models.CharField(blank=True, max_length=100)),
                ('filter', models.IntegerField(choices=[(1, 'u'), (2, 'g'), (3, 'r'), (4, 'i'), (5, 'z')], default=1, null=True, verbose_name='Filter')),
                ('instrument', models.IntegerField(choices=[(1, 'LOT'), (2, 'SLT'), (3, 'TRIPOL')], default=1, null=True, verbose_name='Instruments')),
                ('FWHM', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='targets.target')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'LulinDataProduct',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DataProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('observatory', models.IntegerField(choices=[(1, 'Lulin')])),
                ('path', models.FileField(null=True, upload_to='dataproducts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shareable', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
