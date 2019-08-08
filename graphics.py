#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont


class PuzzleImageWriter:

	def __init__(self, **kwargs):

		for key in kwargs:
			setattr(self, key, kwargs[key])


	def draw(self, puzzle, solution, output_file):

		image = Image.open(self.background_file)
		draw = ImageDraw.Draw(image)

		font = ImageFont.truetype('DejaVuSans-Bold.ttf', size = 24)
		color = 'rgb(0, 0, 0)'

		num_pans = len(solution.pangram_words)
		text = '%d pangram%s' % (num_pans, 's' if num_pans > 1 else '')
		draw.text((10, 10), text, fill = color, font = font)

		font = ImageFont.truetype('DejaVuSans-Bold.ttf', size = 80)
		color = 'rgb(0, 0, 0)'

		x, y = self.key_letter_loc
		text = puzzle.key_letters[0].upper()
		w, h = font.getsize(text)
		draw.text((x - (w / 2), y - (h / 2)), text, fill = color, font = font)

		for text, loc in zip(puzzle.general_letters.upper(), self.letter_locs):
			x, y = loc
			w, h = font.getsize(text)
			draw.text((x - (w / 2), y - (h / 2)), text, fill = color, font = font)

		image.convert('RGB').save(output_file, optimize = True)
