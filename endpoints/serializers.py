from rest_framework import serializers
from .models import Player, Statistic, Team


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = (
            "gp",
            "gs",
            "min",
            "fgm",
            "fga",
            "fg_pct",
            "fg3m",
            "ft_pct",
            "oreb",
            "dreb",
            "reb",
            "ast",
            "stl",
            "blk",
            "tov",
            "pf",
            "pts",
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'name',
            'abbreviation',
            'code',
            'city'
        )


class PlayerSerializer(serializers.ModelSerializer):
    #profile = StatisticSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Player
        fields = (
            'nba_id',
            'full_name',
            'first_name',
            'last_name',
            'player_code',
            'team',
            'from_year',
            'to_year',
            'roster_status',
        )