# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:05:27 2019

@author: garci
"""
import matplotlib.pyplot as plt
import random as ran
import numpy as np

def dist(n):
    sigma=0.5
    plt.figure()
#    plt.clf()
    x=np.linspace(-5,5,500)
    P=(1/np.sqrt(2*np.pi*sigma**2))*exp((-x**2)/(2*sigma)**2)
    plt.ylabel('P(x)',size=13)
    plt.xlabel('x',size=13)
    plt.plot(x,P,linewidth=2,color='gold')
    plt.show()
    
    k=0
    while k < n:
        
        xs = ran.uniform(-5,5)
        ys = ran.uniform(0,1)
        Pxs = (1/np.sqrt(2*np.pi*sigma**2))*exp((-xs**2)/(2*sigma)**2)
        if Pxs > ys:
            plt.scatter(xs,ys,color='m')
        else:
            plt.scatter(xs,ys,color='k')
        plt.title('{} samples'.format(k+1))
            
#        plt.pause(0.00001)
        k+=1

dist(2000)

def singval(n):
    plt.figure()
#    plt.clf()
    x=np.linspace(-5,5,500)
    P=0.40
    plt.ylabel('P',size=13)
    plt.xlabel("doesn't matter",size=13)
    plt.hlines(P,-5,5)
    plt.show()
    
    k=0
    while k < n:
        
        xs = ran.uniform(-5,5)
        ys = ran.uniform(0,1)
        Pxs = 0.4
        if Pxs > ys:
            plt.scatter(xs,ys,color='blue')
        else:
            plt.scatter(xs,ys,color='darkorange')
        plt.title('{} samples'.format(k+1))
#        plt.pause(0.00001)
        k+=1
        
#singval(2000)