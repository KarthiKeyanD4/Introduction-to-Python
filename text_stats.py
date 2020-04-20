#!python3
#!/usr/bin/env python3

import sys
import os.path


def write_output(sorted_alpha_dict,sorted_word_dict,paired_word,out_file):
	output = open(out_file,"w")

	for n in range(5):
		output.write("\n\n" + list(sorted_word_dict.keys())[n] + " (" + str(list(sorted_word_dict.values())[n]) + " occurances)")
		sorted_paired_dict = ({key: value for key, value in sorted(paired_word[list(sorted_word_dict.keys())[n]].items(),   key=lambda item: item[1], reverse=True)})
		for m in range(3):
			output.write("\n---" + list(sorted_paired_dict.keys())[m] + " = " + str(list(sorted_paired_dict.values())[m]) + "")

	output.write("\n\n\nAlphabet frequency")
	for entry in sorted_alpha_dict:
		output.write("\n" + str(entry) + " = " + str(sorted_alpha_dict[entry]) )
	output.write("\n\nTotal number of words = " + str(sum(sorted_word_dict.values())))
	output.write("\n\nTotal number of unique words = " + str(len(sorted_word_dict)))


def receives_input():
	if len(sys.argv) <= 1:
		print ("Input file not given\n")
		print ("###Format###\n\npython3 test_stats.py input_filename.txt output_filename.txt")
		exit()
	elif len(sys.argv) == 2:
		in_file = sys.argv[1]
		return read_file(in_file)
	elif len(sys.argv) == 3:
		in_file = sys.argv[1]
		out_file = sys.argv[2]
		sorted_alpha_dict,sorted_word_dict,paired_word = read_file(in_file)
		write_output(sorted_alpha_dict,sorted_word_dict,paired_word,out_file)
		exit()
	else:
		print ("Exceeds number of arguments")
		exit()


def read_file(in_file):
	if not os.path.isfile(in_file):
		print ("###")
		print ("Filename \"" + str(in_file) + "\" not found")
		print ("###")
		exit()

	return stats_info(in_file)

def purify_word(chr_range,words):
	word = ""
	for letter in words:
		if str(ord(letter)) in chr_range:
			word += letter.lower()
		elif letter.isdigit():
			return (False)
	return (word)


def stats_info(in_file):
	with open(in_file,"r",encoding = 'UTF-8') as file:
		open_file = file.read().split()
		alphabet_dict = {}
		words_dict = {}
		paired_word = {}
		total_words = 0

		chr_range = [39,45]
		for values in [str(ord(letter)) for words in open_file for letter in words if letter.isalpha()]:
			if values not in chr_range:
				chr_range.append(values)

		for count,words in enumerate(open_file):
			for letter in words:
				if letter.isalpha():
					if letter.lower() not in alphabet_dict:
						alphabet_dict[letter.lower()] = 1
					else:
						alphabet_dict[letter.lower()] += 1

				elif letter.isdigit():
					isword = False
				else:
					None

			current_word = purify_word(chr_range,words)
			if current_word:
				total_words += 1
				if current_word in words_dict:
					words_dict[current_word] += 1
				else:
					words_dict[current_word] = 1
					paired_word[current_word] = {}

				n = count + 1
				while n < len(open_file):
					next_word = purify_word(chr_range,open_file[n])
					if next_word :
						if next_word in paired_word[current_word]:
							paired_word[current_word][next_word] += 1
						else:
							paired_word[current_word][next_word] = 1
						break
					n += 1

		sorted_alpha_dict = ({key: value for key, value in sorted(alphabet_dict.items(), key=lambda item: item[1], reverse=True)})
		sorted_word_dict = ({key: value for key, value in sorted(words_dict.items(), key=lambda item: item[1], reverse=True)})

		return (sorted_alpha_dict,sorted_word_dict,paired_word)


if __name__ == "__main__":
	sorted_alpha_dict,sorted_word_dict,paired_word = receives_input()

	for n in range(5):
		print ("\n" + list(sorted_word_dict.keys())[n] + " (" + str(list(sorted_word_dict.values())[n]) + " occurances)")
		sorted_paired_dict = ({key: value for key, value in sorted(paired_word[list(sorted_word_dict.keys())[n]].items(), key=lambda item: item[1], reverse=True)})
		for m in range(3):
			print ("---" + list(sorted_paired_dict.keys())[m] + ":" + str(list(sorted_paired_dict.values())[m]) + "")

	print ("\nAlphabet frequency")
	for entry in sorted_alpha_dict:
		print (entry + " = " + str(sorted_alpha_dict[entry]))
	print ("\nTotal number of words = " + str(sum(sorted_word_dict.values())))
	print ("\nTotal number of unique words = " + str(len(sorted_word_dict)))
