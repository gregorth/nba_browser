from django.core.management.base import BaseCommand, CommandError

from endpoints.models import Profile, Team, Player


class Command(BaseCommand):
    help = 'import example data from stats.nba.com'

    def handle(self, *args, **options):
        from nba_py import player

        ap = player.PlayerList()
        result = ap.info()

        for row in result.itertuples():
            # fetch player statistics
            pc = player.PlayerSummary(row.PERSON_ID)

            p_cstats = player.PlayerCareer(row.PERSON_ID)
            for record in p_cstats.regular_season_career_totals().itertuples():
                profile = Profile.objects.create(
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
                team, created = Team.objects.get_or_create(
                    name = row.TEAM_NAME,
                    abbreviation = row.TEAM_ABBREVIATION,
                    code = row.TEAM_CODE,
                    city = row.TEAM_CITY,
                    nba_id = row.TEAM_ID
                )

                player, created = Player.objects.get_or_create(
                    nba_id = row.PERSON_ID,
                    full_name = row.DISPLAY_FIRST_LAST,
                    first_name = row.DISPLAY_LAST_COMMA_FIRST.split(',')[1],
                    last_name = row.DISPLAY_LAST_COMMA_FIRST.split(',')[0],
                    player_code = row.PLAYER_CODE,
                    from_year = row.FROM_YEAR,
                    to_year = row.TO_YEAR,
                    roster_status = bool(row.roster_status),
                    team = team,
                    profile = profile
                )
