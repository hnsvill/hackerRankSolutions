#!/bin/python3

# Designer PDF Viewer
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    # max height * number of letters = area of the highlighted word
    # all letters are 1mm wide
    return max(getLetterHeights(h, word)) * len(word)
    # return "max height: " + str(h) + " " + "word length" + str(len(word))
    
def getLetterHeights(h, word):
    # returns an array of the heights of only the used letters in the word

    # create a dictionary for the heights provided by the user
    alpha = list(string.ascii_lowercase)
    corres = dict(zip(alpha, h))

    usedHeights = []

    for letter in word:
        usedHeights.append(corres[letter])
    
    return usedHeights




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
