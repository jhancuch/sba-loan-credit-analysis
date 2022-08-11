from flask import Flask, request, Response, jsonify
import pickle
from xgboost import XGBClassifier
import pandas as pd

app = Flask(__name__)

# Load model
model_path = "model/model.pkl"

with open(model_path, "rb") as file:
    model = pickle.load(file)

# Health check route
@app.route("/statuscheck")
def status_check():
    print("/statuscheck request")
    status_code = Response(status=200)
    return status_code

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    print("/predict request")
    
    #data = request.get_json()

    #preds = model.predict(pd.DataFrame(data['instance']))
    preds = model.predict(pd.DataFrame(request.get_json(), index=[0]))
    if preds == 1:
        return_value = 'Default'
    if preds == 0:
        return_value = 'No Default'
    return return_value

# Start flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)