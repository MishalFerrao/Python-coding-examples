#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getOneBits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#
def getOneBits(n):
    results_array = []
    binary_form = []
    ones_count = 0
    while n > 1:
        rem = n % 2
        quo = n // 2
        if rem == 1:
            ones_count += 1
        binary_form.append(rem)
        ##print("n {} r {} q {} ones_count {}".format(n, rem, quo, ones_count))
        n = quo
    binary_form.append(1)
    ones_count += 1
        
        
        
    results_array.append(ones_count)
    
    #print(binary_form)
    
    index = 1
    for k in range(len(binary_form)-1, -1, -1):
        if binary_form[k] == 1:
            results_array.append(len(binary_form) - k)
            index += 1
            
            
    #print(results_array)
    
    return results_array
    
            
    
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')