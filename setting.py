import time
import re
import numpy as np

maximumJobs = 8

command = ['python','./pseudorun.py']

settings = [['-no',str(i)] for i in range(8)]

parameters = {"-T":[str(i/10) for i in range(10,21)]}

def before():
    #print("this is pre-process")
    pass

def after():
    #print("this is sub-process")
    pass

def process(result):
    nums = []
    for i in result[-10:-1]:
        nums.append([float(s) for s in re.findall(r'-?\d+\.?\d*',i)])
    return np.array(nums)

if settings != []:
    assert len(settings) == maximumJobs
