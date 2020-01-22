#!/usr/bin/python3
import sys
import collections
import re

if len(sys.argv) != 2:
    sys.stderr.write("<Usage> ./main <input.txt>\n")
    sys.exit(0)

input_file = open(sys.argv[1],'r').read()
processes = {}
num_of_pro = input_file.split('\n')[0]
for inputs in input_file.split('\n')[1::][:-1]:
    input_num = re.search(r'(\d+)\,(\d+)', inputs)
    input_num_1 = input_num.group(1)
    input_num_2 = input_num.group(2)
    processes[input_num_1] = input_num_2
processes = collections.OrderedDict(sorted(processes.items()))
print(processes.items())

def waiting_time():
    wt = []
    wt.append(int(0))
    for process, ex_time in processes.items():
        if wt[-1] < 
        wt.append(int(process)-1 + int(ex_time) + wt[-1])
    print(wt)

waiting_time()
