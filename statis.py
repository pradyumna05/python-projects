""" import statistics

print(dir(statistics)) """

# mean calculations

def mean(data):
    return sum(data)/len(data)

#median calculations

def median(data):
    n = len(data)
    index = n//2
    if n % 2:
        return sorted(data)[index]
    return sum(sorted(data)[index-1:index+1])/2

#mode calculations

from collections import Counter

def mode(data):
    c = Counter(data)
    return c.most_common()[0][0]

#standard deviation caculations

import math
def var(data):
    n=len(data)
    mean = sum(data)/n
    return sum((x-mean)**2 for x in data)/n

def std(data):
    variance = var(data)
    
    std_dv = math.sqrt(variance)
    return std_dv


