#!/usr/bin/env python3

from string import ascii_lowercase
from collections import namedtuple
from random import choice, sample


Word = namedtuple('Word', ['original', 'letter_set'])
Puzzle = namedtuple('Puzzle', ['key_letter', 'letters', 'pangrams', 'solutions'])


class PuzzleGenerator:

	def __init__(self, str_word_iter, valid_chars = set(ascii_lowercase), min_word_size = 4, puzzle_size = 7):

		self.valid_chars = valid_chars
		self.min_word_size = min_word_size
		self.puzzle_size = puzzle_size

		word_iter = (Word(w, set(w)) for w in map(str.lower, str_word_iter))
		self.word_list = [
			w for w in word_iter
			if len(w.original) >= self.min_word_size
			and len(w.letter_set) <= self.puzzle_size
			and w.letter_set <= self.valid_chars
		]


	def generate(self, max_pangram_size = None):

		if max_pangram_size is None:
			max_pangram_size = self.puzzle_size

		first_pangram = choice([
			w for w in self.word_list
			if len(w.letter_set) == self.puzzle_size
			and len(w.original) <= max_pangram_size
		])

		puzzle_letters = list(first_pangram.letter_set)
		key_letter = choice(puzzle_letters)
		puzzle_letters.remove(key_letter)

		return Puzzle(
			key_letter,
			''.join(sample(puzzle_letters, len(puzzle_letters))),
			sorted((w.original for w in self.word_list if w.letter_set == first_pangram.letter_set), key = len, reverse = True),
			sorted((w.original for w in self.word_list if w.letter_set < first_pangram.letter_set and key_letter in w.letter_set), key = len, reverse = True)
		)
