from itertools import combinations
from py_variance_std import t_significant

#given 3 brands prices
products = dict(snapzi = (15, 12, 14, 11),
irisa = (39, 45, 48, 60),
lolamoon = (65, 45, 32, 28))

#which of these brands have most and least significant price differences?
#do a two tailed T test
result = [(t_significant(products[brands[0]], products[brands[1]], 95, 0), brands[0], brands[1])  for brands in (combinations(products, 2))]

print max(result, key = lambda x: x[0][0]), min(result, key = lambda x: x[0][0])
