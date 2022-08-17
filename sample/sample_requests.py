from func import predict_custom_trained_model_sample, input1, input2, input3
import os
import numpy as np
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "sba-loan-credit-analysis-c755ef85ba35.json"


predict_custom_trained_model_sample(
    project="sba-loan-credit-analysis",
    endpoint_id="4630368920006557696",
    instances=input1()
)

predict_custom_trained_model_sample(
    project="sba-loan-credit-analysis",
    endpoint_id="4630368920006557696",
    instances=input2()
)

predict_custom_trained_model_sample(
    project="sba-loan-credit-analysis",
    endpoint_id="4630368920006557696",
    instances=input3()
)
