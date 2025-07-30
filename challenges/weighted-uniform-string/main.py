#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    def bool_response(b):
        return "Yes" if b else "No"
    def get_weight(char):
        return ord(char) - 96        
    def produce_weighted(s):        
        prev_c = ""
        accumulated_weight = 0
        weight_list = []
        for c in s:
            
            if c != prev_c:
                accumulated_weight = get_weight(c)
            else:
                accumulated_weight += get_weight(c)                
            weight_list.append(accumulated_weight)
            prev_c = c
            print(f"{c} ; ord = {get_weight(c)} ; accumulated_weight = {accumulated_weight}")
            print(weight_list)
        return weight_list
            
    return [ bool_response(q in produce_weighted(s)) for q in queries]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
