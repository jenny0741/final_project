from flask import Flask, render_template, redirect, request
import pickle
import joblib
import pandas as pd
import numpy as np
from tensorflow import keras
app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")


@app.route("/form", methods = ['POST'])
def form():
     
    print("hello")
    input_list = []
    input_list.append(float(request.form['age']))
    input_list.append(float(request.form['gender']))
    input_list.append(float(request.form['chest_pain']))
    input_list.append(float(request.form['trestbps']))
    input_list.append(float(request.form['chol']))
    input_list.append(float(request.form['fbs']))
    input_list.append(float(request.form['restecg']))
    input_list.append(float(request.form['thalach']))
    input_list.append(float(request.form['exang']))
    input_list.append(float(request.form['oldpeak']))
    input_list.append(float(request.form['location']))
    print(input_list)
    input_list=[input_list]
    scaler = joblib.load('notebooks/scaler.save')
    pickled_model = pickle.load(open('notebooks/nn_model.pkl', 'rb'))
    tem_df=pd.DataFrame(input_list)
    xinput = scaler.transform(tem_df)
    print(xinput)
    #finished=pickled_model.predict(xinput)
    reconstructed_model = keras.models.load_model("notebooks/nn") 
    finished=reconstructed_model.predict(xinput)
    print(finished)
    return render_template("index.html",prediction_result=finished[0][0])
if __name__ == "__main__":
    app.run(debug=True)
