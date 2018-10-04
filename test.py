from multiprocessing import Pool,Queue,Process
import sys
import subprocess
import setting
import numpy

#qRev = Queue()

def worker(settings):
    while not setting.q.empty():
        setting.before()
        command = setting.q.get()
        command += settings
        print("working on:",command)
        output = subprocess.check_output(command)
        #save = setting.process(output)
        #print(save)
        #qRev.put([command,save])
        setting.after()
        print("work finish:",command)
        #sys.stdout.flush()

processes = []
for i in range(setting.maximumJobs):
    p = Process(target = worker,args=(setting.settings[i],))
    p.start()
    processes.append(p)
'''
print("run all finish")
while not qRev.empty():
    print(qRev.get())
    sys.stdout.flush()
'''

for p in processes:
    p.join()
