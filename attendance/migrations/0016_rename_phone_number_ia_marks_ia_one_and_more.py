# Generated by Django 4.1.7 on 2023-05-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0015_ia_marks_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ia_marks',
            old_name='phone_number',
            new_name='ia_one',
        ),
        migrations.AddField(
            model_name='ia_marks',
            name='ia_three',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ia_marks',
            name='ia_two',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]