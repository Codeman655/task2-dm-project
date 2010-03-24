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
  for line in fh.readlines():
    if i%3 == 0:
      tmp = line.strip().split()
      questID[tmp[3]] = "c" #Quest ID
      questOD[i] = "c"    #Quest Order
    if i%3 == 1:
      questID[tmp[3]]=line.strip()
      questOD[i]=line.strip()
    i= i+1
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
