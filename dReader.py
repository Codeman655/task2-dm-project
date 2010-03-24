#!/usr/bin/python

'''
package dreader
Reading in Dicionary Data
./myprog <path_to_questions.txt> <path_to_termfreq.dat> <path_to_topics.txt> 
<path_to_test_questions.txt> [<path_to_dictionary.txt>]
'''

import sys,os

#def parse_dict(path):
fh = open("dictionary.txt", 'r')
for line in fh.readlines():
  tmp = line.strip().split()
  print tmp
  
