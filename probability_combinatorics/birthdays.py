from combinatoric import permutation

"""
The probability that at least 2 people in a room of 30 share the same birthday.
P(>= 2 people share the same birth day) = 1 - P(Everyone has a unique birthday)
"""


days = 365
people = 30

print "for %s people" %(people)
unique_bday = permutation(days, people)/(days**people)

print "chances of unique bday is %s" %(unique_bday)
print "chances of 2 or more people sharing their bdays is %s" %(1-unique_bday)

people = 133
print "for %s people" %(people)
unique_bday = permutation(days, people)/(days**people)

print "chances of unique bday is %s" %(unique_bday)
print "chances of 2 or more people sharing their bdays is %s" %(1-unique_bday)
