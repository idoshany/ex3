#!/usr/bin/python3
import sys
import re
import collections

input_file = open(sys.argv[1], 'r')


if len(sys.argv)!= 2:
    sys.stderr.write("<Usage> ./main <input.txt>\n")
    sys.exit(1)
def sort_processes():
    clock_cycle_in = {}
    for inputs in input_file.read().split('\n')[1::][:-1]:
        list_input = re.search(r'(\d+)\,(\d+)', inputs)
        clock_cycle_in[list_input.group(1)] = list_input.group(2)
    clock_cycle_in = collections.OrderedDict(sorted(clock_cycle_in.items()))
    return clock_cycle_in

if __name__ == '__main__':
    sorted_processes = sort_processes()
    TA = []
    for i in sorted_processes:
        print(i)
