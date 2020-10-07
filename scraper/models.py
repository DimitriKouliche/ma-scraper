from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Listing(Base):
    __tablename__ = 'listing'

    id = Column(Integer, primary_key=True)
    room_number = Column(Integer)
    area = Column(Integer)
    district = Column(Integer)
    first_scraping_date = Column(Date)
    last_seen_date = Column(Date)
    prices = relationship("PriceHistory", order_by="desc (PriceHistory.seen_date)",
                          primaryjoin="PriceHistory.listing_id==Listing.id")


class PriceHistory(Base):
    __tablename__ = 'price_history'

    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    seen_date = Column(Date)
    listing_id = Column(Integer, ForeignKey('listing.id'))
    listing = relationship(Listing, primaryjoin=listing_id == Listing.id)

