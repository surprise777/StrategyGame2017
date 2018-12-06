"""module: strategy
"""
from random import choice
from typing import Any


def interactive_strategy(game: "Game") -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)



def random_strategy(game: "Game") -> Any:
    """
    Return a move for game randomly choosing a valid move of the game.
    Example cannot be provided since the move is choosen randomly
    """
    move = choice(game.current_state.get_possible_moves())
    return game.str_to_move(move)


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
