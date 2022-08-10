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
    
    data = request.get_json()
    """
    RevolverStatus=int(data['RevolverStatus'])
    TermInMonths=int(data['TermInMonths'])
    BorrBankSameState=int(data['BorrBankSameState'])
    TotPctDefault=float(data['TotPctDefault'])
    YearlyDefaultCounts=int(data['YearlyDefaultCounts'])
    YearlyPctDefault=float(data['YearlyPctDefault'])
    subpgmdesc__Community_AI=int(data['subpgmdesc__Community Advantage Initiative'])
    subpgmdesc__Community=int(data['subpgmdesc__Community Express'])
    subpgmdesc__Contract=int(data['subpgmdesc__Contract Guaranty'])
    subpgmdesc__Defense=int(data['subpgmdesc__Defense Loans and Technical Assistance, Funded 9/26/95'])
    subpgmdesc__EXPORT=int(data['subpgmdesc__EXPORT IMPORT HARMONIZATION'])
    subpgmdesc__FA=int(data['subpgmdesc__FA$TRK (Small Loan Express)'])
    subpgmdesc__Guaranty=int(data['subpgmdesc__Guaranty'])
    subpgmdesc__Gulf=int(data['subpgmdesc__Gulf Opportunity'])
    subpgmdesc__International=int(data['subpgmdesc__International Trade - Sec, 7(a) (16)'])
    subpgmdesc__Lender=int(data['subpgmdesc__Lender Advantage Initiative'])
    subpgmdesc__Patriot=int(data['subpgmdesc__Patriot Express'])
    subpgmdesc__Revolving=int(data['subpgmdesc__Revolving Line of Credit Exports - Sec. 7(a) (14)'])
    subpgmdesc__Rural=int(data['subpgmdesc__Rural Lender Advantage'])
    subpgmdesc__Seasonal=int(data['subpgmdesc__Seasonal Line of Credit'])
    subpgmdesc__Small=int(data['subpgmdesc__Small Asset Based'])
    subpgmdesc__Small=int(data['subpgmdesc__Small General Contractors - Sec. 7(a) (9)'])
    subpgmdesc__Standard=int(data['subpgmdesc__Standard Asset Based'])
    subpgmdesc__USCAIP=int(data['subpgmdesc__USCAIP Guaranty (NAFTA)'])
    subpgmdesc__Y2K=int(data['subpgmdesc__Y2K Loan'])
    NaicsCode__21=int(data['NaicsCode__21'])
    NaicsCode__22=int(data['NaicsCode__22'])
    NaicsCode__23=int(data['NaicsCode__23'])
    NaicsCode__31=int(data['NaicsCode__31'])
    NaicsCode__32=int(data['NaicsCode__32'])
    NaicsCode__33=int(data['NaicsCode__33'])
    NaicsCode__42=int(data['NaicsCode__42'])
    NaicsCode__44=int(data['NaicsCode__44'])
    NaicsCode__45=int(data['NaicsCode__45'])
    NaicsCode__48=int(data['NaicsCode__48'])
    NaicsCode__49=int(data['NaicsCode__49'])
    NaicsCode__51=int(data['NaicsCode__51'])
    NaicsCode__52=int(data['NaicsCode__52'])
    NaicsCode__53=int(data['NaicsCode__53'])
    NaicsCode__54=int(data['NaicsCode__54'])
    NaicsCode__55=int(data['NaicsCode__55'])
    NaicsCode__56=int(data['NaicsCode__56'])
    NaicsCode__61=int(data['NaicsCode__61'])
    NaicsCode__62=int(data['NaicsCode__62'])
    NaicsCode__71=int(data['NaicsCode__71'])
    NaicsCode__72=int(data['NaicsCode__72'])
    NaicsCode__81=int(data['NaicsCode__81'])
    NaicsCode__92=int(data['NaicsCode__92'])
    ApprovalFiscalYear__2001=int(data['ApprovalFiscalYear__2001'])
    ApprovalFiscalYear__2002=int(data['ApprovalFiscalYear__2002'])
    ApprovalFiscalYear__2003=int(data['ApprovalFiscalYear__2003'])
    ApprovalFiscalYear__2004=int(data['ApprovalFiscalYear__2004'])
    ApprovalFiscalYear__2005=int(data['ApprovalFiscalYear__2005'])
    ApprovalFiscalYear__2006=int(data['ApprovalFiscalYear__2006'])
    ApprovalFiscalYear__2007=int(data['ApprovalFiscalYear__2007'])
    ApprovalFiscalYear__2008=int(data['ApprovalFiscalYear__2008'])
    ApprovalFiscalYear__2009=int(data['ApprovalFiscalYear__2009'])
    ApprovalFiscalYear__2010=int(data['ApprovalFiscalYear__2010'])
    ApprovalFiscalYear__2011=int(data['ApprovalFiscalYear__2011'])
    ApprovalFiscalYear__2012=int(data['ApprovalFiscalYear__2012'])
    ApprovalFiscalYear__2013=int(data['ApprovalFiscalYear__2013'])
    ApprovalFiscalYear__2014=int(data['ApprovalFiscalYear__2014'])
    ApprovalFiscalYear__2015=int(data['ApprovalFiscalYear__2015'])
    ApprovalFiscalYear__2016=int(data['ApprovalFiscalYear__2016'])
    ApprovalFiscalYear__2017=int(data['ApprovalFiscalYear__2017'])
    ApprovalFiscalYear__2018=int(data['ApprovalFiscalYear__2018'])
    ApprovalFiscalYear__2019=int(data['ApprovalFiscalYear__2019'])
    ApprovalFiscalYear__2020=int(data['ApprovalFiscalYear__2020'])
    ApprovalFiscalYear__2021=int(data['ApprovalFiscalYear__2021'])
    ApprovalFiscalYear__2022=int(data['ApprovalFiscalYear__2022'])

    new_record = [[RevolverStatus,TermInMonths,BorrBankSameState,TotPctDefault,YearlyDefaultCounts,YearlyPctDefault,subpgmdesc__Community_AI,subpgmdesc__Community,subpgmdesc__Contract,
    subpgmdesc__Defense,subpgmdesc__EXPORT,subpgmdesc__FA,subpgmdesc__Guaranty,subpgmdesc__Gulf,subpgmdesc__International,subpgmdesc__Lender,subpgmdesc__Patriot,subpgmdesc__Revolving,
    subpgmdesc__Rural,subpgmdesc__Seasonal,subpgmdesc__Small,subpgmdesc__Small,subpgmdesc__Standard,subpgmdesc__USCAIP,subpgmdesc__Y2K,NaicsCode__21,NaicsCode__22,NaicsCode__23,
    NaicsCode__31,NaicsCode__32,NaicsCode__33,NaicsCode__42,NaicsCode__44,NaicsCode__45,NaicsCode__48,NaicsCode__49,NaicsCode__51,NaicsCode__52,NaicsCode__53,NaicsCode__54,NaicsCode__55,
    NaicsCode__56,NaicsCode__61,NaicsCode__62,NaicsCode__71,NaicsCode__72,NaicsCode__81,NaicsCode__92,ApprovalFiscalYear__2001,ApprovalFiscalYear__2002,ApprovalFiscalYear__2003,
    ApprovalFiscalYear__2004,ApprovalFiscalYear__2005,ApprovalFiscalYear__2006,ApprovalFiscalYear__2007,ApprovalFiscalYear__2008,ApprovalFiscalYear__2009,ApprovalFiscalYear__2010,
    ApprovalFiscalYear__2011,ApprovalFiscalYear__2012,ApprovalFiscalYear__2013,ApprovalFiscalYear__2014,ApprovalFiscalYear__2015,ApprovalFiscalYear__2016,ApprovalFiscalYear__2017,
    ApprovalFiscalYear__2018,ApprovalFiscalYear__2019,ApprovalFiscalYear__2020,ApprovalFiscalYear__2021,ApprovalFiscalYear__2022]]
    """
    preds = model.predict(pd.DataFrame(data['instance']))
    if preds == 1:
        return_value = 'Default'
    if preds == 0:
        return_value = 'No Default'
    return return_value

# Start flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)