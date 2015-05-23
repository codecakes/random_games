# -*- coding: utf-8 -*-

"""
An IT company organized a referral point game for their employees. 
Let us say number of employees in the group are n (n&gt;0) and maximum points in
the game are 20. Each employee has a unique identification number. 
The employee’s points are sorted according to their identification numbers. 
Now consider this sorted list. I want to find for each position i (1≤i≤n) in 
the list, the maximum number of employees starting from the list 
(and not ending at position i) which have same points (in the order of list) 
as the employees ending at position i (in the order of the list).
"""


def getPosition(input1):
    index = nextVal = curVal = tot = 0
    occur_dct = {}
    ln = len(input1)
    outlist = [0] * ln
    
    while index < ln:
        
        curVal = input1[index]
        if index + 1  < ln:
            nextVal = input1[index+1]
            
            if curVal not in occur_dct:
                occur_dct[curVal] = nextVal
            elif curVal in occur_dct:
                if occur_dct[curVal] == nextVal:
                    tot += 1
                    outlist[index] = tot
                elif index - 1 >= 0:
                    if occur_dct[input1[index-1]] == curVal and outlist[index-1]>0 and occur_dct[curVal] == nextVal:
                        tot += 1
                        outlist[index] = tot
        index += 1
    
    del occur_dct
    return outlist


if __name__ == "__main__":
    print getPosition([15,3,15,3, 15, 40])
    print getPosition([15,15,3,15,15,15,40])
    #print getPosition([6,3,5,17,19,15,13,15,6,3,5,3])