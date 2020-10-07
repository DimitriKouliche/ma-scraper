from scraper.url_builder import UrlBuilder


def test_extract_listings():
    url_builder = UrlBuilder()
    assert url_builder.get_district_url(5, 1) == "https://www.meilleursagents.com/annonces/achat/search/" \
                                                 "?place_ids=1&transaction_types=TRANSACTION_TYPE.SELL&" \
                                                 "item_types=ITEM_TYPE.APARTMENT&page=5"

