# Generated by Django 4.0 on 2022-02-05 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
