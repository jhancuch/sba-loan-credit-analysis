import logging 

import re

def download(year: int):
    """
    Obtains the url for the .csv file containing sba loan data and returns the data as an object
    year (int): The files are split up by decade, e.g. 2010 or 2020
    """

    logging.info('Requesting data for 10 year increment starting in {}.'.format(year))

    REGEX_STRING = 'r"http.*7afy' + str(year) + '-fy' + str(year + 9) + '.*csv"'

    url_string = re.search(REGEX_STRING)




