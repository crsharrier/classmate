# Generated by Django 5.0.6 on 2024-08-30 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatingassignment',
            name='seating_layout',
        ),
        migrations.AddField(
            model_name='classassignment',
            name='is_current',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='seatingassignment',
            name='class_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='classmate.class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seatingassignment',
            name='week_commencing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='classmate.termperiod'),
            preserve_default=False,
        ),
    ]