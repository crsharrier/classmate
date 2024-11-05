# Generated by Django 5.0.6 on 2024-08-31 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmate', '0003_rename_desk_num_seatingassignment_seat_num_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seatingassignment',
            old_name='class_name',
            new_name='the_class',
        ),
        migrations.RenameField(
            model_name='seatinglayout',
            old_name='class_id',
            new_name='the_class',
        ),
        migrations.RemoveField(
            model_name='classassignment',
            name='class_name',
        ),
        migrations.AddField(
            model_name='classassignment',
            name='the_class',
            field=models.ForeignKey(db_column='class_name', default=None, on_delete=django.db.models.deletion.CASCADE, to='classmate.class'),
            preserve_default=False,
        ),
    ]
