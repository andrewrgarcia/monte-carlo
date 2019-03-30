# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:42:23 2019

@author: garci
"""

import random as ran
import numpy as np

import matplotlib.pyplot as plt

'''montemarathon.py - acceptance-rejection sampling example:
marathon race
Andrew Garcia, 2019'''


'bad runners'
probs_run = [0.40, 0.40, 0.01]
'better runners'
#probs_run = [0.20, 0.30, 0.01]
'joggers (all the same)'
probs_jog = [0.01, 0.00001, 0.00001]


v_run = 12.5        #speed, miles per hour
v_jog = 6        #speed, miles per hour


def out(k,t,probs,speed,blisters):    
    
    'https://www.verywellfit.com/most-common-marathon-injuries-343573'
    P_cramps, P_bls, P_htw = probs
    '''P_cramps : cramps
    P_bls   : blisters
    P_htw    : "hitting-the wall" (out of energy)       '''
    
    if blisters == True:
        speed -= 3.5
        
    if blisters == False:
        if P_bls > ran.uniform(0,1):
            speed -= 3.5        # speed: miles per hour
            blisters == True
    
    d_r = speed / 60              # miles run in 1 minute
    
    if P_cramps > ran.uniform(0,1):
        k -= d_r             # you lose 1 minute dist.
    
    elif P_htw > ran.uniform(0,1):
        P_gsam = 0.30            #somebody helps out 
        if P_gsam > ran.uniform(0,1):
            k -= 5*d_r    # you lose 5 minutes dist.
        else:
            k -= 20*d_r    # you lose 20 minutes dist.
        
    
    k += d_r        #cover 1 minute distance
    t += 1          #1 minute passes
    
    return k,t,blisters
    

def runner(L):
        
    'clock starts @ time t = 0 min and distance k = 0 miles'    
    k, t, blisters = 0, 0, False

    while k < L:
        k,t,blisters = out(k,t,probs_run,v_run,blisters)
    return k,t
    
    
def jogger(L):
    
    'clock starts @ time t = 0 min and distance k = 0 miles'    
    k, t, blisters = 0, 0, False
    
    while k < L:
        k,t,blisters = out(k,t,probs_jog,v_jog,blisters)
    return k,t
    
'running-jogging intervals'
def rj_int(L):
    
    'lower probability of hitting the wall if alternating:'
    probs = [probs_run, probs_jog]
    v = [v_run, v_jog]
    
    k, t, blisters = 0, 0, False
    while k < L:
        choice = ran.randint(0,1)
        probs_k, v_k = probs[choice], v[choice]
        k,t,blisters = out(k,t,probs_k,v_k,blisters)    
        
    return k,t
    

def race_winner(L):

    dr,tr = runner(L)
    dj,tj = jogger(L)

    drj,trj = rj_int(L)
    
    times = [tr,tj,trj]
    whowon = np.zeros(3)
    winner = times.index(np.min(times))
    whowon[winner] =1

    return whowon


def dyn_bar(N):
    L = 26.2    #miles

    j = 0
    rers, jers, rjers = [],[],[]
    while j < N:

        plt.clf()
        run,jog,runjog=race_winner(L)
        
        x=[-0.125, 0.4, 1- 0.125]

        
        rers.append(run)
        jers.append(jog)
        rjers.append(runjog)

        RUNNER, JOGGER, RJ = np.sum(rers),np.sum(jers),np.sum(rjers)
        y = [RUNNER, JOGGER, RJ]
    
        j+=1
#        print(j)
        plt.text(-0.125,RUNNER,'{} %'.format(np.round(RUNNER*100/j,2)),size=15)
        plt.text(0.4,JOGGER,'{} %'.format(np.round(JOGGER*100/j,2)),size=15)
        plt.text(1- 0.125,RJ,'{} %'.format(np.round(RJ*100/j,2)),size=15)

        plt.bar(x,y,0.25)
#        plt.xlim(-0.5,1.5)
        
        plt.ylim(0,N)
        plt.suptitle('Marathon winners - strategies',size =13)
        plt.title('{} marathon contests simulated'.format(j),size=13)
        plt.xticks(x,['running','jogging','run-jog intervals'],size=15)
        plt.pause(0.000001)
        
dyn_bar(100)

