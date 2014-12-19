import unittest
from random import choice
"""
THIRD UPDATE
-----------
Lovely. Shit just works: http://www.codeskulptor.org/#user38_DjCBcO6l1q_6.py
same score and report as above.

SECOND UPDATE
------------
New URL: http://www.codeskulptor.org/#user38_DjCBcO6l1q_5.py

Score: 70.0/100

Everything seems to be working this time.

===Unit Test Failures===
[-12.0 pts]
game = TwentyFortyEight(4, 5)
game.move(UP)

Input board:
[[8, 16, 8, 16, 8],
 [16, 8, 16, 8, 16],
 [8, 16, 8, 16, 8],
 [16, 8, 16, 8, 16]]
 ==> Game Over! at line 239, in new_tile
[-10.0 pts]
game = TwentyFortyEight(1, 1)
game.new_tile()
 ==> set tile (0, 0) with frequencies {2: 1.0, 4: 0.0} instead of {2: .9, 4: .1}
[-8.0 pts] 4 style warnings found (maximum allowed: 10 style warnings)

===General Code Warnings===
[line 106] Expression "[self.free_tiles.add((row, col)) if self[(row, col)] == 0 else self._update_used_tiles(row, col) for row in xrange(self.grid_height) for col in xrange(self.grid_width)]" is assigned to nothing
    function "TwentyFortyEight._update_tiles", line 106
[line 192] Unused variable 'moved'
    function "TwentyFortyEight.move", line 192

===Code Convention Warnings===
[line 132] Invalid name "up" (should match [a-z_][a-z0-9_]{2,30}$)
    function "TwentyFortyEight.reset", line 132

===Refactoring Warnings===
[line 70] Too many instance attributes (17/15)
    function "TwentyFortyEight", line 70

===FIRST UPDATE===
-------------------
I completed this in under 8 hrs.

Game plays out just like Original 2048. Unbelievable.

Results in OwlTests: Score: 70.0/100

Unit Test Failures:
[-12.0 pts]
game = TwentyFortyEight(4, 5)
game.move(UP)

Input board:
[[8, 16, 8, 16, 8],
 [16, 8, 16, 8, 16],
 [8, 16, 8, 16, 8],
 [16, 8, 16, 8, 16]]
 ==> Game Over! at line 190, in new_tile
[-10.0 pts]
game = TwentyFortyEight(1, 1)
game.new_tile()
 ==> set tile (0, 0) with frequencies {2: 1.0, 4: 0.0} instead of {2: .9, 4: .1}
[-8.0 pts] 4 style warnings found (maximum allowed: 10 style warnings)
---------------------------------------------------------------------------

For warnings on original code refer here: http://www.codeskulptor.org/#user38_DjCBcO6l1q_0.py

[line 57] More than one statement on a single line
    function "merge", line 57
[line 90] Invalid name "up" (should match [a-z_][a-z0-9_]{2,30}$)
    function "TwentyFortyEight.reset", line 90
[line 182] More than one statement on a single line
    function "TwentyFortyEight.new_tile", line 182
[line 190] More than one statement on a single line
    function "TwentyFortyEight.new_tile", line 190
----------------------------------------------------
PS: While playing, Line 117: IndexError: list index out of range after a long period.

"""

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    line: list like [8, 0, 16, 0, 16, 8]
    returns: merged list [8, 32, 8, 0]
    loop cur pos and index in list:
        if two equal numbers seperated by 0s, double the previous index and replace number at current position with 0
        elsif 0 and a number, swap recursively until it hits a nonzero number

    """
    prev_index = zero = zero_index = 0
    used_index = []
    for index, current_num in enumerate(line):
        #if index == 0: prev_index = 0
        #print "\n"
        #print "current_num:{} | index:{}".format(current_num, index)
        #if cur number = last nonzero number and its not 0 and prev and present index are not equal
        if current_num == line[prev_index] and current_num != 0 and prev_index != index and prev_index not in used_index:
            used_index.append(prev_index)
            line[prev_index] += current_num
            current_num = line[index] = 0
            zero = 1
            #zero_index = index
        #all abt shifting non-zeros fwd and checking zero continuity
        #print "zero:{}".format(zero)
        #if its 0 then set continuous  zero status to 1 and as latest zero index
        if current_num == 0:
            zero = 1
            zero_index = index
        elif current_num != 0 and zero == 1:
            #if its a nonzero and zero status is ON
            zero = 0
            while line[zero_index] == 0:
                #shift number forward till it hits a non-zero
                zero_index -= 1
                if zero_index < 0: break;
            zero_index += 1
            line[zero_index]= current_num
            line[index] = 0
            #current pos is 0 so set zero status
            zero = 1
            prev_index = zero_index
            #print "line:{} | prev_index:{} | zero_index:{}".format(line, prev_index, zero_index)
        else: prev_index = index  #if its a non zero but zero status OFF
    del prev_index, zero, zero_index, used_index
    return line

class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.cells = self.grid_height * self.grid_width
        self.reset()

    def _update_used_tiles(self, row, col):
        """update used tiles"""
        #add to used tiles
        self.all_tiles_used.add((row,col))
        #remove from free tiles
        self.free_tiles.difference_update(self.all_tiles_used)
        if self[(row,col)] == 2048:
            self.win_tile.append((row, col))

    def _update_free_tiles(self, row, col):
        """
        update free tiles
        """
        self.free_tiles.add((row,col))
        #remove from used tiles
        self.all_tiles_used.difference_update(self.free_tiles)


    def _update_tiles(self):
        """
        update all tiles
        """
        print "In _update tiles"
        self.all_tiles_used.clear()
        self.free_tiles.clear()
        [self.free_tiles.add((row,col)) if self[(row,col)] == 0 else self._update_used_tiles(row, col)\
        for row in xrange(self.grid_height)\
        for col in xrange(self.grid_width)]
        self.empty_cells = len(self.free_tiles)
        #print "empty_cells {} | len(self.all_tiles_used) {} | total cells {}".format(self.empty_cells, len(self.all_tiles_used), self.cells)
        #print "free tiles {} | all tiles used {}".format(self.free_tiles, self.all_tiles_used)
        assert len(self.all_tiles_used) + self.empty_cells == self.cells

    def reset(self):
        """
        1. Reset the game so the grid is empty.
        2. Fills in the right index sequence in all directions
        3. updates free and filled tiles

        OFFSETS = {UP: (1, 0),
                   DOWN: (-1, 0),
                   LEFT: (0, 1),
                   RIGHT: (0, -1)}
        """
        self.total_occur = self.two = self.four = 0
        self.empty_cells = self.cells
        self.all_tiles_used = set()
        #choices for for new random tiles
        self.free_tiles = set()
        self.win_tile = []
        self._grid = []
        self.up, self.down, self.left, self.right  = [], [], [], []
        #check if there are empty cells
        self.moved = 0  #check if there were any moved tiles

        self._grid.extend([[0]*self.grid_width for _ in xrange(self.grid_height)])

        self.orientation = dict(((k, v) for k,v in zip(OFFSETS,(self.up, self.down, self.left, self.right))))

        for direction in (UP, DOWN, LEFT, RIGHT):
            orient = OFFSETS[direction]
            start = 0 if (direction == UP or direction == LEFT) else self.grid_height-1
            ##NOTE: FIXED scaling LEFT RIGHT by rows and UP DOWN by cols
            if direction == LEFT or direction == RIGHT:
                #goes by rows
                self.grid_orient = self.grid_height
            else: self.grid_orient = self.grid_width  #goes by cols
            for col in xrange(self.grid_orient):
                t_list = []
                if direction == LEFT or direction == RIGHT:
                    sum_offset = (col, start)
                else: sum_offset = (start, col)
                t_list.append(sum_offset)
                for _ in xrange(self.grid_height - 1):
                    sum_offset = sum_offset[0] + orient[0], sum_offset[1] + orient[1]
                    t_list += [sum_offset]
                self.orientation[direction].append(t_list)

        self._update_tiles()
        return self._grid

    def __getitem__(self, key):
        return self._grid[key[0]][key[1]]

    def __setitem__(self, key, value):
        self._grid[key[0]][key[1]] = value

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "="*3 + "The Grid" + "="*3 + "\n {}\n".format(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        print "in move"
        self.moved = 0
        for lists in self.orientation[direction]:
            original_config = [self[r,c] \
            for r in xrange(self.grid_height)\
            for c in xrange(self.grid_width)]
            temp_list = [self[rowcol_index] for rowcol_index in lists]
            for new_val, rc_index in zip(merge(temp_list), lists):
                self[rc_index] = new_val

            original_0board = all([l == 0 for l in original_config])
            after_move_board = (original_config != [self[r,c] \
            for r in xrange(self.grid_height)\
            for c in xrange(self.grid_width)])
            #if original line is different after merging/moving and moved=0
            if after_move_board and not self.moved:
                self.moved = 1
        #if nothing has moved because no cells are empty
        if not self.moved and self.empty_cells == 0:
            print "GAME OVER!"
            print self.moved
            raise Exception("Game Over!")
        self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        print "in new tile"
        #update free and filled tiles
        self._update_tiles()
        if self.win_tile:
            return "YOU WIN!"
        print "empty cells "+ str(self.empty_cells)

        if self.empty_cells != 0:
            if self.cells == 1:
                num = 2
            elif not self.total_occur:
                num = 2
                self.two += 1
            else:
                if self.two/float(self.total_occur) < 0.9:
                    num = 2
                    self.two += 1
                else:
                    num = 4
                    self.four += 1
            #get total 2s and 4s occurences
            self.total_occur = self.two + self.four

            tile_val = choice(tuple(self.free_tiles))
            self.set_tile(tile_val[0], tile_val[1], num)
            assert self[tile_val] == num
            self._update_tiles()
        else: raise Exception("Game Over!")

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self[(row,col)] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self[(row,col)]



if __name__ == "__main__":
    line = [2, 0, 2, 4]
    merge(line)
    #print line
    assert line != [2, 0, 2, 4]
    assert merge([2, 0, 2, 4]) == [4, 4, 0, 0]
    assert merge([0, 0, 2, 2]) == [4, 0, 0, 0]
    assert merge([2, 2, 0, 0]) == [4, 0, 0, 0]
    assert merge([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert merge([8, 16, 16, 8]) == [8, 32, 8, 0]
    #print merge([0,2,4,2])
    assert merge([0,2,4,2]) == [2,4,2,0]
    assert merge([0,0,0,4,0]) == [4,0,0,0,0]
    assert merge([0,4,0,0,0]) == [4,0,0,0,0]

    game = TwentyFortyEight(20, 20)
    #print game
    assert game[(19,19)] == game.get_tile(19,19)

    #game[(19,19)] = 98
    #assert game[(19,19)] == 98
    #print game
    game = TwentyFortyEight(4, 4)
    game.new_tile()
    print game
    game.move(1)  #UP
    print game

    game.move(2)  #DOWN
    print game

    game.move(3)  #LEFT
    #print game

    game.move(4)  #RIGHT
    print game

    game = TwentyFortyEight(4,5)

    #set random tiles in game board
    for row in xrange(4):
        for col in xrange(5):
            game[(row,col)] = choice((0, 2, 4))
    print game
    #print game.up
    #print game.down
    #print game.left
    #print game.right

    game.move(1)  #UP
    print game

    game.move(2)  #DOWN
    print game

    game.move(3)  #LEFT
    #print game

    game.move(4)  #RIGHT
    print game

    from cProfile import run
    run("TwentyFortyEight(5, 5)")
    run("game.move(1)")  #UP

    run ("game.move(2)")  #DOWN

    run ("game.move(3)")  #LEFT

    run ("game.move(4)")  #RIGHT

    #=======#

    run("TwentyFortyEight(4,5)")
