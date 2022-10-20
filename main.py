from array import array
import random
import time

def load_data():
    data_aray = []
    
    
    for i in range(10):
        column_aray = []
        for j in range(4):
            column_aray.append(random.randint(0,9))
            data_aray.append(column_aray)
            
    print(data_aray)
    
load_data()