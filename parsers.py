#!/usr/bin/python

'''
Parsers
'''
import sys,os

'''
This parser returns {Word number, word}
'''
def parse_dict(path):
    fh = open(path,'r')
    dict = {}
    for line in fh.readlines():
        tmp = line.strip().split()
        dict[tmp[1]] = tmp[0]
#dict[tmp[0]] = tmp[1]
        return dict

'''
This parser returns 2 dictionaries,
questID which is the { Question Number, [list of words in question] }
questOD which is the { Order in the file, [list of words in the question] }

'''
def parse_quest(path):
  fh = open(path, 'r')
  i=0
  quest = {}
  questID={}
  questOD={}
  line = fh.readline()
  while (line != ''):
    tmp = line.strip().split()
    line2 = fh.readline()
    tmp2 = line2.strip().split()
    questID[tmp[3]] = tmp2
    questOD[i] = tmp2
    fh.readline()
    line = fh.readline()
    i += 1
  return questID, questOD

'''
This parser returns 1 dictionary,
the termDict which is the { questOD_number, [word in the dictionary, the frequency]
'''

def parse_term(path):
  fh = open(path, 'r')
  i = 0;
  termDict = {}
  for line in fh.readlines():
    tmp = line.strip().split()
    termDict[i] = tmp[1:]
  return termDict[i]
