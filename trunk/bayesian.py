#!/usr/bin/python
import sys
from parsers import *
from formulas import *

# Check for correct number of arguments
if (len(sys.argv) != 6):
  print "Usage: ./bayesian.py <path_to_questions.txt> <path_to_termfreq.txt>\n\
         <path_to_topics.txt> <path_to_test_questions.txt> <path_to_dictionary.txt>"
  sys.exit()

# Get the paths for the different arguments
questions_path = sys.argv[1]
termfreq_path = sys.argv[2]
topics_path = sys.argv[3]
testquest_path = sys.argv[4]
dict_path = sys.argv[5]

# Parse the files
questID, questOD = parse_quest(questions_path)
topicDictID, topicDictOD = parse_topics(topics_path)
termFreqDict = parse_term(termfreq_path)
dictionary = parse_dict(dict_path)

# Do some preliminary probability
topicProbList = topicProb(topicDictID, questID)
probDict = prob_given(termFreqDict, topicDictID, questID)

# Parse and classify the test questions
testQuestID, testQuestOD = parse_quest(testquest_path)

right = 0.0
wrong = 0.0
c_matrix = dict([(i, dict([(j, 0) for j in range(1,42)])) for i in range(1,42)])

for qkey in testQuestOD.keys():
  qID = testQuestID[qkey]
  guess = probability(testQuestOD[qkey], topicProbList, probDict, dictionary)
  actual = topicDictID[qID]
  c_matrix[guess][actual] += 1
  if guess == actual:
    right += 1.0
  else :
    wrong += 1.0

# Print the confusion matrix and the accuracy
print "\n%110s" % "Confusion Matrix ( row = predicted, column = actual )"
print "\033[47m\033[30m\033[1m   ",
for i in range(1, 42):
  print "%3d" % i,
print "\033[0m"
for guess in c_matrix.keys():
  print "\033[47m\033[30m\033[1m%3d\033[0m" % guess,
  for actual in c_matrix[guess].keys():
    print "%3d" % c_matrix[guess][actual],
  print ''


print "\nAccuracy: %.3f%%" % (right / (right + wrong) * 100),
