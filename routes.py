import os
from pandas.core.base import SelectionMixin
import pandas as pd
import requests
import uuid
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime   

app = Flask(__name__)
db = "static/data/concrete.csv"

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html', the_title='Database Homepage')

@app.route('/table')
def table():
    
 
	# to read the csv file using the pandas library 
    data = pd.read_csv(db, header=0) 
    datatags=data.columns.values
    myData = data.values
    print(datatags)
    return render_template('table.html', data=myData, datatags=datatags, the_title='Information')



if __name__ == '__main__':
    app.run(debug=True)
