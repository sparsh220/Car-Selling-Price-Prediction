
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('car_price_model.pkl')


# 1. Clean the input data
def get_clean_data(form_data):

    cleaned_data = {
        'brand': [form_data['name']],

        'year': [int(form_data['year'])],

        'km_driven': [int(form_data['km_driven'])],

        'fuel': [form_data['fuel']],

        'seller_type': [form_data['seller_type']],

        'transmission': [form_data['transmission']],

        'owner': [form_data['owner']],

        'mileage': [float(form_data['mileage'])],

        'engine': [float(form_data['engine'])],

        'max_power': [float(form_data['max_power'])],

        'seats': [float(form_data['seats'])]
    }

    return cleaned_data


# 2. Display the homepage
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# 3. Predict the car selling price
@app.route("/predict", methods=["POST"])
def get_prediction():

    car_data = request.form

    data_clean = get_clean_data(car_data)

    car_data_df = pd.DataFrame(data_clean)

    prediction = model.predict(car_data_df)

    return render_template(
        "result.html",
        prediction=round(float(prediction[0]), 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
