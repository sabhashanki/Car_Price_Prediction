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
        Individual = 1
    else:
        Individual = 0

    Transmission = request.form['Transmission']

    if Transmission == 'Manual':
        Manual = 1
    else:
        Manual = 0

    Car_Name = request.form['Car_Name']
    dzire = i10 = swift = seltos = polo = octavia = 0
    names = ['dzire', 'i10', 'swift', 'seltos', 'polo', 'octavia']
    
    for name in names:
        if Car_Name == name:
            name = 1
    input = np.array([Present_Price, Kms_Driven, Owner, seltos, polo, octavia, dzire, i10, swift, Diesel, Petrol, Manual, Individual, Car_Age])
    prediction = model.predict([input])
    output = round(prediction[0],2)
    
    return render_template('home.html', prediction_text = 'Your Car resale price is {} Lakhs'.format(output))

if __name__ == '__main__':
    app.run(debug = True)
