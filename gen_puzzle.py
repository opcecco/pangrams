#!/usr/bin/env python3

import json
from puzzle import PuzzleGenerator
from graphics import PuzzleImageWriter

with open('words/full_wordlist.txt', 'r') as full_word_file, open('words/common_wordlist.txt', 'r') as common_word_file:
	full = (line.strip() for line in full_word_file)
	common = (line.strip() for line in common_word_file)
	generator = PuzzleGenerator(full, common, puzzle_size = 9)

puzzle = generator.generate()

# print('Puzzle:\n')
# print(' %c %c \n%c %c %c\n %c %c ' % (*puzzle.letters[:3].upper(), puzzle.key_letter.upper(), *puzzle.letters[3:].upper()))
# print('\nPangrams:\n')
# print(', '.join(puzzle.pangrams))
# print('\nSolutions:\n')
# print(', '.join(puzzle.solutions))

print(puzzle)

with open('config.json', 'r') as config_file:
	config = json.load(config_file)

writer = PuzzleImageWriter(**config)
writer.draw(puzzle, 'out.jpg')
