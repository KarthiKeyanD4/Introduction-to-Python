import sys
import random

import test_stats as ts

filename = sys.argv[1]
word = sys.argv[2]
word_length = int(sys.argv[3])

sorted_alpha_dict,sorted_word_dict,paired_word_dict = ts.stats_info(filename)


def next_word(current_word,paired_word_dict):
	if len(paired_word_dict[current_word]) == 0:
		print ("No paired value for " + current_word + "\n")
		exit()
		
	probability = random.randrange(sum(paired_word_dict[current_word].values()))
	
	count = 0
	for entry in paired_word_dict[current_word]:
		count += paired_word_dict[current_word][entry]
		if probability < count:
			return (entry )

def markov_chain(word,word_length,paired_word_dict):
	sentence = ""
	current_word = word
	
	for n in range(word_length):
		sentence += current_word + " "
		current_word = next_word(current_word,paired_word_dict)
	print (sentence)

markov_chain(word,word_length,paired_word_dict)