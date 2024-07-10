import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

##import models scaler and ridge picle file
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))


##route for home page
@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")