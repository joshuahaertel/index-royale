# Generated by Django 3.0.5 on 2020-04-22 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_delete_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='team_name',
            new_name='team',
        ),
    ]
