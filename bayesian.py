#!/usr/bin/python
import sys
from parsers import *

if (len(sys.argv) > 6 or len(sys.argv) < 5):
  print "Usage: ./bayesian.py <path_to_questions.txt> <path_to_termfreq.txt>\n\
         <path_to_topics.txt> <path_to_test_questions.txt> [<path_to_dictionary.txt>]"
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
quest, quest_dict = parse_quest(questions_path)

# print quest_dict
print (parse_term(termfreq_path))['572']['786']
