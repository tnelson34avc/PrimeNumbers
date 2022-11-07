# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 18:38:13 2022

@author: nelso

Title: prime numbers
Status: completed
"""
#prime numbers

msize = 1000
import numpy as np
lst = np.arange(1,msize).tolist()
primelst = []

#def factors()
rmax = (int)(msize/2 +1)

for x in range(1,msize+1):
    num_factors = 0
    loops= 0
    for y in range(1,msize+1):
        
        result = x / y
        
        if result == (int)(result):
            print(f"{result} = {x} / {y}")
            r = (int)(result)
            num_factors = num_factors+1
            print(f"{result} == {r} : {num_factors}\n")
        if num_factors>=3:
            break
        elif num_factors<3 and loops==msize-1:
            primelst.append(x)
        loops+=1
print(primelst)
            
