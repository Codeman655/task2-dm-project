#!/usr/bin/python
import sys
from parsers import *
from formulas import *

def create_matrix(questOD, term_dict):
  rows = []
  for q in questOD.keys():
    cols = [0 for i in range(808)]
    for key in term_dict[q].keys():
      cols[key - 1] = term_dict[q][key]
    rows.append(cols)
  return rows


if (len(sys.argv) != 6):
  print "Usage: ./bayesian.py <path_to_questions.txt> <path_to_termfreq.txt>\n\
         <path_to_topics.txt> <path_to_test_questions.txt> <path_to_dictionary.txt>"
  sys.exit()

questions_path = sys.argv[1]
termfreq_path = sys.argv[2]
topics_path = sys.argv[3]
testquest_path = sys.argv[4]
dict_path = None
if (len(sys.argv) == 6):
  dict_path = sys.argv[5]

print "questions file:", questions_path
print "termfreq file:", termfreq_path
print "topics file:", topics_path
print "testquest file:", testquest_path
print "dict file:", dict_path


# Parse the files
questID, questOD = parse_quest(questions_path)

# print quest_dict
term_dict = parse_term(termfreq_path)

# print "572 keys:", term_dict[572].keys()
# print "796 hits:", term_dict[572][790]

print get_word_index("thier", parse_dict(dict_path))

dictionary = parse_dict(dict_path)

matrix = create_matrix(questOD, term_dict)
print matrix[0][207]
topics = parse_topics(topics_path)

#testing probability
probability(questOD.get(1), 0, matrix, 0, topics, dictionary)
