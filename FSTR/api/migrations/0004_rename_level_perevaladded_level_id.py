# Generated by Django 4.0.3 on 2022-12-03 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_perevalareas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perevaladded',
            old_name='level',
            new_name='level_id',
        ),
    ]
