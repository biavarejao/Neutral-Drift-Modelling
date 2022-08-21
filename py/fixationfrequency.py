#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:11:04 2022

@author: home
"""

import numpy as np
from matplotlib import pyplot as plt

#------------------Neutral Drift-------------------------------

# simulating neutral drift in a population with size N in a initial frequency i/N of the allele A
# each initial frequency will be runned n times, we consider a fixation (success) if alelle A arrives to 100% until the tmax iteration

def main():
    #defining parameters
    N=50
    iter_i=50
    tmax=1000
    n=100
    #calling function
    frequency(N, iter_i, tmax, n)
    
    
    
def neutral_drift_suc(N, i, tmax,n):
    suc=0
    #simulating n times
    for j in range (n):
        #initial conditions
        cura=i
        curt=0
        while (cura!=N and cura!=0 and curt<tmax):
            ale=np.random.uniform()
            #defining probabilitiy of A reproducing and B dying
            areplace=(cura/N)*((N-cura)/N)
            #defining probabilitiy of B reproducing and A dying
            breplace=((N-cura)/N)*(cura/N)
            #A replace B
            if (ale<areplace):
                cura+=1
            #B replace A
            elif (ale<areplace+breplace):
                cura-=1
            curt+=1
        #if the allele A fixates, success
        if (cura==N):
            suc+=1
    return suc/n

# simulating genetic drift in population of N size in iter_i different initial frequencies of the allele A
def frequency (N, iter_i, tmax, n):
    #defining how the initial frequencies will increase
    pi=int(N/iter_i)
    i=pi
    suc=[]
    ni=[]
    for j in range (iter_i):
        s=neutral_drift_suc(N, i, tmax,n)
        suc.append(s)
        ni.append(i/N)
        i=i+pi
    y=[]
    for i in ni:
        y.append(i)
    #plotting the expected result according to the genetic drift theory
    plt.plot(ni,y, color='c', label='Theoretical result')
    #plotting the "mean" fixation frequencies of each initial frequency of A
    plt.plot(ni,suc, color='deeppink', label='Stochastic Simulations')
    plt.title("Frequency of fixation of A allele in a Population with %d Individuals"%N)
    plt.xlabel('initial frequency of the A allele')
    plt.ylabel('frequency of fixation of the A allele')
    plt.legend()
    
    ## saving the graph in a known subdirectory figs
    plt.savefig('figs/fixationgraph.png')
        
main()
 
