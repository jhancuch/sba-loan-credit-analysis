"""
main.py is the main part of the flask application that serves predictions back of default/
no default
"""
import google.cloud.logging
from flask import Flask, request, jsonify, render_template
from xgboost import XGBClassifier
import pandas as pd

client = google.cloud.logging.Client()

app = Flask(__name__)
client.setup_logging()

# Load model
model = XGBClassifier()
model.load_model("model/model.bst")

# Landing Page
@app.route("/")
def status_check():
    """
    Landing page for application
    """
    return render_template('home.html')

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    """
    Main route of the model that gets the request and delievers the prediction back to the users
    """
    # gather request json and transform to a list
    data = request.get_json()
    json_instances = data["instances"]

    data1 = pd.DataFrame(json_instances, index=[0]).values
    data2 = list(data1)

    # Classifer the input and return the 1/0 prediction
    response = model.predict(data2)

    if response == 1:
        response_value = 'Default (1)'
    else:
        response_value = 'No default (0)'

    return jsonify({"prediction": response_value})

# Start flask app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
