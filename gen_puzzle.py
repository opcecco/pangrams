#!/usr/bin/env python3

import json

from puzzle import *
from graphics import *


# Create wordlists from files
with open('words/common_wordlist.txt', 'r') as common_word_file, open('words/full_wordlist.txt', 'r') as full_word_file:
	common_wl = WordList(common_word_file, min_word_size = 4)
	full_wl = WordList(full_word_file, min_word_size = 4)

# Generate a puzzle and get its solutions
puz = common_wl.make_puzzle(1, 6)
sol = full_wl.solve_puzzle(puz)
print(puz)
print(sol)

# Load an image writer config
with open('default_config.json', 'r') as config_file:
	config = json.load(config_file)

# Write the puzzle out to an image
writer = PuzzleImageWriter(**config)
writer.draw(puz, sol, 'out.jpg')
