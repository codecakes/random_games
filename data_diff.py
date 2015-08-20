# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
# author: @codecakes
# maintainer: @codecakes

def toprint(string, status=1, *args):
    if status:
        print repr(string) %(args)
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    
    month_days = dict(zip(range(1,13), [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
    leap = lambda yy: (yy%4 == 0 and not (yy%100 == 0)) or (yy%4 == 0 and yy%100 == 0 and yy%400==0)
    
    total_days = 0
    end_month = 12
    end_day = 1
    
    #find remaining days of the start month
    month = month1 if month1 <= end_month else 1
    day = day1 if day1 <= month_days[month] else 1
    total_days += month_days[month] - day
    month = month+1 if month <= end_month else 13
    
    #O(n/~365 + k)     | k <= 24 ~ O(n)
    for yy in xrange(year1, year2 + 1):
        #toprint("Year %s",0, yy)
        if year1 < yy < year2:
            total_days += 365 if not leap(yy) else 366
            continue
        #if leap year
        if leap(yy):
            month_days[2] = 29
            #toprint("Year is a leap year", 0)
        if yy == year2:
            end_month = month2 if month2 <= end_month else 1
            end_day = day2 if day2 <= month_days[end_month] else end_day
            #toprint("This is the last year with ending month %s and ending day %s",0, end_month, end_day)
        #toprint("month - %s and day - %s",0, month, day)
        
        for mm in xrange(month, end_month+1):
            ##sum total days
            if mm == end_month and yy==year2:
                #toprint("month - %s and day - %s", 0, mm, end_day)
                total_days += end_day
                break
            total_days += month_days[mm]
            #toprint("month - %s and day - %s", 0, mm, month_days[mm])
        #set Feb to default
        month_days[2] = 28
        #set month to start
        month = 1
        #set day to start
        day = 1
    #toprint("Total days %s", 0,  total_days)
    return total_days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
                  #((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed result-%s answer-%s" %(result, answer)
        else:
            print "Test case passed!"

if __name__ == "__main__":
    from cProfile import run
    test()