"""
func.py contains the main function that interacts with the GCP API and the three
sample requests that are sent
"""

from typing import Dict, List, Union
import random

from google.cloud import storage
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

def predict_custom_trained_model_sample(
    project: str,
    endpoint_id: str,
    instances: Union[Dict, List[Dict]],
    location: str = "us-east4",
    api_endpoint: str = "us-east4-aiplatform.googleapis.com",
):
    """
    `instances` can be either single instance of type dict or a list
    of instances.
    """
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    # The format of each instance should conform to the deployed model's prediction input schema.
    instances = instances if type(instances) == list else [instances]
    instances = [
        json_format.ParseDict(instance_dict, Value()) for instance_dict in instances
    ]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    
    print("Estimate (0 no default, 1 default): ")
    print(response.predictions)    

def input1():
    """
    The function provides the input values
    """
    dictionary = {"RevolverStatus": 1, 
                  "TermInMonths": 144, 
                  "BorrBankSameState": .3, 
                  "TotPctDefault": .1,
                  "YearlyDefaultCounts": 600, 
                  "YearlyPctDefault": .12,
                  "subpgmdesc__Community Advantage Initiative": 1,
                  "subpgmdesc__Community Express": 0, 
                  "subpgmdesc__Contract Guaranty": 0,
                  "subpgmdesc__Defense Loans and Technical Assistance, Funded 9/26/95": 0,
                  "subpgmdesc__EXPORT IMPORT HARMONIZATION": 0,
                  "subpgmdesc__FA$TRK (Small Loan Express)": 0, 
                  "subpgmdesc__Guaranty": 0,
                  "subpgmdesc__Gulf Opportunity": 0,
                  "subpgmdesc__International Trade - Sec, 7(a) (16)": 0,
                  "subpgmdesc__Lender Advantage Initiative": 0,
                  "subpgmdesc__Patriot Express": 0,
                  "subpgmdesc__Revolving Line of Credit Exports - Sec. 7(a) (14)": 0,
                  "subpgmdesc__Rural Lender Advantage": 0,
                  "subpgmdesc__Seasonal Line of Credit": 0, 
                  "subpgmdesc__Small Asset Based": 0,
                  "subpgmdesc__Small General Contractors - Sec. 7(a) (9)": 0,
                  "subpgmdesc__Standard Asset Based": 0,
                  "subpgmdesc__USCAIP Guaranty (NAFTA)": 0, 
                  "subpgmdesc__Y2K Loan": 0,
                  "NaicsCode__21": 0, 
                  "NaicsCode__22": 0, 
                  "NaicsCode__23": 0, 
                  "NaicsCode__31": 0,
                  "NaicsCode__32": 1, 
                  "NaicsCode__33": 0, 
                  "NaicsCode__42": 0, 
                  "NaicsCode__44": 0,
                  "NaicsCode__45": 0, 
                  "NaicsCode__48": 0, 
                  "NaicsCode__49": 0, 
                  "NaicsCode__51": 0,
                  "NaicsCode__52": 0, 
                  "NaicsCode__53": 0, 
                  "NaicsCode__54": 0, 
                  "NaicsCode__55": 0,
                  "NaicsCode__56": 0, 
                  "NaicsCode__61": 0, 
                  "NaicsCode__62": 0, 
                  "NaicsCode__71": 0,
                  "NaicsCode__72": 0, 
                  "NaicsCode__81": 0, 
                  "NaicsCode__92": 0,
                  "ApprovalFiscalYear__2001": 0, 
                  "ApprovalFiscalYear__2002": 0,
                  "ApprovalFiscalYear__2003": 0, 
                  "ApprovalFiscalYear__2004": 0,
                  "ApprovalFiscalYear__2005": 0, 
                  "ApprovalFiscalYear__2006": 0,
                  "ApprovalFiscalYear__2007": 0, 
                  "ApprovalFiscalYear__2008": 0,
                  "ApprovalFiscalYear__2009": 0, 
                  "ApprovalFiscalYear__2010": 0,
                  "ApprovalFiscalYear__2011": 0, 
                  "ApprovalFiscalYear__2012": 0,
                  "ApprovalFiscalYear__2013": 0, 
                  "ApprovalFiscalYear__2014": 0,
                  "ApprovalFiscalYear__2015": 0, 
                  "ApprovalFiscalYear__2016": 0,
                  "ApprovalFiscalYear__2017": 0, 
                  "ApprovalFiscalYear__2018": 0,
                  "ApprovalFiscalYear__2019": 0, 
                  "ApprovalFiscalYear__2020": 0,
                  "ApprovalFiscalYear__2021": 0, 
                  "ApprovalFiscalYear__2022": 1}

    return dictionary

