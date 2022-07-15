from ingest_sba import download, upload

#df_2010 = download(2010)
df_2020 = download(2020)

#upload('sba-raw', df_2010, 'sba-raw-2010')
upload('sba-raw', df_2020, 'sba-raw-2020')