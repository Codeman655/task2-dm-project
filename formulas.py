#!/usr/bin/python

import sys, os
from parsers import *

#inverse term frequency

#inverse document frequency

#Probability generator
#Cond probablitiy of term in the topic

#How to use this:
#quest = list of words in the question
#qNum = quesion number
#freqMatrix = the freqMatrix
#tProb result of TopicProb[question_number]
#topicDict = the Topic Dictionary

def probability(quest, qNum, freqMatrix, tProb, topicDict, termDict):
  #Use the term frequency matrix to generate a probability/topic dictionary

  tProbList = topicProb(topicDict)

  factor=[] 
  for term in quest:
    #Goal=(frequency of terms in the topic)
    tIndex = get_word_index(term, termDict)
    if tIndex < 0:
      continue
    else:
      fij = freqMatrix[qNum][tIndex-1] #frequency of the term in the question

    #This needs to be in a seperate function
    qTopic = topicDict[qNum] #Grabbin' the topic
    print qTopic
    tmpList = []
    term_subtotal = 0
    for tup in topicDict.iteritems():
      if tup[1] == qTopic: #if the value == the topic of the question
        print tup
        tmpList.append(tup[0]);
    for tmp in tmpList:
      term_subtotal += freqMatrix[tmp][tIndex-1] #Sum the frequencies
    print term_subtotal

    print len(freqMatrix[tIndex-1])
    if len(freqMatrix[tIndex-1]) == 0:
      print "error: len = 0, 1"
      return -1
    term_subtotal = float(term_subtotal) / len(freqMatrix[tIndex-1])  

    if tProbList[qNum+1] == 0:
      print "qnum: "
      print qNum
      print tProbList
      print "error: len = 0, 2"
      return -1

    term_subtotal /= tProbList[qNum+1] #This is P(term & topic) Need to check
    print "P(Term in Topic):" 
    print term_subtotal
    factor.append(fij*term_subtotal)
  
  tmpNum = 1
  for item in factor:
    tmpNum *= item
  tmpNum /= len(quest)
  print "resulting probability: "
  print tmpNum
  return tmpNum #whatever this is

#Calculate probability of topic per tital list of questions
def topicProb(topicDict):
  topic_calc = []
  topic_calc.append(0)
  for i in range(1,42):
    count = 0
    for topic in topicDict.itervalues():
      if topic == i:
        count += 1
    topic_calc.append(count/41.0)
  return topic_calc
