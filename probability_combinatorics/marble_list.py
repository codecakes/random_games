"""
Two things:
1. Figuring out the probability of picking out a particular marble ball out of a  bag of balls of different colors.

2. Figuring out the probability of randomly picking a non-blue marble from the bag.
"""

from random import choice
from matplotlib import pyplot as plt

marble_list = {'blue':2, 'red':9, 'green':3}

def list_trial(max_side, total_times, m_list, steps = 1, *trial_side):
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
    steps = 1 if (steps>=times) else steps
    #print trial_side
    mathematical = [float(m_list[sides])/max_side for sides in trial_side]
    bag = reduce(lambda x,y: (x+y), ([k]*v for k,v in m_list.iteritems()))

    def helper(steps, times, mathematical, bag, *trial_side):
        outcome_times = 0.
        out_p = 0.
        for _ in xrange(0, times, steps):
            out = choice(bag)
            if out in trial_side:
                outcome_times += 1
        out_p += float(outcome_times)/times
        return out_p, outcome_times, [m - out_p for m in mathematical]
    return [helper(steps, i, mathematical, bag, *trial_side) for i in xrange(1,total_times+1)]


if __name__ == "__main__":
    #func - list_trial(max_side, times, m_list, *trial_side, steps = 1)

    times = 1000

    #solve 1
    plt.plot(xrange(times), [ans[0] for ans in list_trial(sum(marble_list.values()), times, marble_list, 1, 'red')])

    #difference between mathematical and actual outcomes as trials increase should diminsh
    plt.plot(xrange(times), [ans[2][0] for ans in list_trial(sum(marble_list.values()), times, marble_list, 1, 'red')])

    #solve 2
    plt.plot(xrange(times), [ans[0] for ans in list_trial(sum(marble_list.values()), times, marble_list, 1, 'red', 'green')])

    #solve 3 probability of even rolls from a 6 sided die in 3 rows
    """done over an average of 1000 times. each time its done 3 times. each time out of 3 times die is rolled iteratively in xrange(3) - 0,1,2"""
    times = 3
    steps = 1
    avg = 0.
    for _ in xrange(1000):
        avg += sum([ans[0] for ans in list_trial(6, times, {i:i for i in xrange(1,7)}, steps, 2,4,6)])/float(times)
    print avg/1000.
    del times, steps, avg
