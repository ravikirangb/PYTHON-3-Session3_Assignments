# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:34:25 2018

@author: 1000091

Implement a function longestWord() that takes a list of words and returns the longest
one.
"""
import os, sys

def longestWord(List):
    LongestOne=""
    for Eachword in List:
        if len(LongestOne) < len(str(Eachword)):
            LongestOne = str(Eachword)
    return LongestOne

WordList = ['Schenectady','Bangalore','Houston']

print("The longest word in the list is:",longestWord(WordList))