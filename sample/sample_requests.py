from func import predict_custom_trained_model_sample, instance_generator
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "sba-loan-credit-analysis-c755ef85ba35.json"


prediction = predict_custom_trained_model_sample(
    project="sba-loan-credit-analysis",
    endpoint_id="7006580673397915648",
    instances=instance_generator()
)

print(prediction)