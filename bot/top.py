# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:25:34 2022

@author: KRISHNA_CHAITANYA
"""

import io
import pandas as pd
import requests
url = "https://www1.nseindia.com/content/indices/ind_nifty50list.csv"

def get_top():
    
    data_req=requests.get(url).content

    data=pd.read_csv(io.StringIO(data_req.decode('utf-8')))
    li = data.head(10)
    return (li['Symbol'])
