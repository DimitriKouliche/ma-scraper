import os

import pytest

from scraper.parsers import HtmlParser

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


@pytest.fixture()
def listings():
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)
    with open(os.path.join(current_directory, "../samples/listings.html")) as f:
        content = f.read()
    yield content

@pytest.fixture()
def authentication():
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)
    with open(os.path.join(current_directory, "../samples/authentication.html")) as f:
        content = f.read()
    yield content


def test_extract_listings(listings):
    parser = HtmlParser(listings)
    listings = parser.extract_listings(1)
    assert listings == mock_listings


def test_extract_area():
    parser = HtmlParser("")
    area = parser.extract_area("Studio - 23 m²")
    assert area == '23'
    area = parser.extract_area("Appartement 5 pièces - 90 m²")
    assert area == '90'
    area = parser.extract_area("Appartement 6 pièces 2 SDB - 120 m²")
    assert area == '120'


def test_extract_room_number():
    parser = HtmlParser("")
    room_number = parser.extract_room_number("Studio - 23 m²")
    assert room_number == '1'
    room_number = parser.extract_room_number("Appartement 5 pièces - 90 m²")
    assert room_number == '5'
    room_number = parser.extract_room_number("Appartement 6 pièces 2 SDB - 90 m²")
    assert room_number == '6'


def test_get_csrf_token(authentication):
    parser = HtmlParser(authentication)
    csrf_token = parser.get_csrf_token()
    assert csrf_token == "5739b74b50cdcc698b414893be70b6a9511a8f7d.X32nwg.HTmsIehbPvbiRhDK71u6h0PbnpA"
