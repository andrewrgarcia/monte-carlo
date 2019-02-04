# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:53:22 2019

@author: garci
"""
'''mc_simple.py - A template for SIMPLE monte carlo simulations
Andrew Garcia'''

import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import tstd, variation

def bellgen(N=1000,var1_mean=165,var1_sd=2,var2_mean=1,var2_sd=0.1):

    def model(var1_mean=var1_mean,var1_sd=var1_sd,var2_mean=var2_mean,var2_sd=var2_sd):
        'pick 2 numbers from a probability distribution:'
        var1 = random.gauss(var1_mean, var1_sd)
        var2 = random.gauss(var2_mean, var2_sd)

        #factor3= random.uniform(0,50)
        'perform operation with two numbers to create a new value i.e. "effect"'
        effect=(var1)/var2

        return effect


    'iteration: repeat "model" function N times'
    x=np.linspace(0,N,N)
    eff1=np.zeros(N)
    for i in range(0,N):
        eff1[i]=model()
    "you have a new distribution now! eff1"

    'calculate distribution parameters from the N population; mu==mean, sigma==standard dev.'
    eff1_mean=np.mean(eff1)
    eff1_sd=tstd(eff1)
    eff1_variation=variation(eff1)

    '''HISTOGRAMS'''

    # Create the histograms and normalize the total count to 1

    histret, binsret = np. histogram(eff1, bins = 100)
    histret = [ float(n)/sum(  histret) for n in   histret]

    '''HISTOGRAMS (plotting)'''
    center = (binsret[:-1]+binsret[1:])/2
    width = 1*(binsret[1]-binsret[0])

    plt.figure(1)
    plt.bar(center,   histret, align = 'center', width = width,color='blue')
    #plt.text(0.040,25,r"$\mu_{Effect}$"+str(round(eff1_mean),2))
    #plt.text(0.035,25,r"$\sigma_{Effect}$"+str(round(eff1_sd),2))
    plt.show()
    '''point plot: all "effect" values made from "model'''
    plt.figure(2)
    plt.plot(x,eff1,'o')

    plt.show()



    print ("effect population", eff1)
    print ("mean effect", eff1_mean)
    print ("standard deviation effect", eff1_sd)
    print ("variation effect", eff1_variation)


bellgen()
