#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:39:52 2020

@author: romankosarzycki
"""

import numpy as np

def GaussJordanTest(A,b): #Currently this is specifically being built for a 3x3 matrix
    Aaug=np.column_stack((A, b)) #Once I get this to work, I'll generalize it
    h,w=len(Aaug),len(Aaug[0])
    amax=Aaug[0][0]
    for m in range(0,h): #pivoting for first row
        if Aaug[m][0]>amax:
            Aaug=np.column_stack((A, b))
            Aaug[[m, 0],:] = Aaug[[0, m],:]
    amax=Aaug[1][1]
    for m in range(1,h): #Pivoting for second row
        if Aaug[m][1]>amax:
            Aaug[[m, 1],:] = Aaug[[1, m],:]
    for m in range(1,h): #Thiw will be eq. 41 applied to the second row
        for n in range(0,w):
            Aaug[m][n]=Aaug[m][n]-(Aaug[m][0]/Aaug[0][0])*Aaug[0][n]
    for m in range(2,h): #This will be eq. 43 applied to the second row
        print("This is m:",m)
        for n in range(0,w):
            print("This is n:",n)
            Aaug[m][n]=Aaug[m][n]-(Aaug[m][1]/Aaug[1][1])*Aaug[1][n]
    print(Aaug)
    
def GaussJordan(A,b):
    Aaug=np.column_stack((A, b))
    h,w=len(Aaug),len(Aaug[0])
    for k in range(0,h):
        amax=Aaug[k][k]
        for m in range(k,h):
            if Aaug[m][k]>amax:
                Aaug[[m, k],:] = Aaug[[k, m],:]
        for m in range(k+1,h): #Thiw will be eq. 41 applied to the second row
            for n in range(0,w):
                Aaug[m][n]=Aaug[m][n]-(Aaug[m][k]/Aaug[k][k])*Aaug[k][n]
    print(Aaug)

A=np.array([[1.,2.,3.,13],[4.,5.,6.,14.],[7.,8.,9.,15.],[16.,17.,18.,19.]])
b=np.array([10.,11.,12.,20.])

print(GaussJordan(A,b))