#!/usr/bin/python

"""
1. Given 2 strings
2. Convert them to lists
3. Get a word frequency counter of unique words
4. Get the dot product of common words
5. Get the product of the normalized dot products of each vector frequency
6. Divide step 4/5. That's the document distance

Detailed steps are as follows(Yes I stole this description because it saves 
the whole explainer for dummies time):

# For each input file, a word-frequency vector is computed as follows:
#    (1) the specified file is read in
#    (2) it is converted into a list of alphanumeric "words"
#        Here a "word" is a sequence of consecutive alphanumeric
#        characters.  Non-alphanumeric characters are treated as blanks.
#        Case is not significant.
#    (3) for each word, its frequency of occurrence is determined
#    (4) the word/frequency lists are sorted into order alphabetically
#
# The "distance" between two vectors is the angle between them.
# If x = (x1, x2, ..., xn) is the first vector (xi = freq of word i)
# and y = (y1, y2, ..., yn) is the second vector,
# then the angle between them is defined as:
#    d(x,y) = arccos(inner_product(x,y) / (norm(x)*norm(y)))
# where:
#    inner_product(x,y) = x1*y1 + x2*y2 + ... xn*yn
#    norm(x) = sqrt(inner_product(x,x))
"""

import operator, re
from collections import Counter
from math import acos
from numpy.linalg.linalg import norm

split_words = lambda f: reduce(operator.add,map(\
lambda x: x.strip('*-\n').split(), f.readlines()))

regex_words = lambda rd: reduce(operator.add, map(\
lambda x:re.findall(r"[a-zA-Z]+", x), rd))


def calc_doc_dist(l1,l2):
    l1_f = Counter(l1.split())
    l2_f = Counter(l2.split())
    l1l2 = sum([l1_f[w]*l2_f[w] for w in l1_f if w in l2_f])
    return acos(float(l1l2)/(norm(l1_f.values())*norm(l2_f.values())))

def doc_dist_files(fn1,fn2):
    with open(fn1) as f1:
        with open(fn2) as f2:
            fread1 = regex_words(split_words(f1))
            fread2 = regex_words(split_words(f2))
            return calc_doc_dist(fread1, fread2)