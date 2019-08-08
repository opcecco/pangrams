#!/usr/bin/env python3

from string import ascii_lowercase
from collections import namedtuple
from random import choice, shuffle


Word = namedtuple('Word', ['string', 'letter_set'])
Puzzle = namedtuple('Puzzle', ['key_letters', 'general_letters'])
Solution = namedtuple('Solution', ['pangram_words', 'general_words'])


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


	def make_puzzle(self, num_key_letters, num_general_letters):

		puzzle_size = num_key_letters + num_general_letters
		seed_word = choice([word for word in self.words if len(word.letter_set) == puzzle_size])

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
