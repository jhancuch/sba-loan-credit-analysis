import base64
from google.cloud import storage
import re
import urllib.request
import pandas as pd

def download_sba(year):
  """
  Obtains the url for the .csv file containing sba loan data and returns the data as an object
  year (int): The files are split up by decade, e.g. 2010 or 2020 
  """
  webpage_raw = urllib.request.urlopen('https://data.sba.gov/dataset/7-a-504-foia')
  webpage_bytes = webpage_raw.read()
  webpage_string = webpage_bytes.decode('utf8')
  webpage_raw.close()

  file_url = re.search(r'http.*7afy' + str(year) + '-.*csv', webpage_string)[0]

  data = pd.read_csv(file_url, encoding = "ISO-8859-1", low_memory = False)

  data.to_csv('/tmp/sba_raw_' + str(year) + '.csv', index=False)


def upload_sba(bucket_name, contents, destination_blob_name):
  """
  Uploads a file to the bucket
  bucket_name is a string containing the bucket name
  source_file_name is a string containing 
  destination_blob_name is the name of your object when stored in the bucket
  """
  storage_client = storage.Client()
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)

  blob.upload_from_filename(contents)

def transform_sba():
  """
  Transform sba raw data into the dataset we will feed into the model
  """
  # Load data
  data1 = pd.read_csv('gs://sba-raw/sba_raw_2000.csv')
  data2 = pd.read_csv('gs://sba-raw/sba_raw_2010.csv')
  data3 = pd.read_csv('gs://sba-raw/sba_raw_2020.csv')
  data = pd.concat([data1, data2, data3], ignore_index=True).reset_index(drop=True)

  # subset to observations with the LoanStatus PIF or CHGOFF aka paid in full or charged off. We don't care about loans that are currently being paid back
  df = data[(data['LoanStatus'] == 'PIF') | (data['LoanStatus'] == 'CHGOFF')].drop_duplicates().reset_index(drop=True)

  # convert PIF to 0 and CHGOFF to 1
  df.loc[df['LoanStatus'] == 'PIF', 'LoanStatus'] = '0' 
  df.loc[df['LoanStatus'] == 'CHGOFF', 'LoanStatus'] = '1'
  df['LoanStatus'] = df['LoanStatus'].astype(int)

  core = df[['LoanStatus', 'BankName', 'RevolverStatus', 'TermInMonths', 'ApprovalFiscalYear', 'NaicsCode', 'subpgmdesc', 'BankState', 'BorrState']].copy().dropna()

  # Same state for Bank and Borrower
  core['BorrBankSameState'] = 0
  core.loc[core.BankState == core.BorrState, 'BorrBankSameState'] = 1

  # Number of total loans, total defaults, and percentage of default for each bank
  df_BankDefaults = pd.merge(pd.DataFrame(df.groupby('BankName')['LoanStatus'].count()).reset_index().rename(columns={'LoanStatus':'TotLoanCounts'}), 
                             pd.DataFrame(df.groupby('BankName')['LoanStatus'].sum()).reset_index().rename(columns={'LoanStatus':'TotDefaultCounts'}), 
                             how='inner', on='BankName')
  core = pd.merge(core[['LoanStatus', 'BankName', 'RevolverStatus', 'TermInMonths', 'BorrBankSameState', 'ApprovalFiscalYear', 'NaicsCode', 'subpgmdesc']], 
                  df_BankDefaults, 
                  how='inner', 
                  on='BankName')
  core['TotPctDefault'] = core['TotDefaultCounts']/core['TotLoanCounts']

  # Number of yearly loans, yearly defaults, and percentage of default for each bank for each year of issuance 
  df_BankDefaultsYearly = pd.merge(pd.DataFrame(df.groupby(['BankName', 'ApprovalFiscalYear'])['LoanStatus'].count()).reset_index().rename(columns={'LoanStatus':'YearlyLoanCounts'}), 
                                  pd.DataFrame(df.groupby(['BankName', 'ApprovalFiscalYear'])['LoanStatus'].sum()).reset_index().rename(columns={'LoanStatus':'YearlyDefaultCounts'}), 
                                  how='inner', on=['BankName', 'ApprovalFiscalYear'])
  core = pd.merge(core[['LoanStatus', 'BankName', 'ApprovalFiscalYear', 'RevolverStatus', 'TermInMonths', 'BorrBankSameState',
                        'TotPctDefault', 'TotDefaultCounts', 'TotLoanCounts', 'NaicsCode', 'subpgmdesc']], 
                  df_BankDefaultsYearly, 
                  how='inner', 
                  on=['BankName', 'ApprovalFiscalYear'])
  core['YearlyPctDefault'] = core['YearlyDefaultCounts']/core['YearlyLoanCounts']

  # Dummy variables for all of the sub program descriptions
  core = pd.merge(core.drop('subpgmdesc', axis=1), pd.get_dummies(core['subpgmdesc'], prefix = 'subpgmdesc_', drop_first=True), how='inner', left_index = True, right_index = True)

  # naics code dummy variable
  core['NaicsCode'] = core['NaicsCode'].astype(str)
  core['NaicsCode'] = core['NaicsCode'].str.slice(stop=2)
  core['NaicsCode'] = core['NaicsCode'].astype(int)
  core = pd.merge(core.drop('NaicsCode', axis=1), pd.get_dummies(core['NaicsCode'], prefix = 'NaicsCode_', drop_first=True), how='inner', left_index = True, right_index = True) 

  # dummy variables for all years
  core = pd.merge(core.drop('ApprovalFiscalYear', axis=1), pd.get_dummies(core['ApprovalFiscalYear'], prefix = 'ApprovalFiscalYear_', drop_first=True), how='inner', left_index = True, right_index = True) 

  # remove unnecessary variables
  core.drop(['TotDefaultCounts', 'TotLoanCounts', 'BankName', 'YearlyLoanCounts'], axis=1, inplace=True)

  # save data
  core.to_csv('/tmp/sba_refined.csv', index=False)

def sba_etl(event, context):
  """
  Triggered from a message on a Cloud Pub/Sub topic.
  Args:
    event (dict): Event payload.
    context (google.cloud.functions.Context): Metadata for the event.
  """
  # Download data to /tmp/
  download_sba(2000)
  download_sba(2010)
  download_sba(2020)

  # Upload the file to GCS bucket
  upload_sba('sba-raw', '/tmp/sba_raw_2000.csv', 'sba_raw_2000.csv')
  upload_sba('sba-raw', '/tmp/sba_raw_2010.csv', 'sba_raw_2010.csv')
  upload_sba('sba-raw', '/tmp/sba_raw_2020.csv', 'sba_raw_2020.csv')

  # Transform data
  transform_sba()

  # Upload transformed data to GCS bucket sba-refined
  upload_sba('sba-refined', '/tmp/sba_refined.csv', 'sba_refined.csv')


