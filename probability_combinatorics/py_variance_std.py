"""
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
from scipy.stats import norm, t

def mean(x): return reduce(lambda a,b: (a+b), x)/float(len(x))

def mean_arr(x):
    sumr = 0.
    prod_list = []
    for i in x:
        sumr += i
        prod_list.append(i*i)
    return sumr/len(x), prod_list


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


############# ALL ABOUT CONFIDENCE INTERVAL & INFERENTIAL STATS ################

#standard error
se = lambda sd, sample_size: (sd/sqrt(sample_size))

#half if two tailed else not and /100
def critical_z(percentile, one_tailed):
    return abs(scipy.stats.norm.ppf((100 - percentile)/100.)) if one_tailed \
    else abs(scipy.stats.norm.ppf((100 - percentile)/200.))

#marginal error given z score range
marginal_z = lambda z_score, se: z_score * se

def calc_z(mu, xbar, sd, sample_size):
    """
    Calculate Z score given normal sample distribution mean
    and population mean, its std dev and the sample size for the
    sample distribution.
    """
    #std_error = se(sd, sample_size)
    return float(xbar - mu)/se(sd, sample_size)


def calc_t(mu, xbar, sd, sample_size): return calc_z(mu, xbar, sd, sample_size)

def t_percentile(t_val, df, one_tailed=0):
    """
    Find P-Value Given T score, DF and if its 1 Tailed or 2 Tailed
    """
    return t.sf(t_val, df) if one_tailed else t.sf(t_val, df) * 2

def critical_t(percentile, df, one_tailed):
    return t.isf((100-percentile)/100., df) if one_tailed else t.isf((100-percentile)/200., df)

#same as above, but in proportion
def t_val_from_t_percentile(t_percentile, df, one_tailed = 0):
    """
    Find T score given T percentile, DF
    and if its 1 Tailed or 2 Tailed
    """
    return t.isf(t_percentile, df) if one_tailed else t.isf(t_percentile/2., df)


def t_cmp(calculated_t, critical_t):
    """
    Given Critical T Value and T score,
    Return if its Significant or Not.
    """
    return abs(calculated_t) > abs(critical_t)

def calc_probability_sample_mean(mu, xbar, sd, sample_size):
    return scipy.stats.norm.cdf(calc_z(mu, xbar, sd, sample_size))

def ci_t_margin_error(sd, sample_size, df, t_score = None, percentile = None, one_tailed = 0):
    critical_t_score = 0.
    if percentile: critical_t_score = critical_t(percentile, df, one_tailed)
    elif t_score: critical_t_score = t_score
    #std_error = se(sd, sample_size)
    return marginal_z(critical_t_score, se(sd, sample_size))

def ci_t(xbar, sd, sample_size, df, t_score = None, percentile = None, one_tailed = 0):
    margin_error = ci_t_margin_error(sd, sample_size, df, t_score = t_score, percentile = percentile, one_tailed = one_tailed)
    return (xbar - margin_error, xbar + margin_error)

def ci_margin_error(sd, sample_size, z_score = None, percentile = None, one_tailed = 0):
    """
    z score * std_error is the margine of error i C.I. from the sample mean
    """
    critical_z_score = 0.
    if percentile: critical_z_score = critical_z(percentile, one_tailed)
    elif z_score: critical_z_score = z_score
    #std_error = se(sd, sample_size)
    return marginal_z(critical_z_score, se(sd, sample_size))


#confidence interval
def ci(xbar, sd, sample_size, z_score = None, percentile = None, one_tailed = 0):
    """
    xbar: sample mean
    percentile: in %
    """
    margin_error = ci_margin_error(sd, sample_size, z_score = z_score, percentile = percentile, one_tailed=one_tailed)
    return (xbar - margin_error, xbar + margin_error)

#Decision process component
def z_cmp(calculated_z_score_proportion, criticalz_percentage_proportion):
    """
    calculated_z_score_proportion: the z score calculated from mu and xbar in proportion
    criticalz_percentage_proportion: Given Critical Value proportion for acceptance criteria
    if calculated_z_score_proportion > criticalz_percentage_proportion
    then the chance of that happening is p < criticalz_percentage_proportion
    """
    return abs(calculated_z_score_proportion) > scipy.stats.norm.cdf(scipy.stats.norm.ppf((100-criticalz_percentage_proportion)/100.))



### Correlation Measures using T Stats ####
def t_r_squared(t_score, df):
    t= t_score**2
    return t/float(t+df)
