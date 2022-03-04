import os
from pandas.core.base import SelectionMixin
import pandas as pd
import requests
import uuid
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_session import Session
from simplejson import load
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime   
from basic_algorithm import load_data

app = Flask(__name__)
db = "static/data/concrete.csv"

# two decorators, same function
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
            no1=request.form.get('weighting 1')
            no2=request.form.get('weighting 2')
            no3=request.form.get('weighting 3')
            longitude=request.form.get('longitude')
            latitude=request.form.get('latitude')
            data = load_data(db)
            datatags=data.columns.values
            myData = data.values
            
            return render_template('table.html', data=myData, datatags=datatags,size=len(datatags), the_title='Information')
    return render_template('index.html', the_title='Database Homepage')

@app.route('/table', methods = ['POST', 'GET'])
def table():
    
	# to read the csv file using the pandas library 
    data = load_data(db)
    datatags=data.columns.values
    myData = data.values
    
    return render_template('table.html', data=myData, datatags=datatags,size=len(datatags), the_title='Information')



if __name__ == '__main__':
    app.run(debug=True)
