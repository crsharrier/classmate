# Generated by Django 5.0.6 on 2024-07-14 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DateDim',
            fields=[
                ('week_commencing', models.DateField(primary_key=True, serialize=False)),
                ('week_number', models.IntegerField(blank=True, null=True)),
                ('period', models.CharField(blank=True, max_length=255, null=True)),
                ('term', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SeatingAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_num', models.IntegerField()),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.class')),
                ('week_commencing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.datedim')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seating_assignments_as_partner', to='classmate.student')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seating_assignments_as_student', to='classmate.student')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceInLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('week_commencing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.datedim')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.student')),
            ],
        ),
        migrations.CreateModel(
            name='JobAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.job')),
                ('week_commencing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.datedim')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.student')),
            ],
        ),
        migrations.CreateModel(
            name='ClassAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.class')),
                ('week_commencing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date_as_week_commencing', to='classmate.datedim')),
                ('week_until', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date_as_week_until', to='classmate.datedim')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.student')),
            ],
        ),
    ]