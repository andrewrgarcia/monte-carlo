'''mclotstrats.py: A simple Monte Carlo algorithm for lottery games
Developed using Pythonista for iPhone/iPad
(c) Andrew R Garcia, 2017

*Lottery customization: no. of balls (balls) in lottery; lowest (low) and highest (high) numbers in lottery
*Game customization: number of lotteries played (N); number of tickets played (ticketN) per N lottery
'''

import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def mcG(N=100,balls=4,low=1,high=30,ticketN=5):
  #developer: Andrew Garcia
  #with plt.xkcd():
  x=np.linspace(0,N,N)

#  L_draw=sample(balls,low,high)
  ballpop=range(low,high+1)
  ticket=np.zeros([ticketN,balls])
  ticketcorr=np.zeros([ticketN,balls])
  for p in range(0,ticketN):
    ticket[p]=random.sample(ballpop,balls)
# lottery numbers for tickets bought
    ticketcorr[p]=np.sort(ticket[p])


  sum_winners=np.zeros(N)

  for j in range(0,N):

#    player_game=sample(balls,low,high)
    winners=np.zeros(ticketN)
    ballpop=range(low,high+1)
    L_draw=random.sample(ballpop,balls)
    L_drawsort=np.sort(L_draw)
    print('lottery draw #{}: {}'.format(j+1,L_draw))
    for i in range(0,ticketN):
      if np.array_equal(ticketcorr[i],L_drawsort)==True:
        winners[i]=1
      else:
        winners[i]=0

    sum_winners[j]=np.sum(winners)
  grandsum_winners=np.sum(sum_winners)
  
  print('____________________________________________________')
  print ('number of times played: ', N)
  print ('tickets bought per played lottery: ', ticketN)
  print ('winning tickets: ',ticket)
  print ('lottery winning timeline: ',sum_winners)
  print ('# times won: ',grandsum_winners)
  print ('investment for $1 lottery: $', N*ticketN*1)

  plt.ylabel("winning tickets")
  plt.xlim(-0.2,N+0.2)
  #plt.ylim(-0.2)
  plt.xlabel("Lottery timeline")
  plt.title("Lottery Draw")

  plt.plot(x,sum_winners,'o',color='magenta')
  plt.show()

  #plt.clf()
  #plt.cla()
  #plt.close()
