# Generated by Django 4.0.3 on 2022-12-04 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_perevaladded_connect'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perevaladded',
            old_name='coord_id',
            new_name='coord',
        ),
        migrations.RenameField(
            model_name='perevaladded',
            old_name='level_id',
            new_name='level',
        ),
    ]