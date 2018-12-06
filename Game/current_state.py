"""module: current_state (SuperClass)
"""
from typing import Any


class State:
    """a class represent the state of class.
    current_player - the player name who is permitted to play this turn.
    current_condition - the current condition of the state of the game
    """

    current_player: str
    current_condition: str

    def __init__(self) -> None:
        """initialize the class.
        >>> st1 = State()
        """
        self.current_player = ''
        self.current_condition = ''

    def __str__(self) -> str:
        """return the string represention of the class.
        """
        raise NotImplementedError("Must implement a subclass!")

    def __eq__(self, other: "State") -> bool:
        """compare if self is equivalent to the other.
        """
        return type(self) == type(other) and \
            self.current_condition == other.current_condition and \
            self.current_player == other.current_player

    def get_possible_moves(self) -> list:
        """get a list of all possible moves of self game which are valid.
        """
        raise NotImplementedError("Must implement a subclass!")

    def is_valid_move(self, move: Any) -> bool:
        """return True if the move from the str_to_move is valid.
        """
        raise NotImplementedError("Must implement a subclass!")

    def make_move(self, move_to_make: Any) -> "State":
        """return new current state class after changing the move of the game.
        """
        raise NotImplementedError("Must implement a subclass!")

    def get_current_player_name(self) -> str:
        """return the current player's name of the self game.
        >>> st1 = State()
        >>> st1.current_player ='a'
        >>> st1.get_current_player_name()
        'a'
        """
        return self.current_player


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
