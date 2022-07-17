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

    data.to_csv('/tmp/sba_raw_' + str(year) + '.csv')


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

def sba_etl(event, context):
    """
    Triggered from a message on a Cloud Pub/Sub topic.
    Args:
      event (dict): Event payload.
      context (google.cloud.functions.Context): Metadata for the event.
    """
    # Download data to /tmp/
    download_sba(2010)
    download_sba(2020)

    # Upload the file to GCS bucket
    upload_sba('sba-raw', '/tmp/sba_raw_2010.csv', 'sba_raw_2010.csv')
    upload_sba('sba-raw', '/tmp/sba_raw_2020.csv', 'sba_raw_2020.csv')

