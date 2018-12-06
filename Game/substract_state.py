"""module: substract_state(subclass of current_state)
"""
from typing import List
from current_state import State


class SubstractState(State):
    """a class represent state of the substrat square game, a subclass of State.
    """
    current_condition: int

    def __init__(self) -> None:
        """initialize the class. Defalt the initial current_codition value = 0.
        extends State.__init__
        >>> sss1 = SubstractState()
        >>> sss1.current_condition
        0
        """
        State.__init__(self)
        self.current_condition = 0

    def __str__(self) -> str:
        """return the string represention of the substractsquare game state.
        Overrides State.__str__
        >>> sss1 = SubstractState()
        >>> print(sss1)
        Now the substract number is: 0
        """
        return "Now the substract number is: {}".format(self.current_condition)

    def get_possible_moves(self) -> List[int]:
        """get a list of all possible valid moves of self substract game state.
        Overrides State.get_possible_moves
        >>> sss1 = SubstractState()
        >>> sss1.current_condition = 4
        >>> sss1.get_possible_moves()
        [1, 4]
        """
        move_list = []
        limit_square = int(self.current_condition**0.5)
        for i in range(1, limit_square + 1):
            move_list.append(i**2)
        return move_list

    def is_valid_move(self, move: int) -> bool:
        """return True if the move from the str_to_move is valid.
        Overrides State.is_valid_move
        >>> sss1 = SubstractState()
        >>> sss1.is_valid_move(10)
        False
        """
        if move in self.get_possible_moves():
            return True
        return False

    def make_move(self, move_to_make: int) -> "SubstractState":
        """return new current state class after changing the move of the game.
        Overrides State.make_move
        >>> sss1 = SubstractState()
        >>> sss1.current_condition = 6
        >>> sss1.current_player = 'p2'
        >>> nsss = sss1.make_move(4)
        >>> nsss.current_condition
        2
        >>> nsss.current_player
        'p1'
        >>> sss1.current_condition
        6
        """
        new_state = SubstractState()
        new_player = 'p2'
        if self.current_player == 'p2':
            new_player = 'p1'
        if self.is_valid_move(move_to_make):
            new_state.current_player = new_player
            new_state.current_condition = self.current_condition - move_to_make
        else:
            new_state = self
        return new_state


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
