from art import *
from tabulate import tabulate
from random import choice
from termcolor import colored
import sys, csv, re, os


def main():
    try:
        tprint("Tic Tac Toe", font="bulbhead")
        while True:
            print("Main Menu: ")
            print("1. Multiplayer")
            print("2. Single Player")
            print("3. Leaderboard")
            print("4. Exit")
            print("Note: Press Ctrl+C to exit at any time.")
            print()
            choice = input("Enter your choice: ")
            if choice == "1":
                multiplayer()
            elif choice == "2":
                singleplayer()
            elif choice == "3":
                print("Leaderboard: ")
                print_leaderboard()
                print()
            elif choice == "4":
                print("Exiting game...")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print()
        print("\nExiting game...")
        sys.exit()


def multiplayer():
    while True:
        p1 = input("<Player1> <Choice>: ")
        p2 = input("<Player2> <Choice>: ")
        try:
            player1, choice1 = p1.split(" ")
            player2, choice2 = p2.split(" ")
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
        if choice1 == choice2:
            print("Both players can't choose same symbol. Please try again.")
            continue
        else:
            break
    stats = get_stats()
    p1_stats = [player for player in stats if player["name"] == player1]
    p1_wins = int(p1_stats[0]["wins"]) if p1_stats else 0
    p1_loses = int(p1_stats[0]["losses"]) if p1_stats else 0
    p1_draws = int(p1_stats[0]["draws"]) if p1_stats else 0
    p2_stats = [player for player in stats if player["name"] == player2]
    p2_wins = int(p2_stats[0]["wins"]) if p2_stats else 0
    p2_loses = int(p2_stats[0]["losses"]) if p2_stats else 0
    p2_draws = int(p2_stats[0]["draws"]) if p2_stats else 0
    if choice1 == "X":
        player1 = colored(player1, "red")
        player2 = colored(player2, "blue")
    else:
        player1 = colored(player1, "blue")
        player2 = colored(player2, "red")
    players = {player1: choice1, player2: choice2}
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    boards = []
    next_player = choice([player1, player2])

    while True:
        try:
            print_board(board, next_player)
            boards.append(board)
            move = input("<row> <col>: ")
            print()
            try:
                row, col = move.split(" ")
            except ValueError:
                print("Invalid move. Try again.")
                continue
            val = players[next_player]
            if val == "X":
                val = colored(val, "red")
            else:
                val = colored(val, "blue")
            if update_board(board, val, int(row) - 1, int(col) - 1):
                winner = check_winner(board)
                if winner:
                    print_board(board, "winner")
                    print("Winner: " + next_player)
                    if next_player == player1:
                        update_stats(
                            p1_wins + 1, p1_loses, p1_draws, remove_color(next_player)
                        )
                        update_stats(
                            p2_wins, p2_loses + 1, p2_draws, remove_color(player2)
                        )
                        winner = player1
                    else:
                        update_stats(
                            p1_wins, p1_loses, p1_draws, remove_color(next_player)
                        )
                        update_stats(
                            p2_wins + 1, p2_loses, p2_draws, remove_color(player2)
                        )
                        winner = player2
                    print()
                    view_stats = input("View stats? (y/n): ")
                    if view_stats == "y":
                        if winner == player1:
                            print(
                                tabulate(
                                    [
                                        ["Name", "Wins", "Losses", "Draws"],
                                        [player1, p1_wins + 1, p1_loses, p1_draws],
                                        [player2, p2_wins, p2_loses + 1, p2_draws],
                                    ],
                                    headers="firstrow",
                                    tablefmt="github",
                                )
                            )
                        else:
                            print(
                                tabulate(
                                    [
                                        ["Name", "Wins", "Losses", "Draws"],
                                        [player1, p1_wins, p1_loses + 1, p1_draws],
                                        [player2, p2_wins + 1, p2_loses, p2_draws],
                                    ],
                                    headers="firstrow",
                                    tablefmt="github",
                                )
                            )
                    print()
                    restart = input(
                        "Restart game? Press Enter to continue or Ctrl+C to exit."
                    )
                    if restart == "":
                        board = [["", "", ""], ["", "", ""], ["", "", ""]]
                        next_player = choice([player1, player2])
                        continue
                    break
                elif all([board[i][j] != "" for i in range(3) for j in range(3)]):
                    print_board(board, "draw")
                    print("Game Draw")
                    draws = p1_draws + 1
                    update_stats(p1_wins, p1_loses, draws, player1)
                    draws = p2_draws + 1
                    update_stats(p2_wins, p2_loses, draws, player2)
                    print()
                    view_stats = input("View stats? (y/n): ")
                    if view_stats == "y":
                        print(
                            tabulate(
                                [
                                    ["Name", "Wins", "Losses", "Draws"],
                                    [player1, p1_wins, p1_loses, p1_draws + 1],
                                    [player2, p2_wins, p2_loses, p2_draws + 1],
                                ],
                                headers="firstrow",
                                tablefmt="github",
                            )
                        )
                    print()
                    restart = input(
                        "Restart game? Press Enter to continue or Ctrl+C to exit."
                    )
                    if restart == "":
                        board = [["", "", ""], ["", "", ""], ["", "", ""]]
                        next_player = choice([player1, player2])
                        continue
                    break
                next_player = player1 if next_player == player2 else player2
            else:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid move. Try again.")
            continue


