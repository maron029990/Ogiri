# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 19:04:29 2018

@author: 010180079
"""

import serial
import time

def func_init(ser):
    
    data="#M0"
    ser.write(bytes(data, 'UTF-8')) # 前進
    time.sleep(1)
    
    data="#X"
    ser.write(bytes(data, 'UTF-8'))
    

    
def func_taiki(ser):
    data="#M0"
    ser.write(bytes(data, 'UTF-8')) # 前進
    time.sleep(2)
    
    data="#M5"
    ser.write(bytes(data, 'UTF-8')) 
    
    time.sleep(5)
    
    data="#M0"
    ser.write(bytes(data, 'UTF-8'))
    
    time.sleep(4)
    
    data="#X"
    ser.write(bytes(data, 'UTF-8'))
     

def func_think(ser):
    data="#M0"
    ser.write(bytes(data, 'UTF-8')) # 前進
    time.sleep(2)
    
    data="#M6"
    ser.write(bytes(data, 'UTF-8')) 
    
    time.sleep(5)
    
    data="#M0"
    ser.write(bytes(data, 'UTF-8'))
    
    time.sleep(4)
    
    data="#X"
    ser.write(bytes(data, 'UTF-8'))
    


def func_hirameki(ser):

    data="#M0"
    ser.write(bytes(data, 'UTF-8')) # 前進
    time.sleep(2)
    
    data="#M7"
    ser.write(bytes(data, 'UTF-8')) 
    
    time.sleep(5)
    
    data="#M0"
    ser.write(bytes(data, 'UTF-8'))
    
    time.sleep(4)
    
    data="#X"
    ser.write(bytes(data, 'UTF-8'))
    
def func_ans(ser):

    data="#M0"
    ser.write(bytes(data, 'UTF-8')) # 前進
    time.sleep(2)
    
    data="#M8"
    ser.write(bytes(data, 'UTF-8')) 
    
    time.sleep(5)
    
    data="#M0"
    ser.write(bytes(data, 'UTF-8'))
    
    time.sleep(4)
    
    data="#X"
    ser.write(bytes(data, 'UTF-8'))
    
def func_thank(ser):

    data="#M0"
    ser.write(bytes(data, 'UTF-8')) # 前進
    time.sleep(2)
    
    data="#M9"
    ser.write(bytes(data, 'UTF-8')) 
    
    time.sleep(5)
    
    data="#M0"
    ser.write(bytes(data, 'UTF-8'))
    
    time.sleep(4)
    
    data="#X"
    ser.write(bytes(data, 'UTF-8'))
    

         