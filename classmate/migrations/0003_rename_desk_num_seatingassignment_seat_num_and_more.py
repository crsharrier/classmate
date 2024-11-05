# Generated by Django 5.0.6 on 2024-08-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmate', '0002_remove_seatingassignment_seating_layout_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seatingassignment',
            old_name='desk_num',
            new_name='seat_num',
        ),
        migrations.AddField(
            model_name='seatingassignment',
            name='desk_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
