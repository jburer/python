# Generated by Django 3.0.8 on 2020-07-07 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200707_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authenticatorstorage',
            old_name='derived_secure_hash',
            new_name='authenticator',
        ),
    ]