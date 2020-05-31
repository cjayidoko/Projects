# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:28:38 2020

@author: chiji
"""

import pandas as pd
import numpy as np
import json
import requests


def retrieve_time_series(api, series_ID):
    '''Return the time series dataframe based on API and Unique series ID'''
    series_search = api.data_by_series(series = series_ID)
    
    df = pd.DataFrame(series_search)
    return df

def retrieve_online(url):
    response = requests.get(url)
    data = response.text
    #Paresed will bring out a json file
    parsed = json.loads(data)# this will be in a dictionary form so you can 
    #call each column data like 'date' and get an array of its rows
    return parsed

#parsed = retrieve_online(https....)
#parsed.keys() will return all the columns
#print(json.dumps(parsed, indent = 4))
#parsed['date']
#parsed.head()