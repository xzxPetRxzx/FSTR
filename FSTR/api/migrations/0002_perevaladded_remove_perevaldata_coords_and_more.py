# Generated by Django 4.0.3 on 2022-12-03 08:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('beauty_title', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=50)),
                ('other_titles', models.CharField(max_length=50)),
                ('connect', models.CharField(max_length=50)),
                ('add_time', models.DateTimeField(blank=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=8)),
                ('coord_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.level')),
            ],
        ),
        migrations.RemoveField(
            model_name='perevaldata',
            name='coords',
        ),
        migrations.RemoveField(
            model_name='perevaldata',
            name='level',
        ),
        migrations.RemoveField(
            model_name='perevaldata',
            name='user',
        ),
        migrations.RemoveField(
            model_name='perevalimages',
            name='pereval_data',
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='perevalimages',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.EmailValidator]),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=16),
        ),
        migrations.DeleteModel(
            name='Pereval',
        ),
        migrations.DeleteModel(
            name='PerevalData',
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
        migrations.AddField(
            model_name='perevalimages',
            name='pereval_added',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.perevaladded'),
            preserve_default=False,
        ),
    ]
