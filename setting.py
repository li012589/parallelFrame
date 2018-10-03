from multiprocessing import Queue
import time
import re
import numpy as np

maximumJobs = 8

command = ['python','./pusedorun.py']

settings = [['-no',str(i)] for i in range(8)]

if settings != []:
    assert len(settings) == maximumJobs

parameters = {"-T":[str(i/10) for i in range(10,21)]}

q = Queue()

for name,content in parameters.items():
    for i in content:
        q.put(command+[name]+[i])


def before():
    #print("this is pre-process")
    pass

def after():
    #print("this is sub-process")
    pass

def process(result):
    nums = []
    res = result.decode('utf-8').split('\n')
    for i in res[:-1]:
        nums.append([float(s) for s in re.findall(r'-?\d+\.?\d*',i)])
    return np.array(nums)