# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nba_id', models.IntegerField(unique=True)),
                ('full_name', models.TextField()),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('player_code', models.CharField(max_length=20)),
                ('from_year', models.IntegerField()),
                ('to_year', models.IntegerField()),
                ('roster_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_id', models.CharField(max_length=14)),
                ('league_id', models.CharField(max_length=2)),
                ('age', models.FloatField()),
                ('gp', models.IntegerField()),
                ('gs', models.IntegerField()),
                ('min', models.IntegerField()),
                ('fgm', models.CharField(max_length=10)),
                ('fga', models.CharField(max_length=10)),
                ('fg_pct', models.CharField(max_length=10)),
                ('fg3m', models.CharField(max_length=10)),
                ('ft_pct', models.CharField(max_length=10)),
                ('oreb', models.CharField(max_length=10)),
                ('dreb', models.CharField(max_length=10)),
                ('reb', models.CharField(max_length=10)),
                ('ast', models.CharField(max_length=10)),
                ('stl', models.CharField(max_length=10)),
                ('blk', models.CharField(max_length=10)),
                ('tov', models.CharField(max_length=10)),
                ('pf', models.CharField(max_length=10)),
                ('pts', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('abbreviation', models.CharField(max_length=3)),
                ('code', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=30)),
                ('nba_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='statistic',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='statistics',
            field=models.ManyToManyField(to='endpoints.Statistic'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.Team'),
        ),
    ]
