# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:31:35 2022

@author: KRISHNA_CHAITANYA
"""

class Position:
    def __init__(self):
        self.d = {'position':None, 'price':0, 'P&L':0}
    
    def display(self):
        print('position :', self.d['position'])
        print("p & l :",self.d['P&L'])
        
    def long(self,price):
        if self.d['position'] == True:
            return
        if self.d['position'] == False:
            Position.square_off(self, price)
        self.d['position']= True
        self.d['price'] = price
    
    def short(self,price):
        if self.d['position'] == False:
            return
        if self.d['position'] == True:
            Position.square_off(self, price)
        self.d['position'] = False
        self.d['price'] = price
        
    def square_off(self,price):
        if self.d['position'] == None:
            return
        if self.d['position'] == True:
            self.d['position'] = None
            self.d['P&L'] += price - self.d['price']
            self.d['price'] = price
            
        elif self.d['position'] == False:
            self.d['position'] = None
            self.d['P&L'] += self.d['price'] - price
            self.d['price'] = price
        Position.display(self)
   
            
            