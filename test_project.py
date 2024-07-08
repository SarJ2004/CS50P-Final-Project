from project import get_computer_move, check_winner, highlight_symbol
from termcolor import colored


def test_get_computer_move():
    # Test 1
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    move = get_computer_move(board)
    assert move in [
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    ]
    # Test 2
    board = [["X", "", ""], ["O", "X", ""], ["", "", "O"]]
    move = get_computer_move(board)
    assert move in [(1, 2), (1, 3), (2, 3), (3, 1), (3, 2)]


def test_check_winner():
    # Test 1
    board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert check_winner(board) == None
    # Test 2
    board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]
    assert check_winner(board) == "X"
    # Test 3
    board = [["X", "O", "X"], ["O", "X", "O"], ["O", "O", "O"]]
    assert check_winner(board) == "O"


def test_highlight_symbol():
    # Test 1
    assert highlight_symbol("X") == colored("X", "red")
    # Test 2
    assert highlight_symbol("O") == colored("O", "blue")
    # Test 3
    assert highlight_symbol("apple") == "apple"
