import serial
import time

def func():
    ser = serial.Serial('COM3', 57600, timeout = 10)
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
    
    ser.close()        