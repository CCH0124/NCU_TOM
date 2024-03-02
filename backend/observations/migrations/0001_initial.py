# Generated by Django 4.2.6 on 2024-02-13 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import observations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('targets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('observatory', models.IntegerField(choices=[(1, 'Lulin')], default=1)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('priority', models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'Too')], default=3)),
                ('status', models.IntegerField(choices=[(1, 'Prep'), (2, 'Pending'), (3, 'In Progress'), (4, 'Done'), (5, 'Expired'), (6, 'Denied'), (7, 'Postponed')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('comments', models.ManyToManyField(related_name='observations', to='helpers.comments')),
                ('tags', models.ManyToManyField(related_name='observations', to='helpers.tags')),
                ('targets', models.ManyToManyField(to='targets.target')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lulin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=5)),
                ('filters', models.JSONField(default=observations.models.get_filters)),
                ('binning', models.IntegerField(default=1)),
                ('frames', models.IntegerField(default=1)),
                ('instruments', models.JSONField(default=observations.models.get_instruments)),
                ('exposure_time', models.IntegerField(default=10)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('observation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='observations.observation')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='targets.target')),
            ],
        ),
    ]
