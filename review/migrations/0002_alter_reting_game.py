# Generated by Django 4.2.4 on 2023-09-01 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_shop', '0002_games_price'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reting',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retings', to='game_shop.games', verbose_name='Игра'),
        ),
    ]
