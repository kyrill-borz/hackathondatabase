""" Base web app. """

__author__ = "Eve Sherratt, John Jessop, Kyrill Borzenko"

# External imports
from flask import Flask, render_template, request

# Internal imports
from basic_algorithm import load_data,create_score

app = Flask(__name__)
db = "static/data/concrete.csv"

# two decorators, same function
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
            no1=int(request.form.get('weighting 1'))
            no2=int(request.form.get('weighting 2'))
            no3=int(request.form.get('weighting 3'))
            data = load_data(db)
            data=create_score(data, money_weight=no1, eco_weight=no2, speed_weight=no3)
            datatags=data.columns.values
            myData = data.values

            return render_template('table.html', data=myData, datatags=datatags,size=len(datatags), the_title='Information')
    return render_template('index.html', the_title='Home | MCCC')

@app.route('/table', methods = ['POST', 'GET'])
def table():
        if request.method == 'POST':
            no1=request.form.get('weighting 1')
            no2=request.form.get('weighting 2')
            no3=request.form.get('weighting 3')
            data = load_data(db)
            data=create_score(data, no1, no2,no3)
            datatags=data.columns.values
            myData = data.values

            return render_template('table.html', data=myData, datatags=datatags,size=len(datatags), the_title='Information')
	# to read the csv file using the pandas library
        data = load_data(db)
        datatags=data.columns.values
        myData = data.values

        return render_template('table.html', data=myData, datatags=datatags,size=len(datatags), the_title='Information')



if __name__ == '__main__':
    app.run(debug=True)
