row_1 = ["*", "*", "*"]
row_2 = ["*", "*", "*"]
row_3 = ["*", "*", "*"]

gameboard = [row_1, row_2, row_3]
game_on = True

def x_move():
    while True:
        try:
            x_axis = int(input("Player X, please enter your desired row (1-3): ")) - 1
            if x_axis < 0 or x_axis > 2:
                raise ValueError("Number outside of range. Pick 1-3")

            y_axis = int(input("Player X, please enter your desired column (1-3): ")) - 1
            if y_axis < 0 or y_axis > 2:
                raise ValueError("Number outside of range. Pick 1-3")

            if gameboard[x_axis][y_axis] == "*":
                break
            else:
                print("Space already taken. Please try again.")
        except ValueError as e:
            print(e)

    gameboard[x_axis][y_axis] = 'X'


def o_move():
    while True:
        try:
            x_axis = int(input("Player O, please enter your desired row (1-3): ")) - 1
            if x_axis < 0 or x_axis > 2:
                raise ValueError("Number outside of range. Pick 1-3")

            y_axis = int(input("Player O, please enter your desired column (1-3): ")) - 1
            if y_axis < 0 or y_axis > 2:
                raise ValueError("Number outside of range. Pick 1-3")

            if gameboard[x_axis][y_axis] == "*":
                break
            else:
                print("Space already taken. Please try again.")
        except ValueError as e:
            print(e)

    gameboard[x_axis][y_axis] = 'O'

def check_win_conditions(player):
    win_patterns = [
        [(0, 0), (0, 1), (0, 2)],  # Top row
        [(1, 0), (1, 1), (1, 2)],  # Middle row
        [(2, 0), (2, 1), (2, 2)],  # Bottom row
        [(0, 0), (1, 0), (2, 0)],  # Left column
        [(0, 1), (1, 1), (2, 1)],  # Middle column
        [(0, 2), (1, 2), (2, 2)],  # Right column
        [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
        [(0, 2), (1, 1), (2, 0)]   # Diagonal from top-right to bottom-left
    ]
    for pattern in win_patterns:
        if all(gameboard[row][col] == player for row, col in pattern):
            return True
    return False


while game_on:
    for i in gameboard:
        print(i)
    x_move()
    if check_win_conditions("X"):
        for i in gameboard:
            print(i)
        print("X Player wins!")
        game_on = False
        break
    for i in gameboard:
        print(i)
    o_move()
    if check_win_conditions("O"):
        for i in gameboard:
            print(i)
        print("O Player Wins!")
        game_on = False
        break
