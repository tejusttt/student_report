# Generated by Django 5.0.2 on 2024-03-13 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0002_subject_subjectmark'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subjectmark',
            unique_together={('student', 'subject')},
        ),
    ]
