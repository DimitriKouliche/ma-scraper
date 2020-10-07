import settings
import urllib.parse as urlparse
from urllib.parse import urlencode


class UrlBuilder:
    """Handles building URLs to retrieve content"""

    def get_district_url(self, page, district_id, transaction_type="TRANSACTION_TYPE.SELL",
                         item_type="ITEM_TYPE.APARTMENT"):
        params = {
            'place_ids': district_id,
            'transaction_types': transaction_type,
            'item_types': item_type,
            'page': page
        }
        url_parts = list(urlparse.urlparse(settings.BASE_SCRAPING_URL))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)
        return urlparse.urlunparse(url_parts)
