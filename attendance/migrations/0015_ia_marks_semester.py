# Generated by Django 4.1.7 on 2023-05-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0014_ia_marks_student_ia_one_student_ia_three_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ia_marks',
            name='semester',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
