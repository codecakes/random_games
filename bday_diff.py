#This is what I call a close to good enough program design. satisfied.
#author: @codecakes; maintainer: @codecakes

month_day = dict(zip(range(1,13), [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
leap = lambda yy: (yy%4 == 0 and not (yy%100 == 0)) \
                    or (yy%4 == 0 and yy%100 == 0 and yy%400==0)

def month_days(month, leap=False):
    '''Returns the number of days in the month'''
    assert 1 <= month <=12
    return month_day[month] if month != 2 \
                            else month_day[month] + (1 if leap else 0)

def nextDay(year, month, day):
    """
    ###
    ### Define a simple nextDay procedure, that assumes
    ### every month has 30 days.
    ###
    ### For example:
    ###    nextDay(1999, 12, 30) => (2000, 1, 1)
    ###    nextDay(2013, 1, 30) => (2013, 2, 1)
    ###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
    ###
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    next_year = year
    next_month = month
    next_day = day
    is_leap = False
    #consider the leap year and month case
    if month == 2 and leap(year):
        is_leap = True
        #month_days[2] = 29
    #get total days in current month
    cur_month_days = month_days(month, is_leap)
    #print "cuurent month days {}".format(cur_month_days)
    #if the next day exceeds total days in the month
    #rollover next date
    if day + 1 > cur_month_days:
        #by checking if next month is valid
        if month+1 > 12:
            #rollover to next year total months overflow
            next_year += 1
            #next year starts with 1st month
            next_month = 1
        else:
            #else increment next month
            next_month += 1
        #set the first day of next month
        next_day = 1
    else:
        #else increment to next day
        next_day += 1
    #set the default non leap year configuration back
    #month_days[2] = 28
    return(next_year, next_month, next_day)

assert nextDay(1999, 12, 30) == (1999, 12, 31)
assert nextDay(2013, 1, 30) == (2013, 1, 31)
assert nextDay(2012, 12, 30) == (2012, 12, 31)
assert nextDay(2012, 2, 28) == (2012, 2, 29)

def dataIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2: return True
    elif year1 == year2:
        if month1 < month2: return True
        if month1 == month2:
            if day1 < day2:
                return True
    return False
        

def calcYr1(year1, month1, day1):
    total_days = 0
    is_leap = False
    if leap(year1):
        #month_days[2] = 29
        is_leap = True
    #rest days of that month
    total_days += month_days(month1, is_leap) - day1
    #total days from rest of the months in first year
    for month in xrange(month1+1, 13):
        total_days += month_days(month, is_leap) #month_days[month]
    #month_days[2] = 28
    return total_days

assert calcYr1(2013,1,1) == 364
assert calcYr1(2013,1,2) == 363

def calcYr2(year2, month2, day2):
    total_days = 0
    is_leap = False
    if leap(year2):
        #month_days[2] = 29
        is_leap = True
    #total days from all months before end month of last year
    for month in xrange(1, month2):
        total_days += month_days(month, is_leap) #month_days[month]
    #all days till day2 of end month
    total_days += day2
    #month_days[2] = 28
    return total_days

assert calcYr2(2013,1,1) == 1
assert calcYr2(2013,1,2) == 2
assert calcYr2(2013,2,1) == 32
assert calcYr2(2013,2,2) == 33

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    if dataIsBefore(year1, month1, day1, year2, month2, day2):
        total_days = 0
        #if same year, iterate through nextDays and increment
        if year1 == year2:
            yy, mm, dd = year1, month1, day1
            while dataIsBefore(yy, mm, dd, year2, month2, day2):
                yy, mm, dd = nextDay(yy, mm, dd)
                total_days += 1
        else:
            #else add all days between start and end year       
            for yy in xrange(year1+1, year2):
                total_days += 365 if not leap(yy) else 366
            #add first year days and end year days to it
            total_days += calcYr1(year1, month1, day1) + \
                            calcYr2(year2, month2, day2)
        #print "total days %s" %total_days
        return total_days
    return -1

if __name__ == "__main__":
    from cProfile import run
    
    def test_diff():
        test_cases = [((2012,9,30,2012,10,30),30), 
                    ((2012,1,1,2013,1,1),366),
                    ((2012,1,1,2013,1,2),367),
                    ((2012,9,1,2012,9,4),3),
                    ((2012,1,1,2012,2,28), 58), 
                    ((2012,1,1,2012,3,1), 60),
                    ((2011,6,30,2012,6,30), 366),
                    ((2011,1,1,2012,8,8), 585 )]
        
        for (args, answer) in test_cases:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
    
    test_diff()
    
    #print daysBetweenDates(1900,1,1,2013,1,1)
    #print daysBetweenDates(1900,1,1,2013,1,2)
    #print daysBetweenDates(1900,1,1,2013,1,3)
    run("daysBetweenDates(1900,1,1,2013,1,1)")