# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:57:31 2022

@author: KRISHNA_CHAITANYA
"""
import csv
import os

class Log:
    def __init__(self):
        pass
    
    def create_dir(name):
        parent = "D:/bot/logs/"
        pwd = name
        path = os.path.join(parent,pwd)
        if os.path.isdir(path):
            return
        os.mkdir(path)
    def create_file(name,di):
        n = "logs/"+di+"/"+name+".csv"
        with open(n,'w',newline="",encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TIME","PRICE","SIGNAL","P&L"])
            
    def insert(name,values:list(),di):
        n = "logs/"+di+"/"+name+".csv"
        with open(n,'a',newline="",encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(values)
        