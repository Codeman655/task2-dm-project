#!/usr/bin/python

import sys, os, random
from parsers import *

#inverse term frequency

#inverse document frequency

# Calculate the probability of a term given a topic
def prob_given(termFreqDict, topicDictID, questID):
  probdict = {}
  for qindex in termFreqDict.keys():
    if questID.keys().count(qindex) == 0:
      continue
    myclass = topicDictID[questID[qindex]]
    if probdict.keys().count(myclass) == 0:
      probdict[myclass] = {}
    for term in termFreqDict[qindex].keys():
      if probdict[myclass].keys().count(term) == 0:
        probdict[myclass][term] = 1.0
      else:
        probdict[myclass][term] += 1.0
  for topic in probdict.keys():
    sum = 0.0
    for windex in probdict[topic].keys():
      sum += probdict[topic][windex]
    for windex in probdict[topic].keys():
      probdict[topic][windex] /= sum
  return probdict

# Convert a list of words into a list of valid term indexes
def converter(term_list, dictionary):
  blank_list = []
  for term in term_list:
    tmp = get_word_index(term, dictionary)
    if tmp < 0:
      continue
    blank_list.append(tmp)
  return blank_list

# Calculate the probability of the topics
def topicProb(topicDictID, questID):
  topic_calc = []
  topic_calc.append(0)
  for i in range(1,42):
    count = 0.0
    for qid in questID.values():
      if topicDictID[qid] == i:
        count += 1.0
    topic_calc.append(count/41.0)
  return topic_calc

# Returns the probability of class given a question
def topic_quest_prob(termList, topic, tProbList, probDict):
    factor = 1.0;
    for term in termList:
      if probDict[topic].keys().count(term) == 0:
        return 0.0
      factor *= probDict[topic][term]
    return  factor * tProbList[topic] 
      
# Calculate the probability of the topics given a question
# and return the topic with the highest probability
def probability(questList, topicProbList, probDict, dictionary):
  termList = converter(questList, dictionary)
# random.seed()
# maxTopic = random.randrange(1,42,1)
  maxTopic = None
  maxProb = float(0.0)

  for i in range (1,42):
    tmp = topic_quest_prob(termList, i, topicProbList, probDict)
    if (tmp > maxProb):
      maxProb = tmp
      maxTopic = i
  return maxTopic

