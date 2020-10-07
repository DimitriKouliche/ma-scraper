import settings


def get_paris_districts():
    """Retrieves a dictionary with district zip codes as keys, and IDs as value"""
    districts = {}
    session = settings.Session()
    district_rows = session.execute('SELECT id, cog from public.geo_place')
    for row in district_rows:
        # First element of tuple is ID, second is zip code
        districts[row[1]] = row[0]
    return districts
