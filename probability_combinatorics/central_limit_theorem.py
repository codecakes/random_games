"""If I had to demo someone Central Limit Theorem,
this is what it looks like.
Simulate a die roll 100 times.
If you take its histogram it will be almost uniform
since 1/6 chance for every die face to be on top.
Take out each simulations mean a 1000 times and  you see a central trend."""

from matplotlib.pyplot import hist

#a die
s = xrange(1,7)

#take random trials 100 rolls. take their MEAN and repeat this experiment 1000 times
print hist([mean([random.choice(s) for _ in xrange(100)]) for _ in xrange(1000)], bins=7)

#or
#roll dice twice.repeat 1000 times
r2=[mean([random.choice(s) for _ in xrange(2)]) for _ in xrange(1000)]

#roll dice frice(u know hw mny times).repeat 1000 times
r5=[mean([random.choice(s) for _ in xrange(5)]) for _ in xrange(1000)]


print hist(r2)

#skinnier distribution.thinner tails.
print hist(r5)

"""thats because of this: Increasing sample size inversely decreases Sample Standard Deviation OR Standard Error.
std(xrange(1,7))/sqrt(5)
Out[158]: 0.76376261582597327

std(xrange(1,7))/sqrt(2)
Out[159]: 1.2076147288491197
"""
