# Generated by Django 3.2.4 on 2021-06-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_game_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='duration',
            field=models.PositiveIntegerField(null=True),
        ),
    ]