#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:26:08 2022

@author: home
"""

import numpy as np
from matplotlib import pyplot as plt

#---------------------Neutral Drift--------------------------------

# simulating n times  a neutral drift in a population of size N, with an allele A in initial frequency i/N in tmax time
# we are supposing a small mutation rate, so no other mutants can arise during the simulation

def main():
    #defining parameters
    N=40
    i=4
    tmax=1000
    n=10
    #calling function
    neutral_drift_graph(N, i, tmax, n)
        
    
def neutral_drift(N, i, tmax):
    cura=i
    a=[i/N]
    curt=0
    t=[0]
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
        t.append(curt)
        a.append(cura/N)
    #plotting the amount of A individual per time
    plt.plot(t,a)
    
    
def neutral_drift_graph(N, i, tmax, n):
    #plotting n times the genetic drift
    for j in range (n):
        neutral_drift(N, i, tmax)
    plt.title("Stochastic Simulations of Neutral Drift in a Population with %d Individuals"%N)
    plt.xlabel('time')
    plt.ylabel('frequency of the A allele in the population')
    plt.ylim([0,1])
    ## saving the graph in a known subdirectory figs
    plt.savefig('figs/simulationsgraph.png')

main()

    