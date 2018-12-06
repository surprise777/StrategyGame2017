"""module: game
"""
from typing import Any
from current_state import State


class Game:
    """superclass of all game
    game has the difference of whose turn
    """
    current_state: "State"

    def __init__(self, turn: bool) -> None:
        """
        initialize the game. who play first depending on turn(True for player 1)
        """
        if turn:
            self.current_state = State()

    def __str__(self) -> str:
        """
        return the string representation of the game
        """
        raise NotImplementedError("Must implement a subclass!")

    def __eq__(self, other: "Game") -> bool:
        """compare if self is equvalent with other.
        """
        return type(self) == type(other) and \
            self.current_state == other.current_state

    def str_to_move(self, move: str) -> Any:
        """return the synataxlly move that make the game run and current player
         change.
        """
        raise NotImplementedError("Must implement a subclass!")

    def get_instructions(self) -> str:
        """return the instructions playing the self game.
        """
        raise NotImplementedError("Must implement a subclass!")

    def is_over(self, current_state: "State") -> bool:
        """return True if the game accomplish the over requirement.
        """
        raise NotImplementedError("Must implement a subclass!")

    def is_winner(self, winner: str) -> bool:
        """return if the winner wins the game.
        """
        raise NotImplementedError("Must implement a subclass!")


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
