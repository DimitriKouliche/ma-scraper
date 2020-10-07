from scraper.core import Scraper


def main():
    """Called when we launch the project"""
    scraper = Scraper()
    scraper.authenticate()
    scraper.retrieve_listings()


if __name__ == '__main__':
    main()
