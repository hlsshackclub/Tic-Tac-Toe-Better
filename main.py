import tkinter as tk

import gameLogic

root = tk.Tk()
root.title("TicTacToe")
root.resizable(False, False)

buttons = []

buttonImages = {
    "X": tk.PhotoImage(file="X.png"),
    "O": tk.PhotoImage(file="O.png"),
    "_": tk.PhotoImage(file="_.png"),
}

title = tk.Label(root, text="TicTacToe", font=("Helvetica", 32))
title.pack(side="top")

buttonFrame = tk.Frame(root)
buttonFrame.pack(side="bottom")

for y in range(3):
    buttons.append([])
    for x in range(3):
        buttons[y].append(
            tk.Button(
                buttonFrame,
                image=buttonImages["_"],
                command=lambda x=x, y=y: buttonClicked(x, y),
            )
        )
        buttons[y][x].grid(row=y, column=x)


def resetButtons():
    global buttons

    for y in range(3):
        buttons.append([])
        for x in range(3):
            buttons[y][x].configure(
                command=lambda x=x, y=y: buttonClicked(x, y),
                bg="white",
                activebackground="white",
                relief="raised",
                image=buttonImages["_"],
            )


def updateButtons():
    global buttons

    for y in range(3):
        buttons.append([])
        for x in range(3):
            buttons[y][x].configure(image=buttonImages[gameLogic.board[y][x]])


winFGColors = {"X": "#ff5959", "O": "#5980ff"}
winBGColors = {"X": "#ffa2a2", "O": "#a2b8ff"}


def endGame():
    global buttons

    for y in range(3):
        buttons.append([])
        for x in range(3):
            buttons[y][x].configure(relief="sunken", command=0)

    for i in gameLogic.winningSquares:
        buttons[i[0]][i[1]].configure(
            bg=winBGColors[gameLogic.winner],
            activebackground=winBGColors[gameLogic.winner],
        )


def buttonClicked(x, y):
    global buttons, root

    gameLogic.makeMove(x, y)
    buttons[y][x].configure(relief="sunken", command=0)
    updateButtons()

    if gameLogic.winner is not None:
        endGame()

        def quit():
            endWindow.destroy()
            root.destroy()

        def playAgain():
            resetButtons()
            gameLogic.reset()
            endWindow.destroy()

        endWindow = tk.Tk()
        endWindow.geometry("256x94")
        endWindow.protocol("WM_DELETE_WINDOW", playAgain)
        endWindow.resizable(False, False)

        bottomframe = tk.Frame(endWindow, bg="white")
        bottomframe.pack(side="bottom")

        playAgainButton = tk.Button(
            bottomframe, text="Play again", font=("Helvetica", 16), command=playAgain
        )
        playAgainButton.pack(side="left")

        quitButton = tk.Button(
            bottomframe, text="Quit", font=("Helvetica", 16), command=quit
        )
        quitButton.pack(side="right")

        winText = tk.Text(endWindow, font=("Helvetica", 32))
        winText.tag_configure("X", foreground=winFGColors["X"])
        winText.tag_configure("O", foreground=winFGColors["O"])
        if gameLogic.winner == "Draw":
            winText.insert("end", "Draw!")
        else:
            winText.insert("end", f"{gameLogic.winner}", gameLogic.winner)
            winText.insert("end", " wins!")
        winText.tag_configure("center", justify="center")
        winText.tag_add("center", "1.0", "end")
        winText.configure(state="disabled")

        winText.pack()

        endWindow.withdraw()
        endWindow.update_idletasks()
        x = (root.winfo_screenwidth() - endWindow.winfo_width()) / 2
        y = (root.winfo_screenheight() - endWindow.winfo_height()) / 2
        endWindow.geometry("+%d+%d" % (x, y))
        endWindow.deiconify()


root.withdraw()
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()

root.mainloop()
