# Generated by Django 3.0.5 on 2020-04-22 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200422_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team_name',
            field=models.CharField(default='', max_length=63),
            preserve_default=False,
        ),
    ]
