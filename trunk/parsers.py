#!/usr/bin/python

'''
Parsers
'''
import sys,os


'''
This gets you the dictionary index given a word
Returns:
	index on success
	-1 on failure
'''
def get_word_index(word, dict):
  for key in dict.keys():
    if word == dict[key]:
      return key
  return -1



'''
This parser returns {Word number, word}
'''
def parse_dict(path):
  fh = open(path,'r')
  dict = {}
  for line in fh.readlines():
    tmp = line.strip().split()
    dict[int(tmp[1])] = tmp[0]
  return dict

'''
This parser returns 2 dictionaries,
questID which is the { Question Number, [list of words in question] }
questOD which is the { Order in the file, [list of words in the question] }

'''
def parse_quest(path):
  fh = open(path, 'r')
  i=1
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
  fh.close()
  return questID, questOD

'''
This parser returns 1 dictionary,
the termDict which is the { questOD_number, [word in the dictionary, the frequency]
'''

def parse_term(path):
  fh = open(path, 'r')
  termDict = {}
  for line in fh.readlines():
    tmp = line.strip().split()
    termDict[int(tmp[0])] = dict([(int(tmp[i]), int(tmp[i+1])) for i in range(1,len(tmp)-1,2)])
  fh.close()
  return termDict

def parse_topics(path):
  fh = open(path, 'r')
  topics = {}
  i = 0
  for line in fh.readlines():
    tmp = line.strip().split(',')
    topics[i] = int(tmp[-1])
    i += 1
  return topics
