### House Price Prediction Project Machine Learning Using Flask

![Flask!](https://github.com/Manjesh30Verma/House_Price_Prediction_Machine_Leanring_using_Flask-Project/assets/144987266/7f8d8871-dc0c-476a-9c47-907e13bb0d44)


#### Project Description
This project involves building a machine learning model to predict house prices based on features such as area size, the number of bedrooms, and the age of the house. The project uses Polynomial Regression to capture the non-linear relationships between the features and the house price. A Flask web application is used to provide a user interface where users can input house details and receive price predictions.

#### Technologies Used
- **Python**: For data processing, model training, and backend logic.
- **Scikit-learn**: For machine learning, particularly Polynomial Regression.
- **Flask**: For creating the web application and serving the model.
- **Bootstrap**: For styling the web interface.
- **Joblib**: For saving and loading the machine learning model and polynomial features.

#### Project Structure
- **app.py**: The main Flask application file that loads the model, handles user input, and returns predictions.
- **model_training.py**: A script for training the Polynomial Regression model and saving it using Joblib.
- **templates/home.html**: The HTML template for the web interface, styled using Bootstrap.
- **model.pkl**: The saved Polynomial Regression model.
- **polynomial_features.pkl**: The saved polynomial features transformation object.

#### Key Features
- **Polynomial Regression**: Captures non-linear relationships between features and the target variable (house price).
- **User Interface**: A web form where users can input house details (area size, number of bedrooms, age of the house).
- **Prediction Output**: The predicted house price is displayed to the user, along with the input details.
- **Responsive Design**: Uses Bootstrap for a clean and responsive user interface.

#### How to Use
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Install Dependencies**:
   Create and activate a virtual environment, then install the required packages.
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Train the Model**:
   If not already provided, run the model training script to generate `model.pkl` and `polynomial_features.pkl`.
   ```sh
   python model_training.py
   ```

4. **Run the Flask Application**:
   Start the Flask web server.
   ```sh
   python app.py
   ```

5. **Access the Web Interface**:
   Open a web browser and navigate to `http://127.0.0.1:5000/`. Fill in the house details and submit the form to get the predicted price.

### Example Repository Structure
```
house-price-prediction/
│
├── app.py
├── model_training.py
├── requirements.txt
├── model.pkl
├── polynomial_features.pkl
└── templates/
    └── home.html
