'''
This file is used to define the type of go game.
'''

import enum
from  collections import namedtuple

# Define the players of go game.
class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white

# Define the point of go game.
class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        '''
        Get the neighbors of the point.
        :return: the neighbors of the point.
        '''
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1)
        ]