def singleplayer():
    while True:
        p1 = input("<Player> <Choice>: ")
        try:
            player1, choice1 = p1.split(" ")
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
        if choice1 != "X" and choice1 != "O":
            print("Invalid choice. Please try again.")
            continue
        else:
            break
    stats = get_stats()
    p1_stats = [player for player in stats if player["name"] == player1]
    p1_wins = int(p1_stats[0]["wins"]) if p1_stats else 0
    p1_loses = int(p1_stats[0]["losses"]) if p1_stats else 0
    p1_draws = int(p1_stats[0]["draws"]) if p1_stats else 0
    p2_stats = [player for player in stats if player["name"] == "Computer"]
    p2_wins = int(p2_stats[0]["wins"]) if p2_stats else 0
    p2_loses = int(p2_stats[0]["losses"]) if p2_stats else 0
    p2_draws = int(p2_stats[0]["draws"]) if p2_stats else 0
    if choice1 == "X":
        player1 = colored(player1, "red")
        player2 = colored("Computer", "blue")
    else:
        player1 = colored(player1, "blue")
        player2 = colored("Computer", "red")
    players = {player1: choice1, player2: "O" if choice1 == "X" else "X"}
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    boards = []
    next_player = choice([player1, player2])

    while True:
        try:
            print_board(board, next_player)
            boards.append(board)
            if next_player == player1:
                move = input("<row> <col>: ")
                print()
                try:
                    row, col = move.split(" ")
                except ValueError:
                    print("Invalid move. Try again.")
                    continue
            else:
                row, col = get_computer_move(board)
                print("Computer's move: " + str(row) + " " + str(col))
                print()
            val = players[next_player]
            if val == "X":
                val = colored(val, "red")
            else:
                val = colored(val, "blue")
            if update_board(board, val, int(row) - 1, int(col) - 1):
                winner = check_winner(board)
                if winner:
                    print_board(board, "winner")
                    print("Winner: " + next_player)
                    if next_player == player1:

                        update_stats(
                            p1_wins + 1, p1_loses, p1_draws, remove_color(next_player)
                        )
                        update_stats(
                            p2_wins, p2_loses + 1, p2_draws, remove_color("Computer")
                        )
                        winner = player1
                        loser = "Computer"
                    else:
                        update_stats(
                            p1_wins, p1_loses + 1, p1_draws, remove_color(next_player)
                        )
                        update_stats(
                            p2_wins + 1, p2_loses, p2_draws, remove_color("Computer")
                        )
                        winner = "Computer"
                        loser = player1
                    print()
                    view_stats = input("View stats? (y/n): ")
                    if view_stats == "y":
                        if winner == player1:
                            print(
                                tabulate(
                                    [
                                        ["Name", "Wins", "Losses", "Draws"],
                                        [player1, p1_wins + 1, p1_loses, p1_draws],
                                        ["Computer", p2_wins, p2_loses + 1, p2_draws],
                                    ],
                                    headers="firstrow",
                                    tablefmt="github",
                                )
                            )
                        else:
                            print(
                                tabulate(
                                    [
                                        ["Name", "Wins", "Losses", "Draws"],
                                        [player1, p1_wins, p1_loses + 1, p1_draws],
                                        ["Computer", p2_wins + 1, p2_loses, p2_draws],
                                    ],
                                    headers="firstrow",
                                    tablefmt="github",
                                )
                            )
                    print()
                    restart = input(
                        "Restart game? Press Enter to continue or Ctrl+C to exit."
                    )
                    if restart == "":
                        board = [["", "", ""], ["", "", ""], ["", "", ""]]
                        next_player = choice([player1, player2])
                        continue
                    break
                elif all([board[i][j] != "" for i in range(3) for j in range(3)]):
                    print_board(board, "draw")
                    print("Game Draw")
                    draws = p1_draws + 1
                    update_stats(p1_wins, p1_loses, draws, player1)
                    draws = p2_draws + 1
                    update_stats(p1_wins, p1_loses, draws, "Computer")
                    view_stats = input("View stats? (y/n): ")
                    if view_stats == "y":
                        print(
                            tabulate(
                                [
                                    ["Name", "Wins", "Losses", "Draws"],
                                    [player1, p1_wins, p1_loses, p1_draws + 1],
                                    ["Computer", p2_wins, p2_loses, p2_draws + 1],
                                ],
                                headers="firstrow",
                                tablefmt="github",
                            )
                        )
                    restart = input(
                        "Restart game? Press Enter to continue or Ctrl+C to exit."
                    )
                    if restart == "":
                        board = [["", "", ""], ["", "", ""], ["", "", ""]]
                        next_player = choice([player1, player2])
                        continue
                    break
                next_player = player1 if next_player == player2 else player2
            else:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid move. Try again.")
            continue


