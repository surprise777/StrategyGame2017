"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from game import Game
from game_state import GameState

def interactive_strategy(game: Game) -> str:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Game) -> str:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(game: Game) -> str:
    """ Return a move for game by picking a move which results in a state with
        the minimax for the opponent using recursive method.
        Cannot provide examples since depend on game.
    """
    best_move = None
    move_list = game.current_state.get_possible_moves()
    best_move_list = []
    new_state = game.current_state
    for move in move_list:
        game.current_state = new_state
        new_state1 = game.current_state.make_move(move)
        score = recursive_method(game, new_state1, move) * (-1)
        best_move_list.append(score)
    if best_move_list != []:
        index = 0
        for i in range(len(best_move_list)):
            if best_move_list[i] == max(best_move_list):
                index = i
        best_move = move_list[index]
    return best_move


def iterative_minimax_strategy(game: Game) -> str:
    """ Return a move for game by picking a move which results in a state with
        the minimax for the opponent using iterative method.
        Cannot provide examples since depend on game.
    """
    best_move = None
    move_list, index1 = [], None
    for item in game.current_state.get_possible_moves():
        stack_lst, score_lst = [], []
        node = [game.current_state.make_move(item), [], None]
        stack_lst.append(node)
        while stack_lst != []:
            node = stack_lst.pop()
            if game.is_over(node[0]):
                init_state = game.current_state
                game.current_state = node[0]
                set_node_score(game, node)
                score_lst.append(node)
                game.current_state = init_state
            elif node[1] == []:
                new_state1 = node[0]
                set_node_children(new_state1, node)
                stack_lst.append(node)
                append_child_in_stack(stack_lst, node)
            else:
                get_node_score_from_children(node, score_lst)
                score_lst.append(node)
        move_list.append(score_lst[-1][2] * (-1))
    if move_list != []:
        for i in range(len(move_list)):
            if move_list[i] == max(move_list):
                index1 = i
        best_move = (game.current_state.get_possible_moves())[index1]
    return best_move


def recursive_method(game: Game, state: GameState, move: str) -> int:
    """helper function of the recursion minimax. Return the best score after
       make the move operation of the game.state.
       Cannot provide examples since depend on game.
    """
    score = -1
    score_list = []
    move = move
    if game.is_over(state):
        current_player = state.get_current_player_name()
        if current_player == 'p1':
            oppo_player = 'p2'
        else:
            oppo_player = 'p1'
        init_state = game.current_state
        game.current_state = state
        if game.is_winner(current_player):
            score = 1
        elif game.is_winner(oppo_player):
            score = -1
        else:
            score = 0
        game.current_state = init_state
    else:
        for moves in state.get_possible_moves():
            state1 = state.make_move(moves)
            new_score = - recursive_method(game, state1, moves)
            score_list.append(new_score)
        score = max(score_list)
    return score


def set_node_score(game: Game, node: list) -> None:
    """helper function of the iterative minimax.
       set the node 's score depending on who is the current winner of the
       game.
       Cannot provide examples since depend on game.
    """
    if node[0].get_current_player_name() == 'p1':
        oppo_player = 'p2'
    else:
        oppo_player = 'p1'
    if game.is_winner(node[0].get_current_player_name()):
        node[2] = 1
    elif game.is_winner(oppo_player):
        node[2] = -1
    else:
        node[2] = 0


def set_node_children(new_state1: GameState, node: list) -> None:
    """helper function of the itrative minimax.
       set the children of the node as formed [new_state1, [], None].
       Cannot provide examples since depend on GameState.
    """
    for move in new_state1.get_possible_moves():
        new_node = [new_state1.make_move(move), [], None]
        node[1].append(new_node)


def append_child_in_stack(stack_lst: list, node: list) -> None:
    """helper function of the itearative minimax.
       append all chirldren of node in the stack_lst.
       Cannot provide examples since depend on game.
    """
    for nodes in node[1]:
        stack_lst.append(nodes)


def get_node_score_from_children(node: list, score_lst: list) -> None:
    """helper function of the itearative minimax.
       get the node 's score from the node 's children 's score in score_lst.
       Cannot provide examples since depend on game.
    """
    max_score = []
    for childs in node[1]:
        for score_node in score_lst:
            if childs[0] == score_node[0]:
                max_score.append(score_node[2] * (-1))
    node[2] = max(max_score)


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
