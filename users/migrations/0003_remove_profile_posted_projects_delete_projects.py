# Generated by Django 4.0.5 on 2022-06-12 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='posted_projects',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
