#!/usr/bin/env python3

from puzzle import PuzzleGenerator


with open('/usr/share/dict/words') as word_file:
	generator = PuzzleGenerator((line.strip() for line in word_file), puzzle_size = 7)

puzzle = generator.generate(max_pangram_size = 7)

print(puzzle)

# print('Puzzle:\n')
# print(' %c %c \n%c %c %c\n %c %c ' % (*puzzle.letters[:3].upper(), puzzle.key_letter.upper(), *puzzle.letters[3:].upper()))

# print('\nPangrams:\n')
# print(', '.join(puzzle.pangrams))

# print('\nSolutions:\n')
# print(', '.join(puzzle.solutions))
