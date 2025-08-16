#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
# 19:37 
# 20:04


def gradingStudents(grades):
    # Write your code here
    def round_grade(grade: int)-> int:
        # difference between the grade and the next multiple of 5 is less than 3 , round  up o the next multiple of 5.
        # Means: 
        #   grade % 5 is 
        #        2: 3 for next multiple - do not round
        #        3: 2 for next multiple - round
        #        4: 1 for next multiple - round
        #print (f"{grade} - {grade // 5}  {grade / 5}  {grade % 5}")        
        #print (f"{grade} - {grade // 5}  {grade / 5}  {grade % 5}  {((grade // 5) + 1) * 5}")        
        if (38 <= grade) and (3 <= (grade % 5)):
            return ((grade // 5) + 1) * 5
        return grade        
        
    return_grades = []
    for i, grade in enumerate(grades):
        return_grades.append(round_grade(grade))
    return return_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
