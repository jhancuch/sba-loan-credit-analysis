# Small Business Administration 7(a) Loan Default Predictions

![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
[![CircleCI](https://circleci.com/gh/jhancuch/sba-loan-credit-analysis.svg?style=svg)](https://circleci.com/gh/jhancuch/sba-loan-credit-analysis)

## Introduction:
The project's inspiration is from the 2008 financial crisis. In the 2008, home loans were issued to buyers whose risk of default was not correctly conveyed in the grading of the securitized bonds who consisted of many home loans packaged together. Thus, banks were holding much riskier assets than they expected. 

The SBA 7(a) loan is different. While it can be securitized, it can only be for the guaranteed amount.  However, if this requirement went away, the smaller banks issuing the loans, securitizing them, and selling them to investors may misrepresent the riskiness of some of the loans part of the securitized bond. 

This application allows a potential investor to check the risk of default for each loan within a securitized bond allowing them to verify the overall risk associated with the securitized bond. This concept can also be applied to other securitized bonds where the investor only has information about the loan but not the underlying financials of the borrower.

## How to Test Run the API
Step 1: Create empty directory and clone github repository.
```
cd ~
mkdir sba-loan-credit-analysis
git clone https://github.com/jhancuch/sba-loan-credit-analysis
```

Step 2: Navigate to the sample folder
```
cd ~/sba-loan-credit-analysis/sba-loan-credit-analysis/sample
```

Step 3: Run the Make file to install dependencies and run the examples.
```
make all
```

## Formatting Your Own Submission
It is recommended that you use the Make file to install the dependencies needed. Second, the user should use the predict_custom_trained_model_sample function in ~/sample/sample_requests.py as the template for their own requests. All the user has to do is update how they want to load the .json file for the "instances" argument.

The input has to be 70 numeric (int and float) fields. A json input should look like the following:
```json
{"RevolverStatus": 1,
 "TermInMonths": 144, 
 "BorrBankSameState": .30, 
 "TotPctDefault": .10,
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
```
