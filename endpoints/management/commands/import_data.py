from django.core.management.base import BaseCommand, CommandError

from endpoints.models import Statistic, Team, Player


class Command(BaseCommand):
    help = 'import example data from stats.nba.com'

    def handle(self, *args, **options):
        from nba_py import player as PLAYER_API

        ap = PLAYER_API.PlayerList()
        result = ap.info()

        for row in result.itertuples():
            # fetch player statistics
            team, created = Team.objects.get_or_create(
                name = row.TEAM_NAME,
                abbreviation = row.TEAM_ABBREVIATION,
                code = row.TEAM_CODE,
                city = row.TEAM_CITY,
                nba_id = row.TEAM_ID
            )
            if Player.objects.filter(nba_id=row.PERSON_ID).exists():
                player = Player.objects.get(nba_id=row.PERSON_ID)
            else:
                player = Player(nba_id = row.PERSON_ID)

            player.__dict__.update({
                "nba_id": row.PERSON_ID,
                "full_name": row.DISPLAY_FIRST_LAST,
                "first_name": row.DISPLAY_LAST_COMMA_FIRST.split(',')[-1],
                "last_name": row.DISPLAY_LAST_COMMA_FIRST.split(',')[0],
                "player_code": row.PLAYERCODE,
                "from_year": row.FROM_YEAR,
                "to_year": row.TO_YEAR,
                "roster_status": bool(row.ROSTERSTATUS),
                "team": team,
            })
        print ("filling players statistics")
        for p_id in Player.objects.all().values_list('nba_id', flat=True):
            p_cstats = PLAYER_API.PlayerCareer(p_id)
            for record in p_cstats.regular_season_totals().itertuples():
                if not Team.objects.filter(pk=record.TEAM_ID).exists():
                    continue
                statistic, created = Statistic.objects.get_or_create(
                    season_id = record.SEASON_ID,
                    league_id = record.LEAGUE_ID,
                    team = Team.objects.get(pk=record.TEAM_ID),
                    age = record.PLAYER_AGE,

                    gp = record.GP,
                    gs = record.GS,
                    min = record.MIN,
                    fgm = record.FDM,
                    fga = record.FGA,
                    fg_pct = record.FG_PCT,
                    fg3m = record.FG3M,
                    ft_pct= record.FT_PCT,
                    oreb  = record.OREB,
                    dreb = record.DREB,
                    reb = record.REB,
                    ast = record.AST,
                    stl = record.STL,
                    blk = record.BLK,
                    tov = record.TOV,
                    pf = record.PF,
                    pts = record.PTS
                )
                if created:
                    player = Player.objects.get(nba_id=p_id)
                    player.statistics.add(statistic)
