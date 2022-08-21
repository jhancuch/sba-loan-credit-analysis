# Small Business Administration 7(a) Loan Default Predictions

![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
[![CircleCI](https://circleci.com/gh/jhancuch/sba-loan-credit-analysis.svg?style=svg)](https://circleci.com/gh/jhancuch/sba-loan-credit-analysis)

## Introduction:
The project's inspiration is from the 2008 financial crisis. In the 2008, home loans were issued to buyers whose risk of default was not correctly conveyed in the grading of the securitized bonds who consisted of many home loans packaged together. Thus, banks were holding much riskier assets than they expected. 

The SBA 7(a) loan is different. While it can be securitized, it can only be for the guaranteed amount.  However, if this requirement went away, the smaller banks issuing the loans, securitizing them, and selling them to investors may misrepresent the riskiness of some of the loans part of the securitized bond. 

This application allows a potential investor to check the risk of default for each loan within a securitized bond allowing them to verify the overall risk associated with the securitized bond. This concept can also be applied to other securitized bonds where the investor only has information about the loan but not the underlying financials of the borrower.

## How to Test Run the API
Submit the following cURL command
```
curl --request POST 'https://sba-loan-credit-analysis.uk.r.appspot.com/predict' \
--header 'Content-Type:application/json' \
--data '{"instances": [{"RevolverStatus":1,"TermInMonths":144,"InitialInterestRate":6.00,"BorrBankSameState":0.30,"TotPctDefault":0.15,"TotDefaultCounts":610,"TotLoanCounts":5000,"YearlyLoanCounts":233,"YearlyDefaultCounts":32,"CumulativeDefault":600,"CumulativeLoansIssued":4000,"YearlyPctDefault":0.12,"CumulativeYearlyPctDefault":0.18,"subpgmdesc_community_express":0,"Year2006":0,"Year2007":0}]}'
```

## Formatting Your Own Submission
The user can easily modify this cURL request to fit their needs. The JSON input has 16 numeric (int and float) fields. An example JSON input that is formatted is below for the users ease/convience of editing it for their own cURL request.
```json
{
	"instances": [{
		"RevolverStatus":1,
		"TermInMonths":144,
		"InitialInterestRate":6.00,
		"BorrBankSameState":0.30,
		"TotPctDefault":0.15,
		"TotDefaultCounts":610,
		"TotLoanCounts":5000,
		"YearlyLoanCounts":233,
		"YearlyDefaultCounts":32,
		"CumulativeDefault":600,
		"CumulativeLoansIssued":4000,
		"YearlyPctDefault":0.12,
		"CumulativeYearlyPctDefault":0.18,
		"subpgmdesc_community_express":0,
		"Year2006":0,
		"Year2007":0
	}]
}
```
