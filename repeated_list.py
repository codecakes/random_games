"""
If number not in seen map, add num:pos;
If number in seen map, turn pattern matching on;
If pattern matching on check if last index+1 == current index + 1 and last_index not in temp dict to overlap;
If above true, add to temp dict current_pos: tot++ + carryover. carryover += 1
If patterh match off and tmp dict has length, iterate over all keys as list indices and add values in outlist;
"""


def getPosition(input1):
    pat_mat = index = nextVal = curVal = tot = 0
    carryover = 0
    seen = {}
    ln = len(input1)
    outlist = [0] * ln
    cache = [0] * ln
    
    while index < ln:
        curVal = input1[index]
        
        if curVal not in seen:
            seen[curVal] = index
        else:
            last_index = seen[curVal]
            if input1[last_index+1] == input1[index+1] and last_index+1 != index:
                carryover = 1
                cache[index] = 1 + carryover
        index += 1
    
    return cache

if __name__ == "__main__":
    print getPosition([15,3,15,3, 15, 40])
    print getPosition([15,15,3,15,15,40])
    #print getPosition([6,3,5,17,19,15,13,15,6,3,5,3])

        
        