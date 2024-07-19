# Generated by Django 5.0.6 on 2024-07-14 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0002_alter_user_address_alter_user_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='academic_record',
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='auth.group'),
        ),
        migrations.CreateModel(
            name='AcademicRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('records', models.TextField()),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.classes')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student')),
            ],
        ),
    ]
