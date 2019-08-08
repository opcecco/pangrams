#!/usr/bin/env python3

# import json
from puzzle import WordList
# from graphics import PuzzleImageWriter

with open('words/common_wordlist.txt', 'r') as common_word_file:
	common_wl = WordList(common_word_file, min_word_size = 4)

with open('words/full_wordlist.txt', 'r') as full_word_file:
	full_wl = WordList(full_word_file, min_word_size = 4)

p = common_wl.make_puzzle(1, 6)
print(p)

s = full_wl.solve_puzzle(p)
print(s)

# print(puzzle)

# with open('config.json', 'r') as config_file:
	# config = json.load(config_file)

# writer = PuzzleImageWriter(**config)
# writer.draw(puzzle, 'out.jpg')
