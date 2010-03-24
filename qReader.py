#!/usr/bin/python
'''
package dreader
Reading in Dicionary Data
./myprog <path_to_questions.txt> <path_to_termfreq.dat> <path_to_topics.txt> 
<path_to_test_questions.txt> [<path_to_dictionary.txt>]
'''

import sys,os
def parse_quest(path):
  fh = open(path, 'r')
  i=0
  quest = {}
  questID={}
  questOD={}
  for line in fh.readlines():
    if i%3 == 0:
      tmp = line.strip().split()
      questID[tmp[3]] = "c" #Quest ID
      questOD[i] = "c"    #Quest Order
    if i%3 == 1:
      questID[tmp[3]]=line.strip()
      questOD[i]=line.strip()
    return questID, questOD

qID,qOD = parse_quest("questions.txt")
print qID
