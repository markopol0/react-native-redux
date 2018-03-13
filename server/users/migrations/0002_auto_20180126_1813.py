# Generated by Django 2.0.1 on 2018-01-27 02:13

import django.core.files.storage
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Get_Notified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/sezzati/git/frontend/media'), upload_to=users.models.User.get_uplaod_file_name),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('player', 'Player'), ('host', 'Host')], max_length=30, null=True),
        ),
    ]
