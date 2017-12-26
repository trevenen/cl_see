# -*- coding: utf-8 -*-

from craigslist import CraigslistForSale
from sqlalchemy import create_engine, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

import datetime
today = datetime.date.today()

import requests

dbname = 'moto2' + str(today) + '.db'
engine = create_engine('sqlite:///' + dbname, echo=False)

Base = declarative_base()

class Listing(Base):
    """
    A table to store data on craigslist listings.
    """

    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    link = Column(String)
    name = Column(String)
    price = Column(Float)
    nearest_city = Column(String)
    location = Column(String)
    cl_id = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def city_loop():
    cities = ('odessa', 'albuquerque', 'phoenix', 'littlerock', 'denver',  'collegestation', 'batonrouge', 'sanangelo', 'wichitafalls', 'austin', 'houston', 'dallas', 'lubbock', 'saltlakecity', 'stgeorge', 'oklahomacity')
    for city in cities:
        print(city)
        cl_loop_hayabusa(city)

def cl_loop_kawasaki(city):
    cl_m = CraigslistForSale(site=city, category='mca', filters={'has_image': True, 'min_year': '2012', 'min_engine_displacement_cc': '1000', 'max_engine_displacement_cc' : '2000',
    'query': 'kawasaki ninja -harley -10r -10R -ZX10R' } )

    results = []
    # Try Block prevents cities without any return from throwing a local varible referenced before assignment error. If City has no # it will just go to next City.
    try:
        for result in cl_m.get_results(sort_by='newest', geotagged=True):
            nearest_city = city
            listing = session.query(Listing).filter_by(cl_id=result["id"]).first()
            print(result['name'], result['price'], result['url'])

            # Try parsing the price.
            price = 0
            try:
                price = float(result["price"].replace("$", ""))
            except Exception:
                pass

            # Create the listing object.
            listing = Listing(
                link=result["url"],
                name=result["name"],
                price=price,
                location=result["where"],
                cl_id=result["id"],
                nearest_city=city


            )
            session.add(listing)

        session.commit()
        results.append(result)
        return
    except Exception:
        pass




city_loop()