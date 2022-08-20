import google.cloud.logging
from flask import Flask, request, Response, jsonify
from xgboost import XGBClassifier
import pandas as pd

client = google.cloud.logging.Client()

app = Flask(__name__)
client.setup_logging()

# Load model
model = XGBClassifier()
model.load_model("model/model.bst")

# Health check route
@app.route("/statuscheck")
def status_check():
    """
    Vertex AI models requires an app route to send periodic messages to/check the health of the application
    """
    print("/statuscheck request")
    status_code = Response(status=200)
    return status_code

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    """
    Main route of the model that gets the request and delievers the prediction back to the users
    """
    print("/predict request")

    # gather request json and transform to a list
    data = request.get_json()
    json_instances = data["instances"]

    data1 = pd.DataFrame(json_instances, index=[0]).values
    data2 = list(data1)

    # Classifer the input and return the 1/0 prediction
    response = model.predict(data2)

    return jsonify({"predictions": response.tolist()})

# Start flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)
