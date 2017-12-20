#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:47:23 2017

@author: ram
"""

import numpy as np

inp = np.zeros(52*4)
a = [33, 38, 45, 15]

def popinp(inp_list, inp):
    for idx, val in enumerate(inp_list):
        newidx = val + idx * 52 - 1
        #print(idx, val, newidx)
        inp[newidx] = 1
    nz = np.nonzero(inp)
    #print("nonzero ", nz)
    
#popinp(a, inp)

#inp = np.zeros(52*4)
#b = [52, 52, 52, 52]
#popinp(b, inp)

#inp = np.zeros(52*4)
#b = [1, 1, 1, 1]
#popinp(b, inp)

#inp = np.zeros(52)
#b = [39]
#popinp(b, inp)

import json
from pprint import pprint

#with open('nums60k.json') as data_file:    
with open('randmap60k.json') as data_file:    
    data = json.load(data_file)
#pprint(data)
inp_lst = []
oup_lst = []
for item in data[:50000]:
    x = item[:4]
    y = [item[4]]
    inp = np.zeros(52*4)
    popinp(x, inp)
    oup = np.zeros(52)
    popinp(y, oup)
    inp_lst.append(inp)
    oup_lst.append(oup)
    clue = item[5]
    myst = item[6]
    #print(x, y, clue, myst)

training_inputs = [np.reshape(x, (208, 1)) for x in inp_lst]
training_results = [np.reshape(y, (52, 1)) for y in oup_lst]
train = zip(training_inputs, training_results)

#train = zip(inp_lst, oup_lst)
#print("all_data", all_data)
print("data[0]", data[0])
print("data[49999]", data[49999])
print("data[50000]", data[50000])
print("data[59999]", data[59999])




inp_lst = []
oup_lst = []
for item in data[-10000:]:
    x = item[:4]
    y = item[4] - 1
    inp = np.zeros(52*4)
    popinp(x, inp)
    inp_lst.append(inp)
    oup_lst.append(y)
    clue = item[5]
    myst = item[6]
  
    
inp_arr = np.array(inp_lst)
oup_arr = np.array(oup_lst)

test_inputs = [np.reshape(x, (208, 1)) for x in inp_arr]
test = zip(test_inputs, oup_arr)
