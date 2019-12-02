# -*- coding: utf-8 -*-
"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: lab 7
Date of last modification: 12/2/2019
Purpose of program:solve the edit distance problem with strings
"""

def edit_distance(str1, str2):
    count = []

    word_1 = len(str1) + 1 # variables created to store length of words +1 (empty strings)
    word_2 = len(str2) + 1

    for i in range(word_2): # creates the two dimensional array based on the lenght of the word
        count.append([0] * word_1)
       

    for i in range(word_1): # initializes first row with with 0 thru the lenght of the  worfd -1
        count[0][i] = i

    for j in range(word_2): # initializes the first column with 0 thru the lenght of the  worfd -1
        count[j][0] = j

    for i in range(1, word_2): # nested for loop to make comparisons. Starts at 1 since comparisons being at index (1,1)
        for j in range(1, word_1):
            if str1[j-1].lower() == str2[i-1].lower(): # compares the characters of the two strings and type cast to lower chars
                count[i][j] = count[i-1][j-1] # if characters are the same, copy value in the digaonal 
            else:
                # when characters are not the same, look at surronding indices find the min and add one
                count[i][j] = min(count[i - 1][j] + 1, count[i - 1][j - 1] + 1,count[i][j - 1] + 1)
    return count[-1][-1] # returns the last index of the matrix, which holds the solution(min number of steps to solve)
