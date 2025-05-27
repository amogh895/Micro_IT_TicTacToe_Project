def printBoard(xState, OState):
    zero = 'X' if xState[0] else ('O' if OState[0] else 0)
    one = 'X' if xState[1] else ('O' if OState[1] else 1)
    two = 'X' if xState[2] else ('O' if OState[2] else 2)
    three = 'X' if xState[3] else ('O' if OState[3] else 3)
    four = 'X' if xState[4] else ('O' if OState[4] else 4)
    five = 'X' if xState[5] else ('O' if OState[5] else 5)
    six = 'X' if xState[6] else ('O' if OState[6] else 6)
    seven = 'X' if xState[7] else ('O' if OState[7] else 7)
    eight = 'X' if xState[8] else ('O' if OState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def sum3(a, b, c):
   return a + b + c

def checkWin(xState, OState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum3(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("\nCongratulations!\nX Won the match")
            return 1
        if(sum3(OState[win[0]], OState[win[1]], OState[win[2]]) == 3):
            print("\nCongratulations!\nO Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    xState = [0] * 9
    OState = [0] * 9
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe Game")
    while True:
        printBoard(xState, OState)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            if xState[value] == 0 and OState[value] == 0:
                xState[value] = 1
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            if xState[value] == 0 and OState[value] == 0:
                OState[value] = 1
            else:
                print("Invalid move. Try again.")
                continue

        cwin = checkWin(xState, OState)
        if cwin != -1:
            printBoard(xState, OState)
            print("Match over")
            break

        if sum(xState) + sum(OState) == 9:
            printBoard(xState, OState)
            print("It's a Draw!")
            break

        turn = 1 - turn
