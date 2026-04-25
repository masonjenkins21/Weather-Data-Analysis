# C4: SQLAlchemy ORM setup
# This file defines the WeatherTable model as well as initializes the SQLite database
# The table stores weather statistics for the chosen location and date
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base

# Creates a base class that allows SQLAlchemy to map Python classes to database tables
Base = declarative_base()

# Schema definition for WeatherData
# Each row holds values for calculated metrics of a given location and date
class WeatherTable(Base):
    __tablename__ = "weather_data"

    #Primary key for each record
    id = Column(Integer, primary_key=True)

    latitude = Column(Float)
    longitude = Column(Float)

    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)

    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)

    avg_wind = Column(Float)
    min_wind = Column(Float)
    max_wind = Column(Float)

    sum_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)

# Creates SQLite database connection
engine = create_engine("sqlite:///weather.db")

# Creates the table in the database
Base.metadata.create_all(engine)