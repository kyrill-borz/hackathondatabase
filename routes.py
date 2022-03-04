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
#db = scoped_session()

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html', the_title='Database Homepage')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')


if __name__ == '__main__':
    app.run(debug=True)
