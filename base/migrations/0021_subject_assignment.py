# Generated by Django 5.0.6 on 2024-08-06 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_attendence_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('assigned_date', models.DateField()),
                ('submission_date', models.DateField()),
                ('class_assigned', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.classes')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.teacher')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.subject')),
            ],
        ),
    ]