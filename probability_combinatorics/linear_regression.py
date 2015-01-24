from itertools import izip
from numpy import mean


def line_fitting(x_arr, y_arr):
    xbar = mean(x_arr)
    ybar = mean(y_arr)
    xsqr_bar = mean([i**2 for i in x_arr])
    xybar = mean([i*j for i,j in izip(x_arr, y_arr)])
    """
    m(of a sample data points) = Covariance(X,Y)/Covariance(X,X)
    = E[(X - E(X))(Y - E(Y))]/E[(X - E(X))^2]
    """
    m = (xbar*ybar - xybar)/(xbar**2 - xsqr_bar)
    c = ybar - m*xbar
    return ybar,m,xbar,c

def trace_line(x_arr, y_arr, x_start = 0):
    y, m, x, c = line_fitting(x_arr, y_arr)
    return [(i, (m*i)+c) for i in [x_start]+list(x_arr)]

def line_error(x_arr, y_arr):
    y, m, x, c = line_fitting(x_arr, y_arr)
    return [(yi - ((m*i)+c))**2 for yi,i in izip(y_arr, x_arr)]

def r_squared(x_arr, y_arr):
    """
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
    variation_not_by_line = float(sum(line_error(x_arr, y_arr)))/sum(total_var_y)
    #R sqaured
    return 1 - variation_not_by_line #total variation in x, variation in line
