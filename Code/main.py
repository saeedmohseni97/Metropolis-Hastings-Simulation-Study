# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## Importing required packages and methods
import sys
sys.path.append('Functions')
from MH_nt import MH_n2t, MH_t2n, MH_n2t_2
import pickle

## parameters:
num_iter = [10, 100, 1000, 10000]
df = [2, 5, 10, 20]
Sample = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

## Algorithm
functions = [MH_n2t, MH_n2t_2, MH_t2n]
Names = ["MH_n2t", "MH_n2t_2", "MH_t2n"]
count = 0
for func in functions:
    for i in range(len(num_iter)):
        for j in range(len(df)):
            Sample[j][i] = func(num_iter[i], df[j], 1)
    
    with open(f'../Results/{Names[count]}_samples.pkl', 'wb') as f:
        pickle.dump(Sample, f)
    count = count + 1   




