# Generated by Django 3.1.2 on 2020-11-09 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lang',
            field=models.CharField(choices=[('nepali', 'Nepali'), ('english', 'English')], default='english', max_length=15),
        ),
    ]
