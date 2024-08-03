# Generated by Django 5.0.6 on 2024-08-03 20:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_name', models.CharField(max_length=255)),
                ('period_type', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^term_time|holiday$')])),
                ('week_commencing_begin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='classmate.datedim')),
                ('week_commencing_end', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='classmate.datedim')),
            ],
        ),
    ]