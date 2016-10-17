from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False)
    abbreviation = models.CharField(max_length=3, null=False, blank=False)
    code = models.CharField(max_length=15, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    nba_id = models.IntegerField(unique=True)


# class Profile(models.Model):
#     # based on player:PlayerSummary(), don't have any idea what these fields mean
#     gp = models.IntegerField()
#     gs = models.IntegerField()
#     min = models.IntegerField()
#     fgm = models.CharField(max_length=10)
#     fga = models.CharField(max_length=10)
#     fg_pct = models.CharField(max_length=10)
#     fg3m = models.CharField(max_length=10)
#     ft_pct = models.CharField(max_length=10)
#     oreb = models.CharField(max_length=10)
#     dreb = models.CharField(max_length=10)
#     reb = models.CharField(max_length=10)
#     ast = models.CharField(max_length=10)
#     stl = models.CharField(max_length=10)
#     blk = models.CharField(max_length=10)
#     tov = models.CharField(max_length=10)
#     pf = models.CharField(max_length=10)
#     pts = models.CharField(max_length=10)


class Statistic(models.Model):
    #  based on player::PlayerCareer().regular_season_totals()
    season_id = models.CharField(max_length=14)
    league_id = models.CharField(max_length=2)
    team = models.ForeignKey(Team)
    age = models.FloatField()

    gp = models.IntegerField()
    gs = models.IntegerField()
    min = models.IntegerField()
    fgm = models.CharField(max_length=10)
    fga = models.CharField(max_length=10)
    fg_pct = models.CharField(max_length=10)
    fg3m = models.CharField(max_length=10)
    ft_pct = models.CharField(max_length=10)
    oreb = models.CharField(max_length=10)
    dreb = models.CharField(max_length=10)
    reb = models.CharField(max_length=10)
    ast = models.CharField(max_length=10)
    stl = models.CharField(max_length=10)
    blk = models.CharField(max_length=10)
    tov = models.CharField(max_length=10)
    pf = models.CharField(max_length=10)
    pts = models.CharField(max_length=10)


class Player(models.Model):
    nba_id = models.IntegerField(unique=True, null=False, blank=False)
    full_name = models.TextField(null=False, blank=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    player_code = models.CharField(max_length=20, null=False, blank=False)
    # profile fields
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    roster_status = models.BooleanField()
    # relation field
    team = models.ForeignKey(Team)
    statistics = models.ManyToManyField(Statistic, symmetrical=False)

