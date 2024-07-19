# Generated by Django 5.0.6 on 2024-07-16 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_student_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='classes',
        ),
        migrations.AddField(
            model_name='teacher',
            name='classes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.classes'),
        ),
    ]