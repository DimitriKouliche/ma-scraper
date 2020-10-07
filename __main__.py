import settings
from scraper.core import Scraper
from scraper.db_utils import DatabaseListing
import argparse
import logging


def main():
    """Called when we launch the project"""
    parser = argparse.ArgumentParser(
        description='A scraper for a well known real estate website'
    )
    parser.add_argument("-v", "--verbose", help="Sets logging level to debug",
                        action="store_true")
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    logging.info(f"Authenticating to MA as {settings.MA_USERNAME}...")
    Scraper.authenticate()
    scraper = Scraper()
    logging.info("Retrieving listings...")
    listings = scraper.retrieve_listings()
    logging.info(f"Inserting / updating {len(listings)} listings in database...")
    db_listing = DatabaseListing()
    db_listing.create_listings(listings)


if __name__ == '__main__':
    main()
