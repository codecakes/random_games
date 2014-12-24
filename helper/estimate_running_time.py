"""Debugging helper.
Fast and easy way to Roughly gets the running time of a function.
Implement a counter in the original function in loops.
Make sure to include counter var in the i/p and return the counter value in the called func as well."""

from math import log
from matplotlib import pyplot as plt


def running_time(func, counter, plot_type, *args, **kwargs):
    """
    A very simple debug to test loops or no loops running time.
    func: some math function thta returns a numeric value
    plot_type: can be LOGLOG or Standard
    Note:
    Have to add counter to the func function as well
    """
    plots = []
    counter = 0
    #include counter
    output = (func(counter, *args, **kwargs))  #returns [value, counter]
    value, counter = output
    if plot_type.upper() == "STANDARD":
        plots.append(output)
    else:
        plots.append((log(float(value)), log(float(counter))))
    #print plots
    return plt.plot(plots)
