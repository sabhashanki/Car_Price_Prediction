from inspect import FullArgSpec
from flask import Flask, request, render_template, jsonify
import requests
import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open('car_price.pkl','rb'))

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
 
    Car_Age = 2022 - int(request.form['Year'])
    Present_Price = float(request.form['Present_Price'])
    Kms_Driven = int(request.form['Kms_Driven'])
    Owner = int(request.form['Owner'])
                
    Fuel_Type = request.form['Fuel_Type']

    if Fuel_Type == 'Petrol':
        Diesel = 0
        Petrol = 1
    elif Fuel_Type == 'Diesel':
        Diesel = 1
        Petrol = 0
    else: 
        Diesel = 0
        Petrol = 0

    Seller_Type = request.form['Seller_Type']

    if Seller_Type == 'Individual':
        dividual = 1
    else:
        Individual = 0

    Transmission = request.form['Transmission']

    if Transmission == 'Manual':
        Manual = 1
    else:
        Manual = 0

    Car_Name = request.form['Car_Name']
    amaze = brio = ciaz = city = corolla_altis = fortuner = grand_i10 = i10 = i20 = innova = jazz = swift = sx4 = verna = 0
    names = ['amaze', 'brio', 'ciaz', 'city', 'corolla_altis', 'fortuner', 'grand_i10', 'i10', 'i20', 'innova', 'jazz', 'swift', 'sx4', 'verna' ]
    
    for name in names:
        if Car_Name == name:
            name = 1
    
    prediction = model.predict([[Present_Price, Kms_Driven, Owner, amaze, brio, ciaz, city, corolla_altis, fortuner, grand_i10, i10, i20, innova, jazz, swift, sx4, verna, Diesel, Petrol, Manual, Individual, Car_Age]])
    output = prediction[0]
    
    return render_template('home.html', prediction_text = 'Well You can sell the car for {}'.format(output))

if __name__ == '__main__':
    app.run(debug = True)
