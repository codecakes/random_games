from pandas import DataFrame
from scipy.stats import chisqprob, chi2

"""
Chi2 Analysis should be used with Independent Test Subjects
"""
def calc_chi2_expected_val(original_d, marginal_col_totals, marginal_row_totals, total):
    """
    this calculates the expected value matrix;
    see 'chi2' to see how to calcualte chi2/kai 2 values using
    orignal/actual value and expected value matrices.
    """
    percentage_col = marginal_col_totals/total
    expected_val = marginal_row_totals.values * percentage_col.values
    return DataFrame(data = expected_val, index = original_d.index, columns = original_d.columns)


def chi2_val(original,expected):
    """
    Given 2 dataframes:
    original = DataFrame(data=[(7,16,6),(43,34,44)], index = ['YES','NO'], columns=['HIT', 'SMASHED', 'CONTROL'])

    expected = DataFrame(data=[[9.67]*3,[40.33]*3], index = ['YES','NO'], columns=['HIT', 'SMASHED', 'CONTROL'])
    """
    return ((original-expected)**2/expected).values.sum()

critical_chi2_val_from_p = lambda p, df: \
round(scipy.stats.chi2.isf(p, df), 3)

p_from_chi2_val = lambda chi2_val, df: \
scipy.stats.chi2.sf(chi2_val, df)

def chi2_cmp(chi2_val, df, alpha_val):
    """
    if the probability of getting chi2_val at df is < alpha_val is TRUE,
    then it is a significant val. Reject the Null.
    """
    return round(chisqprob(chi2_val, df), 4) < alpha_val

def kramers_phi_v(chi2_val, num_samples, d):
    """
    Independence Test: tests for strength between the two variables
    used when >= 2x2 matrix;
    d: original DataFrame 
    """
    k = min((d.columns.size,d.index.size))
    return sqrt(float(chi2_val)/(num_samples*(k-1)))
