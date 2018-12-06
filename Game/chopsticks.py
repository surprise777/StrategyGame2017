"""module: Game of Chopsticks.
"""
from game import Game
from chopsticks_state import ChopstickState


class Chopsticks(Game):
    """a class of game called Chopsticks. Subclass of Game.
    """
    current_state: "ChopstickState"

    def __init__(self, turn: bool) -> None:
        """
        initialize the class: game of Chopsticks, player depending on turn.
        extends Game.__init__
        >>> ch1 = Chopsticks(True)
        >>> ch1.current_state.current_condition
        [1, 1, 1, 1]
        >>> ch1.current_state.current_player
        'p1'
        """
        Game.__init__(self, turn)
        self.current_state = ChopstickState()
        if turn:
            self.current_state.current_player = 'p1'
        else:
            self.current_state.current_player = 'p2'
        self.current_state.current_condition = [1, 1, 1, 1]

    def __eq__(self, other: "Chopsticks") -> bool:
        """compare if self is equvalent with other.
        Overrides Game.__eq__
        """
        return type(self) == type(other) and \
            self.current_state.current_condition == \
            other.current_state.current_condition and \
            self.current_state.current_player == \
            self.current_state.current_player

    def __str__(self) -> str:
        """
        return the string representation of the Chopsticks game with its state.
        Overrides Game.__str__
        >>> ch1 = Chopsticks(True)
        >>> print(ch1)
        Welcome to game Chopsticks. now: Player 1: 1-1; Player 2: 1-1
        """
        return "Welcome to game Chopsticks. now: {}".format(self.current_state)

    def str_to_move(self, move: str) -> str:
        """return the synataxlly move (string) that make chopstick game play.
        Overrides Game.str_to_move
        >>> ch1 = Chopsticks(True)
        >>> ch1.str_to_move(10)
        '10'
        """
        return str(move)

    def get_instructions(self) -> str:
        """return the instructions how to play the self game.
        Overrides Game.get_instructions
        >>> ch1 = Chopsticks(True)
        >>> s1= "Players take turns adding nums from one of their hands to " \
               "one hands of their opponents. Loser is who first get two "\
               "hands num 5 or moduled 0."
        >>> s1 == ch1.get_instructions()
        True
        """
        return "Players take turns adding nums from one of their hands to " \
               "one hands of their opponents. Loser is who first get two "\
               "hands num 5 or moduled 0."

    def is_over(self, current_state: "ChopstickState") -> bool:
        """return True if the game accomplish chopsticks' over requirement:
           one player's two hands are dead (% 5 == 0)
        Overrides Game.is_over
        >>> ch1 = Chopsticks(True)
        >>> ch1.current_state.current_condition = [0, 0, 1, 1]
        >>> ch1.is_over(ch1.current_state)
        True
        """
        left = current_state.current_condition[0]
        right = current_state.current_condition[1]
        if current_state.current_player == 'p1':
            if left % 5 == 0 and right % 5 == 0:
                return True
        elif current_state.current_player == 'p2':
            left = current_state.current_condition[2]
            right = current_state.current_condition[3]
            if left % 5 == 0 and right % 5 == 0:
                return True
        return False

    def is_winner(self, winner: str) -> bool:
        """return if the winner wins the game.(who 's hand are not all dead)
        Overrides Game.is_over
        >>> ch1 = Chopsticks(True)
        >>> ch1.current_state.current_condition = [0, 0, 1, 1]
        >>> ch1.is_winner('p2')
        True
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
