#!/usr/bin/env python

# Import the iterator from operator library
from operator import itemgetter
import sys

# Specify default values
current_word = None
current_count = 0
word = None

# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip()

    # split the input we got from mapper.py to get word and count
    word, count = line.split('\t', 1)

    # convert count from string to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number ignore/discard this line
        continue

    # sort the map outout to pass to reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to standard output
            print('{}\t{}'.format(current_word, current_count))
        current_count = count
        current_word = word

# output the last word if required
if current_word == word:
    print('{}\t{}'.format(current_word, current_count))