def get_computer_move(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                available_moves.append((i + 1, j + 1))
    return choice(available_moves)


def print_board(board, next_player):
    table = [board[0], board[1], board[2]]
    if next_player != "winner" and next_player != "draw":
        print("Next player: " + next_player)
    print(tabulate(table, tablefmt="grid"))


def update_board(board, val, row, col):
    try:
        if board[row][col] == "":
            board[row][col] = highlight_symbol(val)
            return True
        else:
            return False
    except IndexError:
        return False


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None


def highlight_symbol(symbol):
    if symbol == "X":
        return colored(symbol, "red")
    elif symbol == "O":
        return colored(symbol, "blue")
    else:
        return symbol


def get_stats():
    if not os.path.exists("stats.csv"):
        with open("stats.csv", mode="w", newline="") as file:
            fieldnames = ["name", "wins", "losses", "draws"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    players = []
    with open("stats.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            players.append(
                {
                    "name": row["name"],
                    "wins": row["wins"],
                    "losses": row["losses"],
                    "draws": row["draws"],
                }
            )
    return players


def print_leaderboard():
    players = get_stats()
    sorted_players = sorted(
        players, key=lambda x: (-int(x["wins"]), int(x["losses"]), -int(x["draws"]))
    )
    table_data = []
    table_data.append(["Place", "Name", "Wins", "Losses", "Draws"])
    for i, player in enumerate(sorted_players):
        table_data.append(
            [i + 1, player["name"], player["wins"], player["losses"], player["draws"]]
        )
    print(tabulate(table_data, headers="firstrow", tablefmt="github"))


def update_stats(wins, loses, draws, name):
    players = get_stats()
    updated = False
    for player in players:
        if player["name"] == name:
            player["wins"] = str(wins)
            player["losses"] = str(loses)
            player["draws"] = str(draws)
            updated = True
            break
    if not updated:
        players.append(
            {"name": name, "wins": str(wins), "losses": str(loses), "draws": str(draws)}
        )
    with open("stats.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "wins", "losses", "draws"])
        writer.writeheader()
        for player in players:
            writer.writerow(player)


def remove_color(text):
    ansi_escape = re.compile(
        r"\x1B\[[0-?]*[ -/]*[@-~]"
    )  # I looked it up and the library uses ANSI codes internally so I believe this is the right re.compile
    return ansi_escape.sub("", text)


if __name__ == "__main__":
    main()