def input2():
    """
    The function provides the input values
    """
    dictionary = {"RevolverStatus": 1, 
                  "TermInMonths": 112, 
                  "BorrBankSameState": .2, 
                  "TotPctDefault": .15,
                  "YearlyDefaultCounts": 200, 
                  "YearlyPctDefault": .1,
                  "subpgmdesc__Community Advantage Initiative": 0,
                  "subpgmdesc__Community Express": 1, 
                  "subpgmdesc__Contract Guaranty": 0,
                  "subpgmdesc__Defense Loans and Technical Assistance, Funded 9/26/95": 0,
                  "subpgmdesc__EXPORT IMPORT HARMONIZATION": 0,
                  "subpgmdesc__FA$TRK (Small Loan Express)": 0, 
                  "subpgmdesc__Guaranty": 0,
                  "subpgmdesc__Gulf Opportunity": 0,
                  "subpgmdesc__International Trade - Sec, 7(a) (16)": 0,
                  "subpgmdesc__Lender Advantage Initiative": 0,
                  "subpgmdesc__Patriot Express": 0,
                  "subpgmdesc__Revolving Line of Credit Exports - Sec. 7(a) (14)": 0,
                  "subpgmdesc__Rural Lender Advantage": 0,
                  "subpgmdesc__Seasonal Line of Credit": 0, 
                  "subpgmdesc__Small Asset Based": 0,
                  "subpgmdesc__Small General Contractors - Sec. 7(a) (9)": 0,
                  "subpgmdesc__Standard Asset Based": 0,
                  "subpgmdesc__USCAIP Guaranty (NAFTA)": 0, 
                  "subpgmdesc__Y2K Loan": 0,
                  "NaicsCode__21": 0, 
                  "NaicsCode__22": 0, 
                  "NaicsCode__23": 0, 
                  "NaicsCode__31": 0,
                  "NaicsCode__32": 0, 
                  "NaicsCode__33": 0, 
                  "NaicsCode__42": 0, 
                  "NaicsCode__44": 1,
                  "NaicsCode__45": 0, 
                  "NaicsCode__48": 0, 
                  "NaicsCode__49": 0, 
                  "NaicsCode__51": 0,
                  "NaicsCode__52": 0, 
                  "NaicsCode__53": 0, 
                  "NaicsCode__54": 0, 
                  "NaicsCode__55": 0,
                  "NaicsCode__56": 0, 
                  "NaicsCode__61": 0, 
                  "NaicsCode__62": 0, 
                  "NaicsCode__71": 0,
                  "NaicsCode__72": 0, 
                  "NaicsCode__81": 0, 
                  "NaicsCode__92": 0,
                  "ApprovalFiscalYear__2001": 0, 
                  "ApprovalFiscalYear__2002": 0,
                  "ApprovalFiscalYear__2003": 0, 
                  "ApprovalFiscalYear__2004": 0,
                  "ApprovalFiscalYear__2005": 0, 
                  "ApprovalFiscalYear__2006": 0,
                  "ApprovalFiscalYear__2007": 0, 
                  "ApprovalFiscalYear__2008": 0,
                  "ApprovalFiscalYear__2009": 0, 
                  "ApprovalFiscalYear__2010": 0,
                  "ApprovalFiscalYear__2011": 0, 
                  "ApprovalFiscalYear__2012": 0,
                  "ApprovalFiscalYear__2013": 0, 
                  "ApprovalFiscalYear__2014": 0,
                  "ApprovalFiscalYear__2015": 0, 
                  "ApprovalFiscalYear__2016": 0,
                  "ApprovalFiscalYear__2017": 0, 
                  "ApprovalFiscalYear__2018": 0,
                  "ApprovalFiscalYear__2019": 0, 
                  "ApprovalFiscalYear__2020": 0,
                  "ApprovalFiscalYear__2021": 0, 
                  "ApprovalFiscalYear__2022": 1}

    return dictionary

