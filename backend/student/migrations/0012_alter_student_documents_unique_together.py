# Generated by Django 5.1.6 on 2025-04-11 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_check_list_documents_name_student_documents'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student_documents',
            unique_together={('STUDENT_ID', 'DOCUMENT_ID')},
        ),
    ]
