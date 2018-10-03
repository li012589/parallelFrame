import argparse
import time

parser = argparse.ArgumentParser(description='')
group = parser.add_argument_group('')
group.add_argument("-epochs",type=int, default=10,help="dimension")
group.add_argument("-T",type=float, default=2.269185314213022, help="Temperature")
group.add_argument("-no",type=int,default=-1)

args = parser.parse_args()


for i in range(args.epochs):
    time.sleep(1)
    print("at epoch:",i,"T:",args.T,"no",args.no)
