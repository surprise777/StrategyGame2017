"""module: chopstick_state(subclass of current_state)
"""
from typing import List
from current_state import State


class ChopstickState(State):
    """a class represent the state of the chopstick game, a subclass of State.
    """
    current_condition: List[int]

    def __init__(self) -> None:
        """initialize the class.
        extends State.__init__
        >>> chs1 = ChopstickState()
        >>> chs1.current_condition
        [1, 1, 1, 1]
        """
        State.__init__(self)
        self.current_condition = [1, 1, 1, 1]

    def __str__(self) -> str:
        """return the string represention of the chopstick game state.
        Overrides State.__str__
        >>> chs1 = ChopstickState()
        >>> print(chs1)
        Player 1: 1-1; Player 2: 1-1
        """
        player1 = 'Player 1: ' + str(self.current_condition[0]) + '-' \
                               + str(self.current_condition[1])
        player2 = 'Player 2: ' + str(self.current_condition[2]) + '-' \
                               + str(self.current_condition[3])
        return player1 + '; ' + player2

    def get_possible_moves(self) -> List[str]:
        """get a list of all possible valid moves of self chopstick game state.
        Overrides State.get_possible_moves
        >>> chs1 = ChopstickState()
        >>> chs1.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        """
        possible_list = ['ll', 'lr', 'rl', 'rr']
        sfl, sfr, opl, opr = 0, 1, 2, 3
        if self.current_player == 'p1':
            sfl = 0
            sfr = 1
            opl = 2
            opr = 3
        elif self.current_player == 'p2':
            sfl = 2
            sfr = 3
            opl = 0
            opr = 1
        if self.current_condition[sfl] == 0:
            if 'll' in possible_list:
                possible_list.remove('ll')
            if 'lr' in possible_list:
                possible_list.remove('lr')
        if self.current_condition[sfr] == 0:
            if 'rl' in possible_list:
                possible_list.remove('rl')
            if 'rr' in possible_list:
                possible_list.remove('rr')
        if self.current_condition[opl] == 0:
            if 'll' in possible_list:
                possible_list.remove('ll')
            if 'rl' in possible_list:
                possible_list.remove('rl')
        if self.current_condition[opr] == 0:
            if 'lr' in possible_list:
                possible_list.remove('lr')
            if 'rr' in possible_list:
                possible_list.remove('rr')
        return possible_list

    def is_valid_move(self, move: str) -> bool:
        """return True if the move from the str_to_move is valid.
        Overrides State.is_valid_move
        >>> chs1 = ChopstickState()
        >>> chs1.is_valid_move('mm')
        False
        """
        if move in ['ll', 'lr', 'rl', 'rr']:
            if self.current_player == 'p1':
                if move == 'll' or move == 'lr':
                    return self.current_condition[0] != 0
                if move == 'rl' or move == 'rr':
                    return self.current_condition[1] != 0
            elif self.current_player == 'p2':
                if move == 'll' or move == 'lr':
                    return self.current_condition[2] != 0
                if move == 'rl' or move == 'rr':
                    return self.current_condition[3] != 0
        return False

    def make_move(self, move_to_make: str) -> "ChopstickState":
        """return new current state class after changing the move of the game.
        Overrides State.make_move
        >>> chs1 = ChopstickState()
        >>> chs1.current_player = 'p1'
        >>> nchs = chs1.make_move('ll')
        >>> nchs.current_condition
        [1, 1, 2, 1]
        >>> nchs.current_player
        'p2'
        >>> chs1.current_condition
        [1, 1, 1, 1]
        """
        new_state = ChopstickState()
        if self.is_valid_move(move_to_make):
            if self.current_player == 'p1':
                self_left = self.current_condition[0]
                self_right = self.current_condition[1]
                if move_to_make == 'll':
                    op_left = (self.current_condition[2] + self_left) % 5
                    op_right = self.current_condition[3]
                    new_state.current_condition = [self_left, self_right,
                                                   op_left, op_right]
                elif move_to_make == 'lr':
                    op_left = self.current_condition[2]
                    op_right = (self.current_condition[3] + self_left) % 5
                    new_state.current_condition = [self_left, self_right,
                                                   op_left, op_right]
                elif move_to_make == 'rl':
                    op_left = (self.current_condition[2] + self_right) % 5
                    op_right = self.current_condition[3]
                    new_state.current_condition = [self_left, self_right,
                                                   op_left, op_right]
                elif move_to_make == 'rr':
                    op_left = self.current_condition[2]
                    op_right = (self.current_condition[3] + self_right) % 5
                    new_state.current_condition = [self_left, self_right,
                                                   op_left, op_right]
                new_state.current_player = 'p2'
            elif self.current_player == 'p2':
                self_left = self.current_condition[2]
                self_right = self.current_condition[3]
                if move_to_make == 'll':
                    op_left = (self.current_condition[0] + self_left) % 5
                    op_right = self.current_condition[1]
                    new_state.current_condition = [op_left, op_right,
                                                   self_left, self_right]
                elif move_to_make == 'lr':
                    op_left = self.current_condition[0]
                    op_right = (self.current_condition[1] + self_left) % 5
                    new_state.current_condition = [op_left, op_right,
                                                   self_left, self_right]
                elif move_to_make == 'rl':
                    op_left = (self.current_condition[0] + self_right) % 5
                    op_right = self.current_condition[1]
                    new_state.current_condition = [op_left, op_right,
                                                   self_left, self_right]
                elif move_to_make == 'rr':
                    op_left = self.current_condition[0]
                    op_right = (self.current_condition[1] + self_right) % 5
                    new_state.current_condition = [op_left, op_right,
                                                   self_left, self_right]
                new_state.current_player = 'p1'

        else:
            new_state = self
        return new_state


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
