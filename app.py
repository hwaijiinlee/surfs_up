import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#set up database: access SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

#create variable for each class
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link
session = Session(engine)

#set up Flask
app = Flask(__name__)
@app.route('/')
def welcome():
    return( 
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
    