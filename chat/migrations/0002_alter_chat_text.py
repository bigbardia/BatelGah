# Generated by Django 4.0 on 2022-02-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
