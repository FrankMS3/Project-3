#setup dependencies
import numpy as np
import datetime as dt

import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
from config import username, password


#Database setup:
protocol = 'postgresql'

host = 'localhost'
port = 5432
database_name = 'covid_db'
rds_connection_string = f'{protocol}://postgres:{password}@{host}:{port}/{database_name}'
engine = create_engine(rds_connection_string)
conn = engine.connect()
#reflect an existing database into a new model
Base = automap_base()
#reflect the tables
Base.prepare(engine, reflect=True)

#Saving reference to the table (What are our references?)
#measurement = Base.classes.measurement

# Flask setup
app = Flask(__name__)

#Flask Routes:

#creating homepage:
@app.route("/")
def homepage():
    return render_template("index.html")

#creating /api/

@app.route ("/vic")
def vic():
    #retrieve_data = session.query().all()
    retrieve_vic = pd.read_sql_query("SELECT * FROM vic", conn)
    retrieve_nsw = pd.read_sql_query("SELECT * FROM nsw", conn)
    retrieve_tas = pd.read_sql_query("SELECT * FROM tas", conn)
    retrieve_wa = pd.read_sql_query("SELECT * FROM wa", conn)
    retrieve_qld = pd.read_sql_query("SELECT * FROM qld", conn)
    retrieve_nt = pd.read_sql_query("SELECT * FROM nt", conn)
    retrieve_sa = pd.read_sql_query("SELECT * FROM sa", conn)
    retrieve_act = pd.read_sql_query("SELECT * FROM act", conn)
    #convert list of tuples into normal list
    vic_list = list(np.ravel(retrieve_vic))
    nsw_list = list(np.ravel(retrieve_nsw))
    tas_list = list(np.ravel(retrieve_tas))
    wa_list = list(np.ravel(retrieve_wa))
    qld_list = list(np.ravel(retrieve_qld))
    nt_list = list(np.ravel(retrieve_nt))
    sa_list = list(np.ravel(retrieve_sa))
    act_list = list(np.ravel(retrieve_act))
    #convert to json
    vic_data = jsonify(vic_list)
    nsw_data = jsonify(nsw_list)
    tas_data = jsonify(tas_list)
    wa_data = jsonify(wa_list)
    qld_data = jsonify(qld_list)
    nt_data = jsonify(nt_list)
    sa_data = jsonify(sa_list)
    act_data = jsonify(act_list)
    return render_template("vic.html", Mydata=vic_data)

@app.route ("/nsw")
def nsw():
    #retrieve_data = session.query().all()
    retrieve_nsw = pd.read_sql_query("SELECT * FROM nsw", conn)
    #convert list of tuples into normal list
    nsw_list = list(np.ravel(retrieve_nsw))
    #convert to json
    nsw_data = jsonify(nsw_list)
    return render_template("nsw.html", myData=nsw_data)
    
@app.route ("/tas")
def tas():
    #retrieve_data = session.query().all()
    retrieve_tas = pd.read_sql_query("SELECT * FROM tas", conn)
    #convert list of tuples into normal list
    tas_list = list(np.ravel(retrieve_tas))
    #convert to json
    tas_data = jsonify(tas_list)
    return render_template("tas.html", myData=tas_data)

@app.route ("/wa")
def wa():
    #retrieve_data = session.query().all()
    retrieve_wa = pd.read_sql_query("SELECT * FROM wa", conn)
    #convert list of tuples into normal list
    wa_list = list(np.ravel(retrieve_wa))
    #convert to json
    wa_data = jsonify(wa_list)
    return render_template("wa.html", myData=wa_data)
@app.route ("/qld")

def qld():
    #retrieve_data = session.query().all()
    retrieve_qld = pd.read_sql_query("SELECT * FROM qld", conn)
    #convert list of tuples into normal list
    qld_list = list(np.ravel(retrieve_qld))
    #convert to json
    qld_data = jsonify(qld_list)
    return render_template("qld.html", myData=qld_data)

@app.route ("/nt")
def nt():
    #retrieve_data = session.query().all()
    retrieve_nt = pd.read_sql_query("SELECT * FROM nt", conn)
    #convert list ontf tuples into normal list
    nt_list = list(np.ravel(retrieve_nt))
    #convert to json
    nt_data = jsonify(nt_list)
    return render_template("nt.html", myData=nt_data)

@app.route ("/sa")
def sa():
    #retrieve_data = session.query().all()
    retrieve_sa = pd.read_sql_query("SELECT * FROM sa", conn)
    #convert list ontf tuples into normal list
    sa_list = list(np.ravel(retrieve_sa))
    #convert to json
    sa_data = jsonify(sa_list)
    return render_template("sa.html", myData=sa_data)

@app.route ("/act")
def act():
    #retrieve_data = session.query().all()
    retrieve_act = pd.read_sql_query("SELECT * FROM act", conn)
    #convert list ontf tuples into normal list
    act_list = list(np.ravel(retrieve_act))
    #convert to json
    act_data = jsonify(act_list)
    return render_template("act.html", myData=act_data)

if __name__ == '__main__':
    app.run (debug=True)