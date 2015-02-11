from pandas import DataFrame

def chi2(original,expected):
    """
    Given 2 dataframes:
    original = DataFrame(data=[(7,16,6),(43,34,44)], index = ['YES','NO'], columns=['HIT', 'SMASHED', 'CONTROL'])

    expected = DataFrame(data=[[9.67]*3,[40.33]*3], index = ['YES','NO'], columns=['HIT', 'SMASHED', 'CONTROL'])
    """
    return ((original-expected)**2/expected).values.sum()
