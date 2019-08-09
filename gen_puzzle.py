#!/usr/bin/env python3

import json
from puzzle import WordList
from graphics import PuzzleImageWriter

with open('words/common_wordlist.txt', 'r') as common_word_file:
	common_wl = WordList(common_word_file, min_word_size = 4)

with open('words/full_wordlist.txt', 'r') as full_word_file:
	full_wl = WordList(full_word_file, min_word_size = 4)

with open('1-6-config.json', 'r') as config_file:
	config = json.load(config_file)
	writer = PuzzleImageWriter(**config)

puz = common_wl.make_puzzle(1, 6)
sol = full_wl.solve_puzzle(puz)

print(puz, sol)
writer.draw(puz, sol, 'out.jpg')
