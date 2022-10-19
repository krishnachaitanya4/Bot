# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:44:36 2022

@author: KRISHNA_CHAITANYA
"""
from datetime import datetime
import time
import yfinance as yf
from log import Log
import pandas as pd
from pandas_datareader import data as pdr
from strategy import Strategy
from top import get_top
import matplotlib.pyplot as plt
from position import Position

now = datetime.now()
folder = now.strftime("%d-%m-%y")
Log.create_dir(folder)
yf.pdr_override()
tickers = get_top()
tickers = [i+'.NS' for i in tickers]
#print(tickers)
for i in tickers:
    Log.create_file(i,folder)
    
analysis = Strategy()

main = {}
for i in tickers:
    main[i] = Position()
'''    
for i,j in main.items():
    print(i,":")
    main[i].display()'''
f = True
while True:
    if not f: break
    now = datetime.now()
    hour,minute,second = now.hour,now.minute,now.second
    print(hour,': ',minute,": ",second)
    #t = now.strftime("%H:%M:%S")
    if(minute % 1 == 0 and second == 00):
        for a in main.keys():
            df = pd.DataFrame(pdr.get_data_yahoo(a, period='1d', interval = '1m'))
            close_price = pd.Series(df['Close'])[-1]
            t = pd.Series(df.index)
            signal = analysis.moving_average(data=df)
            print(signal)
            if signal == 'buy':
                main[a].long(close_price)
            elif signal == 'sell':
                main[a].short(close_price)
            main[a].display()
            Log.insert(a, [t[t.size-1],close_price,signal,main[a].d['P&L']],folder)
        if(hour == 15 and minute >= 29):
            for a in main.keys():
                main[a].square_off(close_price)
                f = False
                break
    time.sleep(1)