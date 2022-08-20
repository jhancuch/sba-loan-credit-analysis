"""
template that sends three requests to the API endpoint and returns the prediction of
default/no default
"""
import os
from func import predict_custom_trained_model_sample, input1, input2, input3

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "sba-loan-credit-analysis-c755ef85ba35.json"
PROJ = "sba-loan-credit-analysis"
ENDPOINT = "4630368920006557696"

predict_custom_trained_model_sample(
    project=PROJ,
    endpoint_id=ENDPOINT,
    instances=input1()
)

predict_custom_trained_model_sample(
    project=PROJ,
    endpoint_id=ENDPOINT,
    instances=input2()
)

predict_custom_trained_model_sample(
    project=PROJ,
    endpoint_id=ENDPOINT,
    instances=input3()
)
