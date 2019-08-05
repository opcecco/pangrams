#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont


class PuzzleImageWriter:

	def __init__(self, **kwargs):

		for key in kwargs:
			setattr(self, key, kwargs[key])


	def draw(self, puzzle, output_file):

		image = Image.open(self.background_file)
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('DejaVuSans-Bold.ttf', size = 80)
		color = 'rgb(0, 0, 0)'

		x, y = self.key_letter_loc
		text = puzzle.key_letter.upper()
		w, h = font.getsize(text)
		draw.text((x - (w / 2), y - (h / 2)), text, fill = color, font = font)

		for text, loc in zip(puzzle.letters.upper(), self.letter_locs):
			x, y = loc
			w, h = font.getsize(text)
			draw.text((x - (w / 2), y - (h / 2)), text, fill = color, font = font)

		image.convert('RGB').save(output_file, optimize = True)
