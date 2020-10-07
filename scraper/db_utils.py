import logging
from datetime import date

import settings
from scraper.models import Listing, PriceHistory


class DatabaseListing:

    def __init__(self, session=None):
        if session is None:
            self.session = settings.Session()
        else:
            self.session = session

    def get_paris_districts(self):
        """Retrieves a dictionary with district zip codes as keys, and IDs as value"""
        districts = {}
        district_rows = self.session.execute('SELECT id, cog from public.geo_place')
        for row in district_rows:
            # First element of tuple is ID, second is zip code
            districts[row[1]] = row[0]
        return districts

    def create_listings(self, listings):
        for listing in listings:
            self.create_or_update_listing(listing)

    def create_or_update_listing(self, listing):
        today = date.today()
        listing_object = self.session.query(Listing).get(listing['listing_id'])
        if listing_object is None:
            logging.debug(f"Importing new listing with ID {listing['listing_id']}")
            listing_object = Listing(id=listing['listing_id'], first_scraping_date=today)
            self.session.add(listing_object)
            self.session.commit()
        else:
            logging.debug(f"Listing with ID {listing['listing_id']} is already in database, updating data")
        listing_object.room_number = listing['room_number']
        listing_object.area = listing['area']
        listing_object.district = listing['district_id']
        listing_object.last_seen_date = today
        if self.session.query(PriceHistory) \
                .filter(PriceHistory.price == listing['listing_price']) \
                .filter(PriceHistory.seen_date == today) \
                .filter(PriceHistory.listing_id == listing['listing_id']).count() == 0:
            logging.debug(f"Creating new price history for listing {listing['listing_id']}")
            self.session.add(
                PriceHistory(price=listing['listing_price'], seen_date=today, listing_id=listing['listing_id']))
        self.session.commit()
