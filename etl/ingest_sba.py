import os
import logging

import re
import pandas as pd
import urllib.request

from google.cloud import storage


def download(year: int):
    """
    Obtains the url for the .csv file containing sba loan data and returns the data as an object
    year (int): The files are split up by decade, e.g. 2010 or 2020
    """

    logging.info('Requesting data for 10 year increment starting in {}.'.format(year))
    
    webpage_raw = urllib.request.urlopen('https://data.sba.gov/dataset/7-a-504-foia')
    webpage_bytes = webpage_raw.read()
    webpage_string = webpage_bytes.decode('utf8')
    webpage_raw.close()

    url_string = re.search(r'http.*7afy' + str(year) + '-.*csv', webpage_string)[0]
    
    data = pd.read_csv(url_string, encoding = "ISO-8859-1", low_memory = False)

    logging.info('Data obtained and returned as an object')
    return data

def upload(bucket_name, contents, storage_name):
    """
    Uploads .csv file that is currently a dataframe held in memory to bucket sba-raw
    df is a pandas datame
    name is the name we'd like to name the object in the GCP bucket
    """

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(storage_name)

    logging.info('{} being uploaded to bucket {}'.format(bucket_name))

    blob.upload_from_string(contents.to_csv(), 'text/csv')

    logging.info('Upload Complete')



