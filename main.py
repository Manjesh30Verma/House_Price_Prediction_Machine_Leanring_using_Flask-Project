from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

model_path ='C:/Users/hp/OneDrive/Desktop/Flask_HousePrice_ML/model.pkl'

model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        age = float(request.form['age'])

        input_data = np.array([[area, bedrooms, age]])

        prediction = model.predict(input_data)
        output = round(prediction[0], 2)

        return render_template('home.html', prediction_text=f'The Predicted Price is: ₹{output}')


if __name__ == "__main__":
    app.run(debug=True)