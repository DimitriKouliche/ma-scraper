from alchemy_mock.mocking import UnifiedAlchemyMagicMock

from scraper.db_utils import DatabaseListing
from scraper.models import Listing
# FIXME: Find a library that handles filtering sqlalchemy mocks

mock_listings = [{'listing_id': 1969071759, 'listing_price': 1790000, 'room_number': 5, 'area': 129, 'district_id': 1},
                 {'listing_id': 1969537293, 'listing_price': 3145000, 'room_number': 6, 'area': 180, 'district_id': 1},
                 {'listing_id': 1969543938, 'listing_price': 1785000, 'room_number': 4, 'area': 130, 'district_id': 1},
                 {'listing_id': 1969635131, 'listing_price': 1785000, 'room_number': 4, 'area': 130, 'district_id': 1},
                 {'listing_id': 1969917971, 'listing_price': 1000000, 'room_number': 3, 'area': 67, 'district_id': 1},
                 {'listing_id': 1969998874, 'listing_price': 985000, 'room_number': 3, 'area': 86, 'district_id': 1},
                 {'listing_id': 1970003271, 'listing_price': 453000, 'room_number': 1, 'area': 24, 'district_id': 1},
                 {'listing_id': 1969993264, 'listing_price': 430000, 'room_number': 1, 'area': 24, 'district_id': 1},
                 {'listing_id': 1969993265, 'listing_price': 880000, 'room_number': 2, 'area': 50, 'district_id': 1},
                 {'listing_id': 1969996515, 'listing_price': 280000, 'room_number': 1, 'area': 15, 'district_id': 1},
                 {'listing_id': 1969996527, 'listing_price': 2390000, 'room_number': 4, 'area': 152, 'district_id': 1},
                 {'listing_id': 1969996529, 'listing_price': 1350000, 'room_number': 4, 'area': 87, 'district_id': 1}]

session = UnifiedAlchemyMagicMock()


def test_create_listings():
    db_listing = DatabaseListing(session)
    db_listing.create_listings(mock_listings)
    listings = session.query(Listing).filter(Listing.room_number == 5)
    assert listings is not None


def test_create_or_update_listing():
    db_listing = DatabaseListing(session)
    db_listing.create_or_update_listing(mock_listings[0])
    listings = session.query(Listing).filter(Listing.room_number == 5)
    assert listings is not None


def test_get_paris_districts():
    db_listing = DatabaseListing(session)
    districts = db_listing.get_paris_districts()
    print(districts)
    assert districts == {}

