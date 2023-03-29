#!/usr/bin/env python

from tetris_objects import Figure
from random import choice, randrange
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

# Block
shape = np.array([(-1, 0), (-1, 1), (0, 0), (0, -1)])

# Create block object from class Figure
blockShape = np.array([])
block = Figure(shape, color)

logging.debug(f"block color : {block.getColor()}")
logging.debug(f"block shape :  {block.getShape()}")

# iShape

# Shape of i-shape
shape = np.array([(0, 0), (0, -1), (0, 1), (1, -1)])

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

iShape = Figure(shape, color)

logging.debug(f"iShape color : {iShape.getColor()}")
logging.debug(f"iShape shape :  {iShape.getShape()}")

logging.debug("Rotate counterclockwise")
iShape.rotate()

logging.debug(f"iShape color : {iShape.getColor()}")
logging.debug(f"iShape shape :  {iShape.getShape()}")

shape = np.array(
    [(-1, 0), (-1, 1), (0, 0), (0, -1)],
)
zShape = Figure(shape, color)
zShape.rotate()

