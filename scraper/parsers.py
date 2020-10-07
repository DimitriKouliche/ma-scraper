import logging
import re

from bs4 import BeautifulSoup


class HtmlParser:
    """This class handles parsing HTML content for our project"""

    def __init__(self, content):
        self.soup = BeautifulSoup(content, 'html.parser')

    def extract_listings(self, district_id):
        listings = []
        listing_divs = self.soup.findAll("div", {"class": "listing-item"})
        for listing_div in listing_divs:
            listing_metadata = listing_div['data-wa-data'].split('|')
            try:
                price_text = listing_div.find("div", {"class": "listing-price"}).text
            except AttributeError as e:
                logging.error(f"Cannot find price for listing with ID {int(listing_metadata[0].replace('listing_id=', ''))}")
                price_text = "0 €"
            characteristics_text = listing_div.find("div", {"class": "listing-characteristic"}).text
            listings.append({
                'listing_id': int(listing_metadata[0].replace('listing_id=', '')),
                'listing_price': int(re.sub('[^0-9,.]', '', price_text)),
                'room_number': int(self.extract_room_number(characteristics_text.strip())),
                'area': int(self.extract_area(characteristics_text.strip())),
                'district_id': int(district_id)
            })
        return listings

    def extract_area(self, characteristics_text):
        try:
            return re.findall(r'\d+', characteristics_text)[-1]
        except IndexError as e:
            logging.error(f"Cannot extract area from value {characteristics_text}")
            return '0'

    def extract_room_number(self, characteristics_text):
        if characteristics_text.split(' ', 1)[0] == "Studio":
            return '1'
        try:
            return re.search(r'\d+', characteristics_text).group()
        except AttributeError as e:
            logging.error(f"Cannot extract room number from value {characteristics_text}")
            return '0'

    def get_csrf_token(self):
        csrf_input = self.soup.find("input", {"id": "user_csrf_token"})
        try:
            return csrf_input.get('value')
        except AttributeError as e:
            logging.error(f"Cannot extract CSRF token")
            return ""

    def print_page_content(self):
        print(self.soup.prettify())
