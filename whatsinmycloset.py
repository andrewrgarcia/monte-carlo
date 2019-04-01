# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:45:11 2019

@author: garci
"""

import random as ran
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import tstd, variation

def shoes(n,lowbound,upbound):
    
    k=0
    cost = []
    while k < n:
        cost.append(ran.uniform(lowbound,upbound))
        k+=1
    return cost

def clothes(n,mean,sdev,cutoff):
    
    k=0
    cost = []
    while k < n:
        sample=ran.gauss(mean,sdev)
        'cutoff (shirts cannot be cheaper than $[cutoff value] )'
        cost.append(sample) if sample >=cutoff else cost.append(5)
        k+=1
    return cost


def single(show='off'):
    
    nboots,nsand,ndr,nsh,npnt = 10,3,12,15,8
    x= range(sum((nboots,nsand,ndr,nsh,npnt)))
    
    'closet items'
    boots = shoes(nboots,40,120)
    sandals = shoes(nsand,2,10)
    dresses = clothes(ndr,mean=80,sdev=10,cutoff=50)
    shirts = clothes(nsh,mean=40,sdev=20,cutoff=5)
    pants = clothes(npnt,mean=70,sdev=30,cutoff=20)

    data=concatenate((boots,sandals,dresses,shirts,pants))

    if show == 'on':
        
        'plot density histogram'
        plt.figure()
        plt.scatter(x,data)
        plt.title(r'Closet value (single simulation): $ {}'.format(np.round((sum(data)),2)),size=13)
        plt.ylabel(r"Cost of clothing items  /  $",size=13)
        plt.xlabel('Item number',size=13)

        plt.figure()

        wts = np.ones_like(data) / float(len(data))
        plt.hist(data, stacked =True, weights=wts,edgecolor='k')
        plt.title(r'Closet value: $ {}'.format(np.round((sum(data)),2)),size=13)
        plt.xlabel(r"Cost of clothing items  /  $",size=13)
        plt.ylabel('P',size=13)
        plt.show()
        
        '2nd plot'
        total = sum(data)
        plt.figure()
#        wts = np.ones_like(total) 
        plt.hist(total, stacked =True,edgecolor='k',color='darkorange')
        plt.suptitle('<Closet value>: $ {}'.\
                     format(total),size=13)
    
    return sum(data)

#single('on')

def iters(N):
    
    i=0
    simulations = []
    while i < N:
        ith_iter = single('off')
        simulations.append(ith_iter)
        print('$',ith_iter)
        i+=1
        
    data=simulations

    'plot density histogram'
    plt.figure()
    wts = np.ones_like(data) / float(len(data))
    plt.hist(data, stacked =True, weights=wts,edgecolor='k',color='darkorange')
    average=int(np.mean(data))
    plt.suptitle('<Closet value>: $ {} +- {} (std. dev.)'.\
                 format(average,int(tstd(data))),size=13)

    plt.xlabel(r"Total closet values for {} simulation(s)  /  $".format(N),size=13)
    plt.ylabel('P',size=13)
    plt.show()
    
iters(10000)

