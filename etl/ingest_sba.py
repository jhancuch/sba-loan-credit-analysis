import logging 

def download(year: str):
    """
    Obtains the url for the .csv file containing sba loan data and returns the data as an object
    year (string): The files are split up by decade, e.g. "2010", "2020"
    """

    logging