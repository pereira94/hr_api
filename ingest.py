import requests
from pandas.io.json import json_normalize
import pandas as pd
import time
from decouple import config

def get_data_chunks(chunk):
    x = 0
    y = chunk
    while(y < 40):
        url = 'http://127.0.0.1:5000/api/v1/resources/data/'
        new_url = url + str(x) + '/' + str(y)
        df = pd.read_json(new_url)
        bucket = 'hr-ngestion' 
        csv_buffer = StringIO()
        df.to_csv(csv_buffer)
        df_name = "df" + "_" + str(y)+ ".csv"
        s3_resource = boto3.resource('s3', aws_access_key_id=config("AWS_ACCESS_KEY"), 
                  aws_secret_access_key=config("AWS_SECRET_KEY"))
        s3_resource.Object(bucket, df_name).put(Body=csv_buffer.getvalue())
        x = y + 1
        y += 11
        time.sleep(5) 
        
get_data_chunks(10)