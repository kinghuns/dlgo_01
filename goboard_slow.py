import copy
from gotypes import Player, Point

#define move class
#move is the action of a player in a turn
#play is the action of a player to put a stone on the board
#pass is the action of a player to pass the turn
#resign is the action of a player to resign the game
class Move():
    def __init__(self, point = None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign
    
    @classmethod
    def play(cls, point):
        return Move(point=point)
    
    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)
    
    @classmethod
    def resign(cls):
        return Move(is_resign=True)

'''
define go string class
'''
#引入棋链的概念用以表达同色相连的一组棋子
#liberty是气的概念
#如何构建单元测试用以测试GoString类
class GoString():
    def __init__(self, color, stones, liberties) :
        self.color = color 
        self.stones = set(stones)
        self.liberties = set(liberties)
    
    def remove_liberty(self, point):
        self.liberties.remove(point)

    def add_liberty(self, point):
        self.liberties.add(point)
    
    def merged_with(self, go_string):
        assert go_string.color == self.color
        combined_stones = self.stones | go_string.stones
        return GoString(
            self.color,
            combined_stones,
            (self.liberties | go_string.liberties) - combined_stones
        )
    
    @property
    def num_liberties(self):
        return len(self.liberties)
    
    def __eq__(self, other):
        return isinstance(other, GoString) and \
            self.color == other.color and \
            self.stones == other.stones and \
            self.liberties == other.liberties

class Board():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}

    #3-6 检查相邻点的气数
    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        adjacent_same_color =[]
        adjacent_oppsite_color = []
        liberties = []
        for neighbor in point.neighbors():
            if not self.is_on_grid(neighbor):
                continue
            neighbor_string = self._grid.get(neighbor)
            if neighbor_string is None:
                liberties.append(neighbor)
            elif neighbor_string.color == player:
                if neighbor_string not in adjacent_same_color:
                    adjacent_same_color.append(neighbor_string)
            else:
                if neighbor_string not in adjacent_oppsite_color:
                    adjacent_oppsite_color.append(neighbor_string)
        new_string = GoString(player,[point], liberties)
        for same_color_string in adjacent_same_color:
            new_string = new_string.merged_with(same_color_string)
        for new_string_point in new_string.stones:
            self._grid[new_string_point] = new_string
        for other_color_string in adjacent_oppsite_color:
            other_color_string.remove_liberty(point)
        for other_color_string in adjacent_oppsite_color:
            if other_color_string.num_liberties == 0:
                self._remove_string(other_color_string)
    
    def _remove_string(self, string):
        for point in string.stone:
            for neighbor in point.neighbors():
                neighbor_string = self._grid.get(neighbor)
                if neighbor_string is None:
                    continue
                if neighbor_string is not string:
                    neighbor_string.add_liberty(point)
            self._grid[point] = None
        
    
    #3-7 提子和落子
    def is_on_grid(self, point):
        return 1 <= point.row <= self.num_rows and \
            1 <= point.col <= self.num_cols
    
    def get(self, point):
        string = self._grid.get(point)
        if string is None:
            return None
        return string.color
    
    def get_go_string(self, point):
        string = self._grid.get(point)
        if string is None:
            return None
        return string

#3-10 存储状态。
# 对于各种AI参与的棋类游戏来说，回溯是比较其估值的一个必须的环节。
class GameState():
    def __init__(self, board, next_player, previous, move):
        self.board = board
        self.nex_player = next_player
        self.previous = previous
        self.move = move


new_string = None
new_string = GoString(Player.black, 
                              [Point(1,1), Point(1,2)],
                              [Point(0,1), Point(0,2), Point(1,0), Point(1,3), Point(2,1), Point(2,2)])
new_string.remove_liberty(Point(0,2))