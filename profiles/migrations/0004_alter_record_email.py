# Generated by Django 4.0.3 on 2022-03-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_record_delete_record_of_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
