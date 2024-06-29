import tkinter

def set_tile(row, column):
    global current_player

    if board[row][column]["text"] != "":
        return     

    board[row][column]["text"] = current_player
    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = current_player+ "'s turn"

    # check winner
    check_winner()

def check_winner():
    pass
    

def new_game():
    global turns, game_over
    turns += 1

# game setup
playerX = "X"
playerO = "O"

current_player = playerX

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

colorBlue = "#4584b6"
colorYellow = "#ffde57"
colorGray = "#343434"
colorLightGrey = "#646464"

turns = 0
game_over = False

# window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame,  text=current_player + "'s turn", font=("consolas", 20), background=colorGray, foreground="white")

label.grid(row=0, column=0, columnspan=3,  sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame,  text="", font=("Consolas", 50, "bold"), background=colorGray, foreground=colorBlue, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))

        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Restart Game", font=("Consolas", 20), background=colorGray, foreground="White", command=new_game)
button.grid(row=4,column=0, columnspan=3, sticky="we")

frame.pack()

window.mainloop()# Minor edit
# Minor edit # Minor edit
