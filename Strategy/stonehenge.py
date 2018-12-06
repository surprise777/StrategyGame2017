"""module: stonehenge game, with a class of game and a class of gamestate
"""
from typing import Any, List
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """a class representing a game called Stonehenge, a subclass of Game.

    Cannot write example since class needs input.

    state - the current state of the Stonehenge Game
    side_length - the side length og the Stonehenge grid

    """
    current_state: "StonehengeState"
    side_length: int

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize StonehengeGame, using p1_starts to find who the first
        player is.
        overrides Game.__init__.
        """
        self.side_length = int(input("Enter the side length of the board:"))
        self.current_state = StonehengeState(p1_starts, self.side_length)

    def get_instructions(self) -> str:
        """
        Return the instructions for Stonehenge Game.
        overrides Game.get_instruction.
        """
        instructions = "Welcome to the Stonehenge Game, you are going to claim"\
                       " the cell in the Stonehenge grid by turns, who claims "\
                       "at least a half ley-lines of the grid will be the "\
                       "winner!"
        return instructions

    def is_over(self, state: "StonehengeState") -> bool:
        """
        Return whether or not StonehengeGame is over at state.
        Overrides Game.is_over.
        """
        counting1 = state.current_line[0] / (3 * (self.side_length + 1))
        counting2 = state.current_line[1] / (3 * (self.side_length + 1))
        return counting2 >= 0.5 or counting1 >= 0.5

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won StonehengeGame.
        Overrides Game.is_winner.

        Precondition: player is 'p1' or 'p2'.
        """
        if self.is_over(self.current_state):
            if self.current_state.get_current_player_name() != player:
                return True
        return False

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        Overrides Game.str_to_move.
        """
        return str(string)


class StonehengeState(GameState):
    """a class representing a game state of the Stonehenge Game, a subclass
    of GameState.

    grid - the list of how stonehenge grid looks like with each specific
           elements.
    current_line - a list showed the number of two players claimed ley lines.
    """
    current_line: List[int]
    grid: List[str]

    def __init__(self, is_p1_turn: bool, grid_length: int) -> None:
        """
        Initialize StonehengeState state and set the current player based on
        is_p1_turn. Form the initial grid by given grid_length
        extends GameState.__init__
        >>> state = StonehengeState(True, 1)
        >>> state.grid
        [['@', '@'], ['@', 'A', 'B'], ['@', 'C', '@'], ['@']]
        >>> state.p1_turn
        True
        """
        GameState.__init__(self, is_p1_turn)
        self.current_line = [0, 0]
        self.grid = [['@', '@']]
        order = ord('A')
        first_num = 2
        for i in range(grid_length + 1):
            line = ['@']
            num = 0
            if i == grid_length:
                first_num -= 2
            while num < first_num:
                line.append(chr(order + num))
                num += 1
            order += num
            first_num += 1
            if i != grid_length - 1:
                line.append('@')
            self.grid.append(line)
        self.grid += [['@'] * grid_length]

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        Overrides GameState.__str__
        """

        n = len(self.grid)
        g1 = 3
        g2 = ' - '
        g3 = ' / \\'
        g4 = ' \\ /'
        graph = (2 * n - 2) * ' ' + self.grid[0][0] + g1 * ' ' + \
                self.grid[0][1] + '\n'
        graph += (2 * n - 3) * ' ' + '/' + g1 * ' ' + '/' + '\n'
        for i in range(1, n - 3):
            graph += 2 * (n - 3 - i) * ' '
            for j in range(len(self.grid[i]) - 2):
                graph += self.grid[i][j] + g2
            graph += self.grid[i][len(self.grid[i]) - 2] + g1 * ' ' + \
                     self.grid[i][len(self.grid[i]) - 1] + '\n'
            graph += (2 * (n - 3 - i) + 2) * ' ' + g3 * (i + 1) + ' /' + '\n'
        for j in range(len(self.grid[n - 3]) - 1):
            graph += self.grid[n - 3][j] + g2
        graph += self.grid[n - 3][len(self.grid[n - 3]) - 1] + '\n'
        graph += 4 * ' ' + g4 * (n - 3) + ' \\' '\n' + 2 * ' '
        for j in range(len(self.grid[n - 2]) - 2):
            graph += self.grid[n - 2][j] + g2
        graph += self.grid[n - 2][len(self.grid[n - 2]) - 2] + g1 * ' ' + \
                 self.grid[n - 2][len(self.grid[n - 2]) - 1] + '\n'
        graph += 4 * ' ' + '   \\' * (n - 3) + '\n'
        graph += 5 * ' '
        for j in range(n - 3):
            graph += g1 * ' ' + self.grid[n - 1][j]
        graph += '\n'
        return graph

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        Overrides GameState.get_possible_moves

        >>> state = StonehengeState(True, 1)
        >>> state.grid
        [['@', '@'], ['@', 'A', 'B'], ['@', 'C', '@'], ['@']]
        >>> state.get_possible_moves()
        ['A', 'B', 'C']
        """
        new_list = []
        counting1 = self.current_line[0] / (3 * (len(self.grid) - 2))
        counting2 = self.current_line[1] / (3 * (len(self.grid) - 2))
        for i in range(1, len(self.grid) - 1):
            for j in range(1, len(self.grid[i])-1):
                if self.grid[i][j].isalpha():
                    new_list.append(self.grid[i][j])
            if i == len(self.grid) - 3:
                if self.grid[i][len(self.grid[i]) - 1].isalpha():
                    new_list.append(self.grid[i][len(self.grid[i]) - 1])
        if counting1 >= 0.5 or counting2 >= 0.5:
            new_list = []
        return new_list

    def make_move(self, move: str) -> 'StonehengeState':
        """
        Return the StonehengeState that results from applying move to
        this StonehengeState.
        Overrides GameState.make_move

        >>> state = StonehengeState(True, 1)
        >>> new_state = state.make_move('A')
        >>> new_state.grid
        [['1', '@'], ['1', '1', 'B'], ['@', 'C', '@'], ['1']]
        >>> new_state.p1_turn
        False
        """
        new_state = StonehengeState(self.p1_turn, len(self.grid) - 2)
        new_state.current_line, new_state.grid = self.current_line[:], [
            [cell for cell in item] for item in self.grid]
        if not self.is_valid_move(move):
            return self
        my_pos, index, new_state.p1_turn, ley_line_dic = '1', 0, False, {}
        if not self.p1_turn:
            my_pos, index, new_state.p1_turn = '2', 1, True
        for i in range(len(new_state.grid)):
            for j in range(len(new_state.grid[i])):
                new_state.grid[
                    i][j] = my_pos if new_state.grid[
                        i][j] == move else new_state.grid[i][j]
        c1, c2, ley_line_dic['+0+0'], ley_line_dic['-2-1'] \
            = 0, 0, [], []
        ley_line_dic['+0+0'].append(new_state.grid[0][0])
        ley_line_dic['-2-1'].append(new_state.grid[-2][-1])
        for i in range(1, len(new_state.grid) - 2):
            ley_line_dic['+0+0'].append(new_state.grid[i][1])
            ley_line_dic['-2-1'].append(new_state.grid[i][i + 1])
            c1 = c1 + 1 if new_state.grid[i][1] == my_pos else c1
            c2 = c2 + 1 if new_state.grid[i][i + 1] == my_pos else c2
        if c1 >= (len(ley_line_dic['+0+0']) - 1) / 2 and new_state.grid[int(
                '+0+0'[0:2])][int('+0+0'[2:])] == '@':
            new_state.grid[int('+0+0'[0:2])][
                int('+0+0'[2:])], new_state.current_line[
                    index] = my_pos, new_state.current_line[index] + 1
        if c2 >= (len(ley_line_dic['-2-1']) - 1) / 2 and new_state.grid[int(
                '-2-1'[0:2])][int('-2-1'[2:])] == '@':
            new_state.grid[int('-2-1'[0:2])][
                int('-2-1'[2:])], new_state.current_line[
                    index] = my_pos, new_state.current_line[index] + 1
        name1, name2, c1, c2, ley_line_dic['+0+1'], ley_line_dic['-1-1'] \
            = '+0+1', '-1-1', 0, 0, [], []
        ley_line_dic['+0+1'].append(
            new_state.grid[0][1])
        ley_line_dic['-1-1'].append(
            new_state.grid[-1][-1])
        for j in range(2, len(new_state.grid) - 1):
            for i in range(j - 1, len(new_state.grid) - 2):
                ley_line_dic[name1].append(new_state.grid[i][j])
                ley_line_dic[name2].append(new_state.grid[i][i + 2 - j])
                c1 = c1 + 1 if new_state.grid[i][j] == my_pos else c1
                c2 = c2 + 1 if new_state.grid[i][i + 2 - j] == my_pos else c2
            ley_line_dic[name1].append(
                new_state.grid[len(new_state.grid) - 2][j - 1])
            ley_line_dic[name2].append(
                new_state.grid[len(new_state.grid) - 2][-j])
            c1 = c1 + 1 if new_state.grid[
                len(new_state.grid) - 2][j - 1] == my_pos else c1
            c2 = c2 + 1 if new_state.grid[
                len(new_state.grid) - 2][-j] == my_pos else c2
            if c1 >= (len(ley_line_dic[name1]) - 1) / 2 and new_state.grid[int(
                    name1[0:2])][int(name1[2:])] == '@':
                new_state.grid[
                    int(name1[0:2])][int(name1[2:])], new_state.current_line[
                        index] = my_pos, new_state.current_line[index] + 1
            if c2 >= (len(ley_line_dic[name2]) - 1) / 2 and new_state.grid[int(
                    name2[0:2])][int(name2[2:])] == '@':
                new_state.grid[
                    int(name2[0:2])][int(name2[2:])], new_state.current_line[
                        index] = my_pos, new_state.current_line[index] + 1
            if j + 1 <= len(new_state.grid) - 2:
                name1, name2 = '+' + str(j - 1) + '+' + str(j + 1), \
                               '-1' + str(-j)
                ley_line_dic[name1], ley_line_dic[name2], c1, c2 = \
                    [], [], 0, 0
                ley_line_dic[name1].append(new_state.grid[j - 1][j + 1])
                ley_line_dic[name2].append(new_state.grid[-1][-j])
        for i in range(1, len(new_state.grid) - 1):
            name3, c3 = '+' + str(i) + '+' + '0', 0
            ley_line_dic[name3] = []
            for j in range(len(new_state.grid[i]) - 1):
                ley_line_dic[name3].append(new_state.grid[i][j])
                c3 = c3 + 1 if new_state.grid[i][j] == my_pos else c3
            if i == len(new_state.grid) - 3:
                ley_line_dic[name3].append(
                    new_state.grid[i][len(new_state.grid[i]) - 1])
                c3 = c3 + 1 if new_state.grid[i][
                    len(new_state.grid[i]) - 1] == my_pos else c3
            if c3 >= (len(ley_line_dic[name3]) - 1) / 2 and new_state.grid[int(
                    name3[0:2])][int(name3[2:])] == '@':
                new_state.grid[int(name3[0:2])][int(
                    name3[2:])], new_state.current_line[
                        index] = my_pos, new_state.current_line[index] + 1
        return new_state

    def __repr__(self) -> Any:
        """
        Return a representation of this StonehengeState (which can be used for
        equality testing).
        Overrides GameState.__repr__
        """
        player = 'p2'
        if self.p1_turn:
            player = 'p1'
        return "Player {} is playing and result as below: {}".format(player,
                                                                     self.grid)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        >>> state = StonehengeState(True, 1)
        >>> state = state.make_move('A')
        >>> state.rough_outcome()
        -1
        """
        move_list = self.get_possible_moves()
        if move_list == []:
            return self.LOSE
        for item in move_list:
            new_state1 = self.make_move(item)
            if new_state1.get_possible_moves() == []:
                return self.WIN
            for item2 in new_state1.get_possible_moves():
                new_state2 = new_state1.make_move(item2)
                if new_state2.get_possible_moves() == []:
                    return self.LOSE
        return self.DRAW


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
