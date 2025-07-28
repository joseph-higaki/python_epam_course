#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# start  18:41
# finish 19:27 :(
def isBalanced(s):
    
    # create a stack
    # when an opening bracket push
    # when a closing bracket, pop only if last item is opening one
    # return yes if stack empty
    stack = []
    def pop():        
        stack.pop()        
    def see_last():
        if len(stack) == 0:
            return ""        
        return stack[-1]
    def push(item):
        stack.append(item)
        return item                
    def returnValue(bool_value):
        return "YES" if bool_value else "NO"            
        
    # Write your code here
    
    #create dict for easy close/ open brackets match
    brackets = {
        "]": "[",
        ")": "(",
        "}": "{"
    }
    for c in s:
        #print("stack ",stack)
        if c in brackets.values():
            push(c)
        else:
            closing = brackets.get(c, "~")
            if see_last() == closing:
                pop()
            else:
                return returnValue(False)                
    #print("before return stack ",stack)
    return returnValue(len(stack) == 0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
