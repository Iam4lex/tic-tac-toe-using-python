import tkinter

def set_tile(row, column):
    global current_player

    if board[row][column]["text"] != "":
<<<<<<< HEAD
        return  

    if (game_over):
        return   
=======
        return     
>>>>>>> 7f4d3283505b583cfd250412e3e0b56b03a39246

    board[row][column]["text"] = current_player
    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = current_player+ "'s turn"

    # check winner
    check_winner()

def check_winner():
<<<<<<< HEAD
    global turns, game_over
    turns += 1


    # Holizontaly check 3 rows
    for row in range (3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=colorYellow)
            for column in range (3):
                board[row][column].config(foreground=colorYellow, background=colorLightGrey)
            game_over = True
            return
        
    # verticaly check 3 rows
    for column in range (3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=colorYellow)
            for row in range (3):
                board[row][column].config(foreground=colorYellow, background=colorLightGrey)
            game_over = True
            return

    # check diagonaly
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=colorYellow)
        for i in range (3):
            board[i][i].config(foreground=colorYellow, background=colorLightGrey)
        game_over = True
        return
    
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=colorYellow)
        board[0][2].config(foreground=colorYellow, background=colorLightGrey)
        board[1][1].config(foreground=colorYellow, background=colorLightGrey)
        board[2][0].config(foreground=colorYellow, background=colorLightGrey)
        game_over = True
        return
    
    # check anti-diagonaly
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=colorYellow)

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=current_player+"' turn!", foreground="White")

    for row in range(3):
        for column in range (3):
            board[row][column].config(text="", foreground=colorBlue, background=colorGray)
    
=======
    pass
    

def new_game():
    global turns, game_over
    turns += 1
>>>>>>> 7f4d3283505b583cfd250412e3e0b56b03a39246

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
<<<<<<< HEAD
colorYellow = "greenyellow"
=======
colorYellow = "#ffde57"
>>>>>>> 7f4d3283505b583cfd250412e3e0b56b03a39246
colorGray = "#343434"
colorLightGrey = "#646464"

turns = 0
game_over = False

# window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
<<<<<<< HEAD
window.resizable(True,True)
=======
window.resizable(False,False)
>>>>>>> 7f4d3283505b583cfd250412e3e0b56b03a39246

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
