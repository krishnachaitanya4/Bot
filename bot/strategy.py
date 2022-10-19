# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:18:40 2022

@author: KRISHNA_CHAITANYA
"""

import talib as ta
import pandas as pd

class Strategy:
    '''def __init__(self,data):
        self.data = data'''
    def believer(self,data):
        pl = data['Close']
        sma_15 = ta.MA(pl,9)
        sma_30 = ta.MA(pl,21)
        #signal = ''
        if(sma_15[-1] > sma_30[-1]):
            #print("signal = buy")
            return "buy"
        else:
            #print("signal = sell")
            return "sell"
        
    
    
    def trend(data):
        high = data["High"]
        low = data["Low"]
        close = data["Close"]
        real = ta.ADX(high, low, close, timeperiod=14)
        return real[-1]
    
    def moving_average(self,data):
        pl = data['Close']
        ma = ta.MA(pl,9)
        ma2 = ta.MA(pl,36)
        if(ma[-1] > ma2[-1]):
            return "buy"
        if(ma[-1] < ma2[-1]):
            return "sell"
        