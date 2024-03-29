import logging

import shadow_useragent

import settings
from scraper.db_utils import DatabaseListing
from scraper.parsers import HtmlParser
from scraper.url_builder import UrlBuilder


class Scraper:
    """This class is the cornerstone of our project, it handles the the retrieval of content from the web"""

    def __init__(self, ua_spoofer):
        db_listing = DatabaseListing()
        self.paris_districts = db_listing.get_paris_districts()
        self.url_builder = UrlBuilder()
        if ua_spoofer:
            self.user_agent_spoofer = shadow_useragent.ShadowUserAgent()
        else:
            self.user_agent_spoofer = None

    @staticmethod
    def authenticate():
        web_page = settings.web_session.get(settings.CONNECT_URL)
        parser = HtmlParser(web_page.content)
        settings.web_session.post(settings.CONNECT_URL, {
            'action': 'signin',
            'user_csrf_token': parser.get_csrf_token(),
            "user_username": settings.MA_USERNAME,
            "user_password": settings.MA_PASSWORD
        })

    def retrieve_listings(self):
        listings = []
        for i in range(1, 21):
            # FIXME: Find a more robust method to retrieve zip codes
            zip_code = f"751{str(i).zfill(2)}"
            listings += self.retrieve_district_listings(self.paris_districts[zip_code])
        return listings

    def retrieve_district_listings(self, district_id):
        district_listings = []
        retrieved_results = True
        page = 1
        while retrieved_results:
            url = self.url_builder.get_district_url(page, district_id)
            logging.info(f"Requesting content from URL {url}")
            if self.user_agent_spoofer is not None:
                web_page = settings.web_session.get(url,
                                                    headers={'User-Agent': self.user_agent_spoofer.random_nomobile})
            else:
                web_page = settings.web_session.get(url)
            parser = HtmlParser(web_page.content)
            listings = parser.extract_listings(district_id)
            retrieved_results = listings != []
            district_listings += listings
            page += 1
        return district_listings
