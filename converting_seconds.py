# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(secs):
    hh, mm = secs/3600, secs%3600
    mm, ss = mm/60, mm%60
    hh = round(hh, 1)
    mm = round(mm, 1)
    ss = round(ss, 1)
    return "{} {}, {} {}, {} {}".format(\
                                        int(hh) if hh == int(hh) else hh, "hours" if (hh > 1 or hh==0) else "hour", \
                                        int(mm) if mm == int(mm) else mm, "minutes" if (mm > 1 or mm==0) else "minute", \
                                        int(ss) if ss==int(ss) else ss, "seconds" if (ss > 1 or ss==0) else "second" \
                                        )

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(3600)
#>>>```1 hour, 0 minutes, 0 seconds```