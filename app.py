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
    Welcome to the Climate Analysis API!<br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end<br>
    ''')

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    