"""module: game of substract square
"""
from game import Game
from substract_state import SubstractState


class SubstractSquare(Game):
    """class of a game called SubstractSquare, the subclass of the class Game.
    ALL example cannot be provided since the initial depends on the input value.
    """
    current_state: "SubstractState"

    def __init__(self, turn: bool) -> None:
        """
        initialize the class: game of SubstractSquare, player depending on turn.
        extends Game.__init__
        """
        self.current_state = SubstractState()
        if turn:
            self.current_state.current_player = 'p1'
        else:
            self.current_state.current_player = 'p2'
        self.limit = int(input("please input a number limit:"))
        self.current_state.current_condition = self.limit

    def __str__(self) -> str:
        """
        return the string representation of SubstractSquare game with its state.
        Overrides Game.__str__
        """
        return "Welcome to game Substract square. {}".format(self.current_state)

    def __eq__(self, other: "SubstractSquare") -> bool:
        """compare if self is equvalent with other.
        Overrides game.__eq__
        """
        return type(self) == type(other) and \
            self.current_state.current_condition == \
            other.current_state.current_condition and \
            self.current_state.current_player == \
            self.current_state.current_player

    def str_to_move(self, move: str) -> int:
        """return the synataxlly move (int) that make SubstractSquare game play.
        Overrides Game.str_to_move
        """
        return int(move)

    def get_instructions(self) -> str:
        """return the instructions playing the self game.
        Overrides Game.get_instructions
        """
        return "Players take turns substracting square numbers from " \
               "number: {}. Winner is who substracting to 0.".format(self.limit)

    def is_over(self, current_state: "SubstractState") -> bool:
        """return True if the game accomplish SubstractSquare over requirement:
        substract number becomes 0
        Overrides Game.is_over
        """
        if current_state.current_condition == 0:
            return True
        return False

    def is_winner(self, winner: str) -> bool:
        """return if the winner wins the game.(who cannot substract number any
        more.)
        Overrides Game.is_over
        """
        if self.is_over(self.current_state) and \
                winner != self.current_state.current_player:
            return True
        return False


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
