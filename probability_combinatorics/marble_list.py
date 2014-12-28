"""
Two things:
1. Figuring out the probability of picking out a particular marble ball out of a  bag of balls of different colors.

2. Figuring out the probability of randomly picking a non-blue marble from the bag.
"""

from random import choice
from matplotlib import pyplot as plt

marble_list = {'blue':2, 'red':9, 'green':3}

def list_trial(max_side, times, m_list, steps = 1, *trial_side):
    """
    max_side: maximum number of possibilities
    times: total number of trials to play
    m_list: the list or bag of choices under observation!
    trial_side: The expected outcome(s)

    returns:
    out_p: the total probability out of the trial "times"
    outcome_times: total occurences
    mathematical - out_p: difference between mathematical-probability and total probability out of the trial "times"
    """
    outcome_times = 0.
    out_p = 0.
    steps = 1 if (steps>=times) else steps

    #print trial_side
    mathematical = [float(m_list[sides])/max_side for sides in trial_side]
    bag = reduce(lambda x,y: (x+y), ([k]*v for k,v in m_list.iteritems()))

    for _ in xrange(0, times, steps):
        out = choice(bag)
        if out in trial_side:
            outcome_times += 1
    out_p += float(outcome_times)/times

    return out_p, outcome_times, [m - out_p for m in mathematical]


if __name__ == "__main__":
    #func - list_trial(max_side, times, m_list, *trial_side, steps = 1)

    times = 1000

    #solve 1
    plt.plot(xrange(times), [list_trial(sum(marble_list.values()), i, marble_list, 1, 'red')[0] for i in xrange(1,times+1)])

    #difference between mathematical and actual outcomes as trials increase should diminsh
    plt.plot(xrange(times), [list_trial(sum(marble_list.values()), i, marble_list, 1, 'red')[2][0] for i in xrange(1,times+1)])

    #solve 2
    plt.plot(xrange(times), [list_trial(sum(marble_list.values()), i, marble_list, 1, 'red', 'green')[0] for i in xrange(1,times+1)])
