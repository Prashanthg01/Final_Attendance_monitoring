# Generated by Django 4.1.7 on 2023-05-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0013_rename_semester_attendance_semister_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IA_marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='ia_one',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='ia_three',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='ia_two',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
