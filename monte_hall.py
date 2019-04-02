# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:57:22 2019
@author: garci
"""
import random as ran
import matplotlib.pyplot as plt

from sty import fg, bg, ef, rs
fg.orange = ('rgb', (255, 150, 50))
fg.crimson = ('rgb', (220, 20, 60))
fg.deepskyblue1 = ('rgb', (0,0,200))

from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data

'''monte_hall.py - Simulations elucidating the Monty Hall problem. Solutions
are in concordance with Marilyn vos Savant's argument.

Andrew Garcia, 2019'''

doors = ['car','goat','goat']


def monty(doors,k_c):
    k = 0
    while doors[k] != 'goat' or k == k_c:
        k=ran.randint(0,2)


    return doors[k],k


def imscatter(x, y, image, ax=None, zoom=1):
    'OPTIONAL contest representation (figures)'
    if ax is None:
        ax = plt.gca()
    try:
        image = plt.imread(image)
    except TypeError:
        # Likely already an array...
        pass
    im = OffsetImage(image, zoom=zoom)
    x, y = np.atleast_1d(x, y)
    artists = []
    for x0, y0 in zip(x, y):
        ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
        artists.append(ax.add_artist(ab))
    ax.update_datalim(np.column_stack([x, y]))
    ax.autoscale()
    return artists

def game(trial,animation='off',new='off'):
    '''CORE AlGORITHM'''
    random.shuffle(doors)

    print('Game # ',trial+1)
          
    doors_revealed = ['door']*3
    
    ind_c = ran.randint(0,2)
#    door_choice = doors[ind_c]
    print('*Contestant initially chooses door # {}'.format(ind_c+1))
    doors_revealed[ind_c] = 'first choice'

    print('*Monty shows door with goat and asks \
          contestant: \n"Stay or Switch?"\nContestant switches' )
    str_goat, ind_goat = monty(doors,ind_c)
    doors_revealed[ind_goat] = str_goat
    
    ind_swap = doors_revealed.index('door')
    final_choice = doors[ind_swap]      #<--door identity
    print('*Contestant switches to door # {}'.format(ind_swap+1))
    print('\n{} \n'.format(doors_revealed))
    
    if final_choice == 'car':
        print('*After switch: ' + fg.deepskyblue1 + final_choice + fg.rs +' in door # '+str(ind_swap+1))
        print( fg.deepskyblue1 + 'YOU WON!' + fg.rs )
    if final_choice == 'goat':
        print('*After switch: ' + fg.crimson + final_choice + fg.rs +' in door # '+str(ind_swap+1))
        print( fg.crimson + 'YOU LOST' + fg.rs )
    print('\n')


    
    '''ANIMATION SECTION'''
    if animation == 'on':
        
        if new == 'on':
            imgoat,imcar,imdoor = get_sample_data('goat.png'),\
            get_sample_data('car.png'),get_sample_data('door.png')
            
            fig, ax = plt.subplots()
            
            ax.cla()
        
        else:
            plt.clf()
            m_size=35
        
        if new == 'on':
            imscatter(ind_goat,0, imgoat, zoom=0.6, ax=ax)
            ax.plot(ind_goat,0)
        else:
            plt.plot(ind_goat,0,marker='$goat$',color ='grey',markersize=m_size,label='goat')
            
        if final_choice == 'car':
            if new == 'on':
                imscatter(ind_c,0, imdoor, zoom=0.6, ax=ax)
                ax.plot(ind_c,0)
                imscatter(ind_swap,0, imcar, zoom=0.6, ax=ax)
                ax.plot(ind_swap,0)
                msg = 'you won a car!'
                
            else:
                plt.plot(ind_c,0,'s',color='brown',markersize=m_size,label='door')
                plt.plot(ind_swap,0,marker='$car$',color='red',markersize=m_size,label='car')
                msg = 'you won a car!'
        else:
            if new == 'on':
                imscatter(ind_c,0, imdoor, zoom=0.6, ax=ax)
                ax.plot(ind_c,0)
#                imscatter(ind_swap,0, imgoat, zoom=0.6, ax=ax)
#                ax.plot(ind_swap,0)
                msg = 'you lost'
                

            else:
                plt.plot(ind_c,0,'s',color='brown',markersize=m_size,label='door')
                plt.plot(ind_swap,0,marker='$goat$',color ='grey',markersize=m_size,label='goat')
                msg = 'you lost'
        if new == 'on':
            fig.patch.set_visible(False)
            ax.axis('off')
        else:
            plt.axis('off')
#        plt.legend()
        plt.xticks([])
        plt.yticks([])
        plt.suptitle('The Monty Hall Problem',size =13)
        plt.title('Game # {}: {}'.format(trial+1,msg),size =13)
#        plt.show()
        plt.pause(0.000001)


    return final_choice

def iters(trials):
    car, goat = 0, 0
    for i in range(trials):
        if game(i,'on','off') == 'car':
            car += 1
        else:
            goat += 1

    return [car, goat]

def static_bar(N):
#    N=100
    y=iters(N)
    car,goat = y
    x=[-0.125, 1- 0.125]
    plt.figure()
    plt.text(-0.125,y[0],'{} %'.format(car*100/N),size=15)
    plt.text(1- 0.125,y[1],'{} %'.format(goat*100/N),size=15)
    plt.bar(x,y,0.25)
    plt.xlim(-0.5,1.5)
    plt.suptitle('The Monty Hall Problem - Outcomes',size =13)
    plt.title('{} games simulated'.format(N),size=13)
    plt.xticks(x,['won','lost'],size=15)

static_bar(100)

def dyn_bar(N):
#    N=100
    k=1
    c, g = [],[]
    while k < N:
        plt.clf()
        
        y=iters(1)
        car,goat = y
        x=[-0.125, 1- 0.125]
        k+=1
        c.append(car)
        g.append(goat)
        CAR, GOAT = np.sum(c),np.sum(g)
        z = [CAR,GOAT]
    
    
        plt.text(-0.125,CAR,'{} %'.format(np.round(CAR*100/k,2)),size=15)
        plt.text(1- 0.125,GOAT,'{} %'.format(np.round(GOAT*100/k,2)),size=15)
        plt.bar(x,z,0.25)
        plt.xlim(-0.5,1.5)
        plt.ylim(0,N)
        plt.suptitle('The Monty Hall Problem - Outcomes    (Garcia 2019)',size =13)
        plt.title('{} games simulated'.format(N),size=13)
        plt.xticks(x,['won','lost'],size=15)
        plt.pause(0.000001)
        
#dyn_bar(100)
