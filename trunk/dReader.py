#!/usr/bin/python
'''
Reading in Dicionary Data
./myprog <path_to_questions.txt> <path_to_termfreq.dat> <path_to_topics.txt> 
<path_to_test_questions.txt> [<path_to_dictionary.txt>]
'''
import sys,os

def parse_dict(path):
  fh = open(path,'r')
  dict = {}
  for line in fh.readlines():
   tmp = line.strip().split()
   dict[tmp[1]] = tmp[0]
   #dict[tmp[0]] = tmp[1]


  return dict

id = parse_dict("dictionary.txt")
print id
