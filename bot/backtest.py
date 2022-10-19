# -*- coding: utf-8 -*-
"""
Created on Mon May 23 09:51:11 2022

@author: KRISHNA_CHAITANYA
"""
from datetime import date
from datetime import timedelta
import pandas as pd
from position import Position
from strategy import Strategy
import yfinance as yf
from pandas_datareader import data as pdr
yf.pdr_override()
import time
today = date.today()
yesterday = today - timedelta(days = 1)
yt = yesterday-timedelta(days = 1)
symbol="WIPRO.NS"
main = Position()
main.display()
while True:
    past = pdr.get_data_yahoo(symbol,start=yesterday,end=today,interval = '1m')
    past_index = pd.Series(past.index)
    
    current = pdr.get_data_yahoo(symbol,start=today,interval = '1m')
    current_index = pd.Series(current.index)
    analysis = Strategy()
    for i in current_index: 
        #past.drop(past.iloc[0],inplace=True)
        #print(i)
        past.loc[i] = current.loc[i]
        if analysis.moving_average(past) == 'buy':
            main.long(past.loc[i]["Close"])
            
        if analysis.moving_average(past) == 'sell':
            main.short(past.loc[i]["Close"])
        main.display()
    time.sleep(1000)
main.square_off(past.iloc[len(past.index)-1]['Close'])
#print(past)
#print(current)
