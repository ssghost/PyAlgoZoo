from typing import List, Tuple, Callable

def check_win(board: List[List[int]]) -> bool:
    pass

def get_state(board: List[List[int]]) -> bool:
    pass

def game_theory(board: List[List[int]], depth: int, check_win: Callable, saddle: bool) -> float:
    if check_win(board):
        return float('inf')
    elif not check_win(board):
        return -float('inf')
    elif get_state(board):
        return 0.
    
    if saddle:
        score = -float('inf')
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0: 
                    board[row][col] = 1
                    score = max(score, game_theory(board, depth + 1, False))
                    board[row][col] = 0
        return score
    else:
        score = float('inf')
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0:
                    board[row][col] = -1
                    score = min(score, game_theory(board, depth + 1, True))
                    board[row][col] = 0
        return score
    
def perform(board: List[List[int]]) -> Tuple[int]:
    score = -float('inf')
    move = (-1, -1)

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                board[row][col] = 1
                cur_score = game_theory(board, depth=0, check_win=check_win, saddle=False)
                board[row][col] = 0
                if cur_score > score:
                    score = cur_score
                    move = (row, col)

    return move