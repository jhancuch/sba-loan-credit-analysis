import os
import logging
from flask import Flask
from flask import request, escape
from ingest_sba import download, upload

app = Flask(__name__)

@app.route("/", methods=['POST'])
def ingest_sba():
    try:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
        json = request.get_json(force=True) # https://stackoverflow.com/questions/53216177/http-triggering-cloud-function-with-cloud-scheduler/60615210#60615210

        #df_2010 = download(2010)
        df_2020 = download(2020)

        #upload('sba-raw', df_2010, 'sba-raw-2010')
        upload('sba-raw', df_2020, 'sba-raw-2020')
        
    except Exception as e:
        logging.exception('Failed to download and upload sba data')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

