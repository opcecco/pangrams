#!/usr/bin/env python3

import json
import sys
from puzzle import Puzzle
from graphics import PuzzleImageWriter


with open('config.json', 'r') as config_file:
	config = json.load(config_file)

p = PuzzleImageWriter(**config)
p.draw(Puzzle(sys.argv[1], sys.argv[2], [], []), 'out.jpg')
