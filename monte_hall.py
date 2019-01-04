# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:57:22 2019

@author: garci
"""
import random as ran
import matplotlib.pyplot as plt
'''monte_hall.py - Simulations elucidating the Monte Hall problem. Solutions
in concordance with Marilyn vos Savant's argument.

Andrew Garcia, 2019'''

plt.xkcd()
doors = ['car','goat','goat']


def monty(doors,k_c):
    k = 0
    while doors[k] != 'goat' or k == k_c:        
        k=ran.randint(0,2)
        

    return doors[k],k


def game():
    random.shuffle(doors)
    
    'contestant chooses door but choice is not revealed to him'
    ind_c = ran.randint(0,2)
    door_choice = doors[ind_c]
    
    print(door_choice, ind_c)
    
    'monty shows door with goat to contestant, this is what is seen:'
    doors_revealed = ['closed door']*3
    str_goat, ind_goat = monty(doors,ind_c)
    doors_revealed[ind_goat] = str_goat
    doors_revealed[ind_c] = 'door opened'
    
    'change door after shown the door w/ goat'
    ind_swap = doors_revealed.index('closed door')
    
    final_choice = doors[ind_swap]
    
    print(doors_revealed)
    print(final_choice)
    print()
    
    plt.clf()
    m_size=20
    plt.plot(ind_goat,0,'ko',markersize=m_size,label='goat')
    if final_choice == 'car':
        plt.plot(ind_c,0,'s',markersize=m_size,label='closed door')
        plt.plot(ind_swap,0,'ro',markersize=m_size,label='car')
    else:
        plt.plot(ind_c,0,'s',markersize=m_size,label='closed door')
        plt.plot(ind_swap,0,'ko',markersize=m_size,label='goat')
    plt.legend()
    plt.xticks([])
    plt.yticks([])

    plt.show()
    plt.pause(0.0001)

    
    return final_choice

def iters():
    car, goat = 0, 0
    for i in range(200):
        if game() == 'car':
            car += 1
        else:
            goat += 1
            
    return [car, goat]

y=iters()
x=[-0.125, 1- 0.125]
plt.figure()
plt.bar(x,y,0.25)
plt.xlim(-0.5,1.5)
plt.title('Outcome after changing doors')
plt.xticks(x,['car','goat'])


    
    
#    index = random.randint(0,2)
    
#    if doors_rev[index] = 'G':
#        choose_again  
