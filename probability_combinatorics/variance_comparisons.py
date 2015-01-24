from numpy import var
from matplotlib.pyplot import plot

from py_variance_std import mean_arr, mean, variance_biased, variance_unbiased

from random import randint, choice

def create_random_population():
    #populate
    random_population = [randint(1,1000) for _ in xrange(1000)]
    return random_population

def create_random_sample(random_population, r = 100):
    """
    choose sample from population
    r: range of number to choose from the random population
    """
    choose_sample = [choice(random_population) for _ in xrange(r)]
    return choose_sample

def actual_population_variance(random_population):
    #take out population variance
    population_variance = var(random_population)
    return population_variance


def create_variance_map():
    random_population = create_random_population()
    population_variance = actual_population_variance(random_population)
    biased_list = []
    unbiased_list = []
    for _ in xrange(10):
        samples = create_random_sample(random_population)
        biased_list.append(variance_biased(samples))
        unbiased_list.append(variance_unbiased(samples))
        #print "Biased_var - population_variance"
        #print "{} - {}".format(biased_var, population_variance)
        #print "Unbiased_var - population_variance"
        #print "{} - {}".format(unbiased_var, population_variance)
    print biased_list, unbiased_list
    print population_variance, mean(biased_list), mean(unbiased_list)
    return plot((biased_list, unbiased_list))

if __name__ == "__main__":
    create_variance_map()
