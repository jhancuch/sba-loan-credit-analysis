import logging 

import re
import pandas as pd
import urllib.request

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

def upload_raw(blob):
    """
    Uploads .csv file that is currently a dataframe held in memory to bucket sba-raw
    
    """
