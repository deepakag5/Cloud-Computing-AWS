#!/usr/bin/env python

# import the system library
import sys

# input data comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # it will work as input for the Reducer
        # tab-delimited word and count
        print('{}\t{}'.format(word.strip(), 1))
