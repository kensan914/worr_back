# Generated by Django 3.0.6 on 2020-05-29 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200529_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_user',
            new_name='user_id',
        ),
    ]
