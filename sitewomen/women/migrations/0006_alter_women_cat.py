# Generated by Django 5.1.5 on 2025-02-13 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0005_category_women_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='women.category'),
        ),
    ]
