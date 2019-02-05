'''mclotstrats.py: A simple Monte Carlo algorithm for the design of lottery games
Developed using Pythonista for iPhone/iPad
(c) Andrew R Garcia, 2017

*Lottery customization: no. of draws (draws) in lottery; lowest (low) and highest (high) numbers in lottery
*Game customization: number of lotteries played (N); 
number of tickets played (ticketN) per N lottery
'''

import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def mcG(N=100,draws=5,low=1,high=30,ticketN=5):
  #developer: Andrew Garcia
  #with plt.xkcd():
  x=np.linspace(0,N,N)

#  L_draw=sample(draws,low,high)
  drawrange=range(low,high+1)
  ticket=np.zeros([ticketN,draws])
  ticketcorr=np.zeros([ticketN,draws])
  for p in range(0,ticketN):
    ticket[p]=random.sample(drawrange,draws)
# lottery numbers for tickets bought
    ticketcorr[p]=np.sort(ticket[p])


  sum_winners=np.zeros(N)

  for j in range(0,N):

#    player_game=sample(draws,low,high)
    winners=np.zeros(ticketN)
    drawrange=range(low,high+1)
    L_draw=random.sample(drawrange,draws)
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
  print ('investment for $1 lottery(ies): $', N*ticketN*1)

  plt.xlim(-1,1.5)

  plt.suptitle(r' \$1e+06 Lottery - number of draws: {}; draw range: ({}-{})'.format(draws,low,high))
  plt.title('investment @ \$1/ticket: $ {:.2e}'.format(N*ticketN*1))
  
  plt.text(-0.2,N-grandsum_winners,'{}'.format(N-grandsum_winners))
  plt.text(1- 0.125,grandsum_winners,'{}'.format(grandsum_winners))
  xax=[-0.2, 1- 0.125]
  y=[N-grandsum_winners,grandsum_winners]
  plt.bar(xax,y,0.5)
  plt.xticks(xax,['lose','win'])

  plt.show()

  #plt.clf()
  #plt.cla()
  #plt.close()

mcG(N=400,ticketN=2000)