# C4: SQLAlchemy ORM setup
# This file defines the database schema as well as initializes the SQLite database
# The table stores weather statistics for the chosen location and date
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base

# Creates a base class that allows SQLAlchemy to map Python classes to database tables
Base = declarative_base()

# Schema definition for WeatherData class, chich maps to the weather_data table
# Each row holds values for calculated metrics of a given location and date
class WeatherTable(Base):
    __tablename__ = "weather_data"

    #Primary key uniquely identifying each record
    id = Column(Integer, primary_key=True)

    # Location data
    latitude = Column(Float)
    longitude = Column(Float)

    # Date information
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)

    # Temperature metrics (in Celsius)
    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)

    # Wind speed metrics (km/h)
    avg_wind = Column(Float)
    min_wind = Column(Float)
    max_wind = Column(Float)

    # Precipitation metrics (mm)
    sum_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)

# Creates SQLite database connection
engine = create_engine("sqlite:///weather.db")

# Creates the table in the database if it does not already exist
Base.metadata.create_all(engine)