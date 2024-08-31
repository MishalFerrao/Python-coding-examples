#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'romanizer' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def romanizer(numbers):
    arabic_no = [1,2,3,4,5,6,7,8,9,10,40,50,90,100,400,500,900,1000]
    roman_no = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XL','L','XC','C','CD','D','CM','M']
    string_array = []
    
    for i in range(len(numbers)):
        input_no = numbers[i]
        
        if input_no <= 10:
            string_array.append(roman_no[arabic_no.index(input_no)])
    
        else:
            final_string = ""
            while (input_no >0):
                for i in range(len(arabic_no)):
                    if input_no < arabic_no[i]:
                        base_value = arabic_no[i-1]
                        break
                
                quo = input_no // base_value
                rem = input_no % base_value
                
                final_string = final_string + (roman_no[arabic_no.index(base_value)] * quo)
                #print("input_no {} base_value {}, rem {} quo {} final_string {}".format(input_no, base_value, rem, quo, final_string))
                input_no = rem
                
            string_array.append(final_string)
            
    return string_array      
            
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = romanizer(numbers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
