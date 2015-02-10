from math import sqrt
from itertools import izip
from numpy import mean

from py_variance_std import t_percentile

def calc_slope(r, sdy, sdx): return r * (float(sdy)/sdx)

def line_fitting(x_arr, y_arr):
    xbar = mean(x_arr)
    ybar = mean(y_arr)
    xsqr_bar = mean([i**2 for i in x_arr])
    xybar = mean([i*j for i,j in izip(x_arr, y_arr)])
    """
    using straight line y = mx + c;
    m(of a sample data points) = Covariance(X,Y)/Covariance(X,X)
    = E[(X - E(X))(Y - E(Y))]/E[(X - E(X))^2]
    Another way: Look at calc_slope given STD Y and STD X and r
    """
    #calcuate the slope m
    m = (xbar*ybar - xybar)/(xbar**2 - xsqr_bar)
    #calculate the y intercept
    c = ybar - m*xbar
    return ybar,m,xbar,c

def trace_line(x_arr, y_arr, x_start = 0):
    y, m, x, c = line_fitting(x_arr, y_arr)
    return [(i, (m*i)+c) for i in [x_start]+list(x_arr)]

def line_error(**params):
    """
    The least squares estimates represent the minimum value;
    http://www.pmean.com/10/LeastSquares.html
    params: x_arr, y_arr, m,c
    """
    if 'x_arr' in params and 'y_arr' in params:
        if ('m' in params and 'c' in params):
            m,c = params['m'], params['c']
        else:
            y, m, x, c = line_fitting(params['x_arr'], params['y_arr'])
        return [(yi - ((m*xi)+c))**2 for yi,xi in izip(params['y_arr'], params['x_arr'])]


def std_error_y_estimate(n, y_line_error_var):
    """
    To construct a confidence interval for the slope of the regression line, we need to know the standard error of the sampling distribution of the slope;

    n: total samples in x or y;
    y_line_error_var: sum(line_error(**params))

    df = n-2 since two variables while calculating linear regression.
    #calculate \summ(yi - y_cap)^2 variance
    line_error_var = line_error(**params)
    """
    return sqrt(float(y_line_error_var)/(n-2))

def x_line_std(x_arr):
    xbar = mean(x_arr)
    return sqrt(sum([(xi - xbar)**2 for xi in x_arr]))

def std_error_linear(se_y, x_line_std):
    """
    se_y: from std_error_y_estimate(n, y_line_error_var)
    #calculate x - xbar variance and then STD
    xbar = mean(x_arr)
    x_line_std: x_line_std(x_arr, xbar)
    """
    return se_y/x_line_std

def find_std_err_linear(x_arr, y_arr, n_sample):
    #find descriptive params
    ybar,m,xbar,c = line_fitting(x_arr, y_arr)
    #find error in x
    se_x = x_line_std(x_arr)
    #find error in y
    y_line_error = sum(line_error(**dict(x_arr=x_arr, y_arr=y_arr, m=m, c=c)))
    se_y = std_error_y_estimate(n_sample, y_line_error)
    #return standard error
    return std_error_linear(se_y, se_x)

def r_squared(x_arr, y_arr):
    """
    Literally Trying to do sqrt() of scipy.stats import pearsonr val
    using functions in this module: linear_regression.py.

    Also called Coefficient of Determination.
    It simply means total_variation_line: How much the best fit line is
    "fit" Or Away from the scattered points. High value means good fit.
    How much % is explained by the Fitted Line.
    High R^2 = good model, probably profitable,
    Low R^2 = bad model, probably dangerous
    """
    y, m, x, c = line_fitting(x_arr, y_arr)
    total_var_y = ([(i-y)**2 for i in y_arr])  #(y-ybar)^2
    #print sum(total_var_y)
    #\summ(yi - mxi * c)^2/\summ(yi - ybar)^2
    variation_not_by_line = float(sum(line_error(x_arr=x_arr, y_arr=y_arr, m=m, c=c)))/sum(total_var_y)
    #R sqaured
    return 1 - variation_not_by_line #total variation in x, variation in line

def calc_tscore_from_r(r,n):
    """
    Hypothesis Testing if relationship is due to sampling error.
    r: coefficient of determination
    n: number of elements in a sample
    Returns: t score
    For looking at critical t val and comparing the t score,
    df = n-2 since there are 2 variables for correlation under test.
    """
    return r*sqrt(float(n-2)/(1 - r**2))

def calc_p_from_tval_from_r(r,n, one_tailed= 0 ):
    return t_percentile(calc_tscore_from_r(r,n), n-2, one_tailed= one_tailed)

def margin_error_linear(tscore, se): return tscore * se

def ci_linear(slope, tscore, se):
    margin_error = margin_error_linear(tscore, se)
    return (slope - margin_error, slope + margin_error)
