# ORM - Object Relatioan Mapping

# 1. raw sql - sql scripteket futtatunk
# 2. expression language - objektumokat használ az adatbázis kommunikációra
#   szinten teljesen elfedi a raw sql használatát


from sqlalchemy import Column, create_engine, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

db = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)

base = declarative_base()

# tábla model: adatbázis táblájának a python reprezentációja
# ORM webfejlesztéshez jó
class Movie(base):
    __tablename__ = 'movies'

    title = Column(String, primary_key=True)
    director = Column(String)
    release_date = Column(Date)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

alien = Movie(title='Alien', director="Ridley Scott", release_date=datetime.datetime(1979, 1, 1))
session.add(alien)
session.commit()

movies = session.query(Movie)

for movie in movies:
    print(movie.title)

alien.director = "Ricsi"
alien.title = 'Ricsi'
session.commit()

session.delete(alien)
session.commit()
