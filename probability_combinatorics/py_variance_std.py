"""
If there is no numpy/scipy lib;
var = sd^2 = summ(Xi^2 - mu)/N = summ(Xi^2)/N - mu^2

Observation is:
Biased_Variance = (n-1)/n Population/Total_Variance
OR,
summ(Xi^2 - mu)/n = (n-1)/n Population/Total_Variance
=> Population_Variance = summ(Xi^2 - mu)/(n-1)
is a better Variance estimate than Sample Variance
"""

from math import sqrt, pi, e
import scipy.stats

def mean_arr(x):
    sumr = 0.
    prod_list = []
    for i in x:
        sumr += i
        prod_list.append(i*i)
    return sumr/len(x), prod_list

def mean(x): return reduce(lambda a,b: (a+b), x)/float(len(x))

def variance_biased(x):
    """x is a list of numbers"""
    mean_x, prod_list = mean_arr(x)
    return sum(prod_list)/float(len(x)) - (mean_x)**2

def variance_unbiased(x):
    """x is a list of numbers"""
    xbar = mean(x)
    return sum([(i-xbar)**2 for i in x])/float(len(x)-1)


def std_deviation_biased(x):
    return sqrt(variance_biased(x))

def std_deviation_unbiased(x):
    return sqrt(variance_unbiased(x))


def normal_distro_probability(x, xbar, var):
    z2 = float(x-xbar)**2/var  #z squared
    return 1./sqrt((2*pi*var) * (e**z2))


def normal_sample_variance(original_var, sample_size):
    """given original variance but not all data points"""
    return original_var/sample_size

#standard error
se = lambda sd, sample_size: (sd/sqrt(sample_size))

#critical z score range
critical_z = lambda z_score, se: z_score * se

def calc_z(mu, xbar, sd, sample_size):
    """
    Calculate Z score given normal sample distribution mean
    and population mean, its std dev and the sample size for the
    sample distribution.
    """
    std_error = se(sd, sample_size)
    return float(xbar - mu)/std_error

#confidence interval
def ci(xbar, sd, sample_size, z_score = None, percentile = None):
    """
    xbar: sample mean
    percentile: in %
    """
    if percentile:
        #half and /100
        percentile = (100 - percentile)/200.
        z_score = abs(scipy.stats.norm.ppf(percentile))
    std_error = se(sd, sample_size)
    cz = critical_z(z_score, std_error)
    return (xbar - cz, xbar + cz)

def ci_margin_error(xbar, sd, sample_size, z_score = None, percentile = None):
    """
    z score * std_error is the margine of error i C.I. from the sample mean
    """
    if percentile:
        #half and /100
        percentile = (100 - percentile)/200.
        z_score = abs(scipy.stats.norm.ppf(percentile))
    return critical_z(z_score, se)
