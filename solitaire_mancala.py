"""
What I learnt in this exercise is
initializing a mutable DS like list
and then again reassigning in set_board, when doing any arithmetic assignment over the DS/list, one has to use self.DS/slots and merely self[index] +- = number doesn't work. id(self[index]) is id(self.slots[index]) comes False

Advice: Instead of object, could subclass this as a list subclass.
"""

class SolitaireMancala(object):

    def __init__(self):
        """object whose configuration consists of a board with an empty store and no houses"""
        self.slots = [0]  #original 0 store
        self.len = self.__len__

    def __len__(self):
        return len(self.slots)

    def __getitem__(self, house_num):
        return self.slots[house_num] if 0<=house_num<self.len() else None

    def __setitem__(self, house_num, seed_val):
        if self[house_num]: self.slots[house_num] = seed_val

    def __iter__(self): return iter(self.slots)

    def __getslice__(self, start = None, end = None, step = None):
        return self.slots[slice(start, end, step)]

    def __str__(self):
        """Return a string corresponding to the current configuration of the Mancala board. This string is formatted as a list with the store appearing in the rightmost (last) entry. Consecutive entries should be separated by a comma and blank (as done by Python when converting a list to a string)."""
        return '[' + ', '.join(map(str,self.slots[::-1])) + ']'

    def set_board(self, configuration):
        """Set the board to be a copy of the supplied configuration (to avoiding referencing issues). The configuration will be a list of integers."""
        config = tuple(configuration)
        self.slots = list(config)

    def get_num_seeds(self, house_num):
        """Return the number of seeds in the house with index house_num. Note that house 0 corresponds to the store."""
        return self[house_num]

    def is_legal_move(self, house_num):
        """Return True if moving the seeds from house house_num is legal. Otherwise, return False. If house_num is zero, is_legal_move should return False."""
        return True if house_num == self[house_num] and house_num != 0 else False

    def apply_move(self, house_num):
        """ Apply a legal move for house house_num to the board."""
        if self.is_legal_move(house_num):
            seed = house_num
            #print "seed: {} prev_house:{} self[prev_house]:{}".format(seed, house_num, self[house_num])
            for prev_house in xrange(house_num-1,-1,-1):
                self.slots[prev_house] += 1
                seed -= 1
                #print "len: {} seed: {} prev_house:{} self[prev_house]:{}".format(self.len(), seed, prev_house, self[prev_house])
            self[house_num] = seed

    def choose_move(self):
        """Return the index for the legal move whose house is closest to the store. If no legal move is available, return 0."""
        #min(self.slots, key = lambda X: X < self.len ? X == self.slots[X] : )
        for house_num in xrange(1,self.len()):
            if self.is_legal_move(house_num):
                return house_num
        return 0

    def is_game_won(self):
        """Return True if all houses contain no seeds. Return False otherwise."""
        return all([num == 0 for num in self[1:]])

    def plan_moves(self):
        """Given a Mancala game, return a list of legal moves computed to win the game if possible. In computing this sequence, the method repeatedly chooses the move whose house is closest to the store when given a choice of legal moves. Note that this method should not update the current configuration of the game."""
        backup = tuple(self)
        move_num = []
        status_num = self.choose_move()
        #while anything but 0
        while status_num:
            self.apply_move(status_num)
            move_num.append(status_num)
            status_num = self.choose_move()
        self.slots = list(backup)
        del backup
        return move_num

if __name__ == "__main__":

    config1 = [0, 0, 1, 1, 3, 5]
    game = SolitaireMancala()
    game.set_board(config1)

    assert str(game) == str(list(reversed(config1)))
    assert game.get_num_seeds(1) == config1[1]
    assert game.get_num_seeds(3) == config1[3]
    assert game.get_num_seeds(5) == config1[5]

    assert game.is_game_won() == False

    config2 = [1,0,0]
    game.set_board(config2)
    assert game.is_game_won() == True

    game.set_board(config1)
    #print game
    assert game.is_legal_move(0) == False
    assert game.is_legal_move(5) == True
    game.apply_move(5)
    #print str(game)
    assert str(game)  == str([0, 4, 2, 2, 1, 1])
    assert config1 == [0, 0, 1, 1, 3, 5]

    config3 = [1, 1, 2, 2, 4, 0]
    game.set_board(config3)
    assert game.is_legal_move(3) == False
    game.apply_move(3)
    assert str(game) == str([0, 4, 2, 2, 1, 1])

    game.set_board(config1)
    move = game.choose_move()
    assert move == 5
    game.apply_move(move)
    assert str(game) == str([0, 4, 2, 2, 1, 1])

    config6 = [0, 0, 1]
    game.set_board(config6)
    move = game.choose_move()
    assert move == 0

    game.set_board(config3)
    move_list = game.plan_moves()
    assert move_list == [1, 2, 1, 4, 1, 3, 1, 2, 1]

    for move in move_list:
        game.apply_move(move)
    assert str(game) == str([0, 0, 0, 0, 0, 10])

    config5 = [0, 0, 0, 3]
    game.set_board(config5)
    move_list = game.plan_moves()
    assert move_list == [3, 1]
