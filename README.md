# Car Selling Price Prediction

## Project Overview
This project predicts the selling price of a used car based on its features using Machine Learning. A Flask web application allows users to enter car details and receive an estimated selling price.

## Objectives
- Analyze used-car data.
- Build a Machine Learning model to predict selling prices.
- Create a simple web interface using Flask.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Flask
- Joblib
- HTML and CSS

## Features
- Enter car details through a web form.
- Predict the estimated selling price.
- Display the result in Indian rupees.

## Project Structure
```text
├── app.py
├── car_price_model.pkl
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
├── Task_2_.ipynb
└── cardekho (1).csv
```

## Installation and Setup

## Getting Started

Follow these steps to run the project on your local machine.

**1. Download the project**

```bash
git clone https://github.com/sparsh220/Car-Selling-Price-Prediction.git
```

**2. Navigate to the project directory**

```bash
cd Car-Selling-Price-Prediction
```

**3. Install the dependencies**

Install all the required Python libraries using the provided requirements file.

```bash
pip install -r requirements.txt
```

**4. Launch the application**

Start the Flask server by running:

```bash
python app.py
```

**5. Open the web application**

Once the server starts, open the following address in your browser:

http://127.0.0.1:5000/

Enter the car details in the form and click **Predict** to get the estimated selling price.

## How to Use
1. Enter the car details in the form.
2. Click the Predict button.
3. View the estimated selling price.

## Disclaimer
The predicted price is an estimate and may differ from the actual market price.