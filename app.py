from flask import Flask, request, render_template, jsonify
import requests
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

model = pickle.load(open('car_price.pkl','rb'))

@app.route('/', methods = ['GET']
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        