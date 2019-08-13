#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont


class PuzzleImageWriter:

	def __init__(self, **kwargs):

		for key in kwargs:
			setattr(self, key, kwargs[key])


	def draw(self, puzzle, solution, output_file):

		image = Image.open(self.background_file)
		draw = ImageDraw.Draw(image)

		font = ImageFont.truetype(self.letter_font, size = self.letter_font_size)
		color = self.letter_font_color

		for text, loc in zip(puzzle.key_letters.upper(), self.key_letter_locs):
			x, y = loc
			w, h = font.getsize(text)
			draw.text((x - (w / 2), y - (h / 2)), text, fill = color, font = font)

		for text, loc in zip(puzzle.general_letters.upper(), self.general_letter_locs):
			x, y = loc
			w, h = font.getsize(text)
			draw.text((x - (w / 2), y - (h / 2)), text, fill = color, font = font)

		image.convert('RGB').save(output_file, optimize = True)
