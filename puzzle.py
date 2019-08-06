#!/usr/bin/env python3

from string import ascii_lowercase
from collections import namedtuple
from random import choice, shuffle


Word = namedtuple('Word', ['original', 'letter_set'])
Puzzle = namedtuple('Puzzle', ['key_letter', 'letters', 'pangrams', 'solutions'])


class PuzzleGenerator:

	def __init__(self, full_str_iter, seed_str_iter = None, valid_chars = ascii_lowercase, min_word_size = 4, puzzle_size = 7):

		self.valid_chars = set(valid_chars)
		self.min_word_size = min_word_size
		self.puzzle_size = puzzle_size

		# Get the full valid word list
		full_word_iter = (Word(w, set(w)) for w in map(str.lower, full_str_iter))
		self.full_word_list = [
			w for w in full_word_iter
			if len(w.original) >= self.min_word_size
			and len(w.letter_set) <= self.puzzle_size
			and w.letter_set <= self.valid_chars
		]

		# Get list of words to seed the panagram
		if seed_str_iter is not None:
			seed_word_iter = (Word(w, set(w)) for w in map(str.lower, seed_str_iter))
			self.seed_word_list = [
				w for w in seed_word_iter
				if len(w.letter_set) == self.puzzle_size
				and w.letter_set <= self.valid_chars
			]
		else:
			self.seed_word_list = [w for w in self.full_word_list if len(w.letter_set) == self.puzzle_size]


	def generate(self):

		# Pick a seed panagram from the seed words list
		first_pangram = choice(self.seed_word_list)

		# Generate the puzzle
		puzzle_letters = list(first_pangram.letter_set)
		shuffle(puzzle_letters)
		key_letter = puzzle_letters.pop()

		# Return a Puzzle tuple including solutions
		return Puzzle(
			key_letter,
			''.join(puzzle_letters),
			sorted((w.original for w in self.full_word_list if w.letter_set == first_pangram.letter_set), key = len, reverse = True),
			sorted((w.original for w in self.full_word_list if w.letter_set < first_pangram.letter_set and key_letter in w.letter_set), key = len, reverse = True)
		)
