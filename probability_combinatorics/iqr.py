from numpy import median

def quartile_range(arr):
    """
    Find out the Interquartile Range
    """
    #if it is odd
    if len(arr)%2 != 0:
        left=median(arr[:len(arr)/2])
        right=median(arr[len(arr)/2 + 1:])
    else:
        #if array is even
        left = median(arr[:len(arr)/2])
        right = median(arr[len(arr)/2:])
    return left, abs(right - left), right  #Q1,Q2,Q3

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

def filter_outlier_df(df):
    """
    Filters outliers from DataFrame.
    df: DataFrame.
    #col_name: String - Column name of the DataFrame.
    """
    q1, q2, q3 = quartile_range(sorted(df))
    low_bound, upper_bound = outliers_min_max(q1,q2,q3)
    return df[(df >= low_bound) & (df <= upper_bound)]
