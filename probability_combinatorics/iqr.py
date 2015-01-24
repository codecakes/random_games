from numpy import median

def quartile_range(arr):
    """
    Find out the Interquartile Range
    """
    #if array is even
    if len(arr)%2 == 0:
        left=arr[:len(r)/2]
        left = left[len(left)/2]
        right=arr[len(r)/2:]
        right = right[len(right)/2]
    else:
        #else if it is odd
        left = median(arr[:len(r)/2])
        right = median(arr[len(r)/2+1:])
    return left, right - left, right  #Q1,Q2,Q3

def outliers_min_max(q1,q2,q3):
    """
    Given
    q1: Lower Quartile Number
    q2: Inter-Quartile Range(this is a range from difference q3-q1, not one number)
    q3: Upper Quartile Number
    Returns the lower and upper boundaries outside which any number
    is an outlier.
    """
    return q1 - (1.5*q2), q3 + (1.5*q2)
