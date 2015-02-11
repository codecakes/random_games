from pandas import DataFrame
from scipy.stats import chisqprob

"""
Chi2 Analysis should be used with Independent Test Subjects
"""

def chi2(original,expected):
    """
    Given 2 dataframes:
    original = DataFrame(data=[(7,16,6),(43,34,44)], index = ['YES','NO'], columns=['HIT', 'SMASHED', 'CONTROL'])

    expected = DataFrame(data=[[9.67]*3,[40.33]*3], index = ['YES','NO'], columns=['HIT', 'SMASHED', 'CONTROL'])
    """
    return ((original-expected)**2/expected).values.sum()


def chi2_cmp(chi2_val, df, alpha_val):
    """
    if the probability of getting chi2_val at df is < alpha_val is TRUE,
    then it is a significant val. Reject the Null.
    """
    return round(chisqprob(chi2_val, df), 4) < alpha_val

def kramers_phi_v(chi2_val, num_samples, d):
    """
    used when > 2x2 matrix;
    testing for strength between the two variables
    """
    k = min((d.columns.size,d.index.size))
    return sqrt(float(chi2_val)/(num_samples*(k-1)))
