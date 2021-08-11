#!/usr/bin/env python3

from string import ascii_lowercase
from collections import namedtuple
from random import choice, shuffle
from functools import lru_cache
import json


class Word:

	def __init__(self, string, letter_set):

		self.string = string
		self.letter_set = letter_set

	def __repr__(self):

		return json.dumps({'string': self.string, 'letter_set': list(self.letter_set)})


class Puzzle:

	def __init__(self, key_letters, general_letters):

		self.key_letters = key_letters
		self.general_letters = general_letters

	def __repr__(self):

		return json.dumps({'key_letters': list(self.key_letters), 'general_letters': list(self.general_letters)})


class Solution:

	def __init__(self, pangram_words, general_words):

		self.pangram_words = pangram_words
		self.general_words = general_words

	def __repr__(self):

		return json.dumps({'pangram_words': sorted(list(self.pangram_words)), 'general_words': sorted(list(self.general_words))})


class WordList:

	def __init__(self, word_line_iter, min_word_size = 0, max_word_size = 99, valid_chars = ascii_lowercase):

		self.min_word_size = min_word_size
		self.max_word_size = max_word_size
		self.valid_chars = set(valid_chars)

		word_iter = (Word(raw, set(raw)) for raw in (line.strip().lower() for line in word_line_iter))
		self.words = [
			word for word in word_iter
			if self.min_word_size <= len(word.string) <= self.max_word_size
			and word.letter_set <= self.valid_chars
		]


	@lru_cache()
	def get_puzzle_words(self, puzzle_size):

		return [word for word in self.words if len(word.letter_set) == puzzle_size]


	def make_puzzle(self, num_key_letters, num_general_letters):

		seed_word = choice(self.get_puzzle_words(num_key_letters + num_general_letters))

		puzzle_letters = list(seed_word.letter_set)
		shuffle(puzzle_letters)
		key_letters = [puzzle_letters.pop() for i in range(num_key_letters)]

		return Puzzle(''.join(key_letters), ''.join(puzzle_letters))


	def solve_puzzle(self, puzzle):

		key_letter_set = set(puzzle.key_letters)
		total_letter_set = set(puzzle.key_letters + puzzle.general_letters)

		pangram_words = set(word.string for word in self.words if word.letter_set == total_letter_set)
		general_words = set(word.string for word in self.words if word.letter_set < total_letter_set and word.letter_set >= key_letter_set)

		return Solution(pangram_words, general_words)
