import argparse
import time
import random

parser = argparse.ArgumentParser(description='')
group = parser.add_argument_group('')
group.add_argument("-epochs",type=int, default=10,help="dimension")
group.add_argument("-T",type=float, default=2.269185314213022, help="Temperature")
group.add_argument("-cuda",type=int,default=-1)

args = parser.parse_args()


for i in range(args.epochs):
    time.sleep(0.3+random.randint(0,10)/10)
    print("at epoch:",i,"T:",args.T,"cuda",args.cuda)

