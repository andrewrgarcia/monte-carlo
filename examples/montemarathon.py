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


'bad runners - probabilities for injuries / exhaustion high '
probs_run = [0.40, 0.40, 0.01]
v_run = 12.5        #speed, miles per hour

'better runners - probabilities for injuries / exhaustion reduced'
#probs_run = [0.20, 0.30, 0.01]
#v_run = 12.5        #speed, miles per hour

'joggers probabilities all the same whether good or bad'
probs_jog = [0.01, 0.00001, 0.00001]
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


'MONTE CARLO ALGORITHMS FOR RACE CONTESTANTS'

'pure runners - ran entire race'
def runner(L):
        
    'clock starts @ time t = 0 min and distance k = 0 miles'    
    k, t, blisters = 0, 0, False

    while k < L:
        k,t,blisters = out(k,t,probs_run,v_run,blisters)
    return k,t
    
'pure joggers - jogged entire race'
def jogger(L):
    
    'clock starts @ time t = 0 min and distance k = 0 miles'    
    k, t, blisters = 0, 0, False
    
    while k < L:
        k,t,blisters = out(k,t,probs_jog,v_jog,blisters)
    return k,t
    
'runner-joggers - alternated between running and jogging'
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
    
'--------------------------------------------------------------------------'
'1st 2nd or 3rd place'
def race_places(L):

    dr,tr = runner(L)
    dj,tj = jogger(L)

    drj,trj = rj_int(L)
    
    times = [tr,tj,trj]
    order = list(np.sort(times))
    
    places = [order.index(times[0]),order.index(times[1]),order.index(times[2])]

    return places


def assign_places(L,rers1st, jers1st, rjers1st,rers2nd, jers2nd, \
                  rjers2nd,rers3rd, jers3rd, rjers3rd):

    run,jog,runjog=race_places(L)

    rers1st.append(1 if run == 0 else 0)
    jers1st.append(1 if jog == 0 else 0)
    rjers1st.append(1 if runjog == 0 else 0)
    
    rers2nd.append(1 if run == 1 else 0)
    jers2nd.append(1 if jog == 1 else 0)
    rjers2nd.append(1 if runjog == 1 else 0)
    
    rers3rd.append(1 if run == 2 else 0)
    jers3rd.append(1 if jog == 2 else 0)
    rjers3rd.append(1 if runjog == 2 else 0)

    R1st, J1st, RJ1st = np.sum(rers1st),np.sum(jers1st),np.sum(rjers1st)
    R2nd, J2nd, RJ2nd = np.sum(rers2nd),np.sum(jers2nd),np.sum(rjers2nd)
    R3rd, J3rd, RJ3rd = np.sum(rers3rd),np.sum(jers3rd),np.sum(rjers3rd)
    
    return R1st, J1st, RJ1st, R2nd, J2nd, RJ2nd, R3rd, J3rd, RJ3rd 

'ITERATIONS'

def fast_iters(N):
    L = 26.2    #miles

    j = 0
    rers1st, jers1st, rjers1st = [],[],[]
    rers2nd, jers2nd, rjers2nd = [],[],[]
    rers3rd, jers3rd, rjers3rd = [],[],[]

    while j < N:
        R1st, J1st, RJ1st, R2nd, J2nd, RJ2nd, R3rd, J3rd, RJ3rd = \
        assign_places(L,rers1st, jers1st, rjers1st, \
                      rers2nd, jers2nd, rjers2nd, rers3rd, jers3rd, rjers3rd)
        j+=1
    
    print('Results {} Marathon races'.format(j))
    print('Runners: \n1st place {0}({3}%)\n2nd place {1}({4}%) \
          \n3rd place {2}({5}%)'.\
          format(R1st,R2nd,R3rd,R1st*100/j,R2nd*100/j,R3rd*100/j))
    
    print('\nJoggers: \n1st place {0}({3}%)\n2nd place {1}({4}%) \
          \n3rd place {2}({5}%)'.\
          format(J1st,J2nd,J3rd,J1st*100/j,J2nd*100/j,J3rd*100/j))
    
    print('\nRunner-Joggers: \n1st place {0}({3}%)\n2nd place {1}({4}%) \
          \n3rd place {2}({5}%)'.\
          format(RJ1st,RJ2nd,RJ3rd,RJ1st*100/j,RJ2nd*100/j,RJ3rd*100/j))

print(fast_iters(1000))

        
def dyn_bar(N):
    L = 26.2    #miles

    j = 0
    rers1st, jers1st, rjers1st = [],[],[]
    rers2nd, jers2nd, rjers2nd = [],[],[]
    rers3rd, jers3rd, rjers3rd = [],[],[]

    while j < N:

        plt.clf()
        
        R1st, J1st, RJ1st, R2nd, J2nd, RJ2nd, R3rd, J3rd, RJ3rd = \
        assign_places(L,rers1st, jers1st, rjers1st, \
                      rers2nd, jers2nd, rjers2nd, rers3rd, jers3rd, rjers3rd)
        
        
        x=[0, 1, 2]
        y = [R2nd,R1st,R3rd]
        
        x2=[4,5,6]
        y2 = [J2nd,J1st,J3rd]
#        
        x3 = [8,9,10]
        y3 = [RJ2nd,RJ1st,RJ3rd]
    
        j+=1

        plt.bar(x,y,0.8,label='running')
        plt.bar(x2,y2,0.8,label='jogging')
        plt.bar(x3,y3,0.8,label='run-jog intervals')

        
        plt.legend(prop={'size': 13})
        plt.ylim(0,N*1.3)
        plt.suptitle('Marathon results',size =13)
        plt.title('{} marathon contests simulated'.format(j),size=13)
        plt.xticks([0,1,2,4,5,6,8,9,10],['2nd','1st','3rd']*3,size=13)


        plt.pause(0.000001)
        
    plt.text(0-.5,R2nd+1,'{} %'.format(np.round(R2nd*100/j,2)),size=14)
    plt.text(1-.5,R1st+1,'{} %'.format(np.round(R1st*100/j,2)),size=14)
    plt.text(2-.5,R3rd+1,'{} %'.format(np.round(R3rd*100/j,2)),size=14)

    plt.text(4-.5,J2nd+1,'{} %'.format(np.round(J2nd*100/j,2)),size=14,color='blue')
    plt.text(5-.5,J1st+1,'{} %'.format(np.round(J1st*100/j,2)),size=14,color='blue')
    plt.text(6-.5,J3rd+1,'{} %'.format(np.round(J3rd*100/j,2)),size=14,color='blue')
    
    plt.text(8-.5,RJ2nd+1,'{} %'.format(np.round(RJ2nd*100/j,2)),size=14,color='magenta')
    plt.text(9-.5,RJ1st+1,'{} %'.format(np.round(RJ1st*100/j,2)),size=14,color='magenta')
    plt.text(10-.5,RJ3rd+1,'{} %'.format(np.round(RJ3rd*100/j,2)),size=14,color='magenta')

dyn_bar(100)