def input3():
    """
    The function provides the input values
    """
    dictionary = {"RevolverStatus": 0, 
                  "TermInMonths": 12, 
                  "BorrBankSameState": 1, 
                  "TotPctDefault": .9,
                  "YearlyDefaultCounts": 5, 
                  "YearlyPctDefault": .9,
                  "subpgmdesc__Community Advantage Initiative": 1,
                  "subpgmdesc__Community Express": 0, 
                  "subpgmdesc__Contract Guaranty": 0,
                  "subpgmdesc__Defense Loans and Technical Assistance, Funded 9/26/95": 0,
                  "subpgmdesc__EXPORT IMPORT HARMONIZATION": 0,
                  "subpgmdesc__FA$TRK (Small Loan Express)": 0, 
                  "subpgmdesc__Guaranty": 0,
                  "subpgmdesc__Gulf Opportunity": 0,
                  "subpgmdesc__International Trade - Sec, 7(a) (16)": 0,
                  "subpgmdesc__Lender Advantage Initiative": 0,
                  "subpgmdesc__Patriot Express": 0,
                  "subpgmdesc__Revolving Line of Credit Exports - Sec. 7(a) (14)": 0,
                  "subpgmdesc__Rural Lender Advantage": 0,
                  "subpgmdesc__Seasonal Line of Credit": 0, 
                  "subpgmdesc__Small Asset Based": 0,
                  "subpgmdesc__Small General Contractors - Sec. 7(a) (9)": 0,
                  "subpgmdesc__Standard Asset Based": 0,
                  "subpgmdesc__USCAIP Guaranty (NAFTA)": 0, 
                  "subpgmdesc__Y2K Loan": 0,
                  "NaicsCode__21": 0, 
                  "NaicsCode__22": 0, 
                  "NaicsCode__23": 0, 
                  "NaicsCode__31": 0,
                  "NaicsCode__32": 0, 
                  "NaicsCode__33": 0, 
                  "NaicsCode__42": 0, 
                  "NaicsCode__44": 0,
                  "NaicsCode__45": 0, 
                  "NaicsCode__48": 0, 
                  "NaicsCode__49": 0, 
                  "NaicsCode__51": 0,
                  "NaicsCode__52": 0, 
                  "NaicsCode__53": 0, 
                  "NaicsCode__54": 0, 
                  "NaicsCode__55": 0,
                  "NaicsCode__56": 0, 
                  "NaicsCode__61": 1, 
                  "NaicsCode__62": 0, 
                  "NaicsCode__71": 0,
                  "NaicsCode__72": 0, 
                  "NaicsCode__81": 0, 
                  "NaicsCode__92": 0,
                  "ApprovalFiscalYear__2001": 0, 
                  "ApprovalFiscalYear__2002": 0,
                  "ApprovalFiscalYear__2003": 0, 
                  "ApprovalFiscalYear__2004": 0,
                  "ApprovalFiscalYear__2005": 0, 
                  "ApprovalFiscalYear__2006": 0,
                  "ApprovalFiscalYear__2007": 0, 
                  "ApprovalFiscalYear__2008": 0,
                  "ApprovalFiscalYear__2009": 0, 
                  "ApprovalFiscalYear__2010": 0,
                  "ApprovalFiscalYear__2011": 0, 
                  "ApprovalFiscalYear__2012": 0,
                  "ApprovalFiscalYear__2013": 1, 
                  "ApprovalFiscalYear__2014": 0,
                  "ApprovalFiscalYear__2015": 0, 
                  "ApprovalFiscalYear__2016": 0,
                  "ApprovalFiscalYear__2017": 0, 
                  "ApprovalFiscalYear__2018": 0,
                  "ApprovalFiscalYear__2019": 0, 
                  "ApprovalFiscalYear__2020": 0,
                  "ApprovalFiscalYear__2021": 0, 
                  "ApprovalFiscalYear__2022": 0}

    return dictionary