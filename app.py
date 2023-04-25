from flask import Flask, request,  render_template
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
app = Flask(__name__)

# load the trained model
model = joblib.load("model2.joblib")
data = pd.read_csv('framingham.csv')

# Drop the 'TenYearCHD' column from the dataframe
data = data.drop('TenYearCHD', axis=1)
data = data.drop('education', axis=1)

@app.route('/')
def index():
    return render_template('index.html')



UPLOAD_FOLDER = 'uploads'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get values from form
        sex = request.form['sex']
        age = request.form['age']
        currentSmoker = request.form['currentSmoker']
        cigsPerDay = request.form['cigsPerDay']
        BPMeds = request.form['BPMeds']
        prevalentStroke = request.form['prevalentStroke']
        prevalentHyp = request.form['prevalentHyp']
        diabetes = request.form['diabetes']
        totChol = request.form['totChol']
        sysBP = request.form['sysBP']
        diaBP = request.form['diaBP']
        BMI = request.form['BMI']
        heartRate = request.form['heartRate']
        glucose = request.form['glucose']

        # Validate age
        if not age.isnumeric() or int(age) < 0 or int(age) > 120:
            error_msg = "Invalid age value. Please enter a valid age between 0 and 120."
            return render_template('index.html', error_msg=error_msg)
        
        user_data = pd.DataFrame({
            'male': [sex],
            'age': [age],
            'currentSmoker': [currentSmoker],
            'cigsPerDay': [cigsPerDay],
            'BPMeds': [BPMeds],
            'prevalentStroke': [prevalentStroke],
            'prevalentHyp': [prevalentHyp],
            'diabetes': [diabetes],
            'totChol': [totChol],
            'sysBP': [sysBP],
            'diaBP': [diaBP],
            'BMI': [BMI],
            'heartRate': [heartRate],
            'glucose': [glucose],
        })
        user_data = user_data[data.columns]
        # y_pred = model.predict(user_data)
        print(user_data)
        prediction=0
        if(currentSmoker == '0' and prevalentStroke == '0' and diabetes == '0' and prevalentHyp == '0' and BPMeds == '0' ):
              prediction = 0 
        elif(currentSmoker == '1' and prevalentStroke == '1' and diabetes == '1' and prevalentHyp == '1' and BPMeds == '1'):
              prediction = 1 
        elif((float(totChol)>300 and float(BMI) > 24) and int(cigsPerDay) > 3 ):
              prediction = 1        
        print(prediction)
        
        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)