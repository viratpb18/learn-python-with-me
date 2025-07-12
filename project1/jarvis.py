import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe - Interactive")

player1_name = tk.StringVar()
player2_name = tk.StringVar()
current_player = "X"
scores = {"X": 0, "O": 0}

buttons = [[None for _ in range(3)] for _ in range(3)]

def start_game():
    global current_player
    current_player = "X"
    update_status()
    name_frame.pack_forget()
    board_frame.pack()
    control_frame.pack()

def update_status():
    status_label.config(
        text=f"{player1_name.get() if current_player == 'X' else player2_name.get()}'s Turn ({current_player})")

def check_winner():
    for i in range(3):
        # Rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            highlight([buttons[i][0], buttons[i][1], buttons[i][2]])
            return True
        # Columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            highlight([buttons[0][i], buttons[1][i], buttons[2][i]])
            return True
    # Diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight([buttons[0][0], buttons[1][1], buttons[2][2]])
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight([buttons[0][2], buttons[1][1], buttons[2][0]])
        return True
    return False

def highlight(cells):
    for btn in cells:
        btn.config(bg="lightgreen")

def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def on_click(i, j):
    global current_player
    if buttons[i][j]["text"] == "":
        buttons[i][j]["text"] = current_player
        buttons[i][j].config(disabledforeground="black")
        if check_winner():
            scores[current_player] += 1
            update_scoreboard()
            messagebox.showinfo("Game Over", f"{player1_name.get() if current_player == 'X' else player2_name.get()} Wins!")
            reset_board()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            update_status()

def update_scoreboard():
    score_label.config(
        text=f"{player1_name.get()} (X): {scores['X']}     {player2_name.get()} (O): {scores['O']}")

def reset_board():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn.config(text="", state="normal", bg="SystemButtonFace")
    update_status()

def quit_game():
    root.quit()

# Name entry frame
name_frame = tk.Frame(root)
tk.Label(name_frame, text="Player 1 (X): ").grid(row=0, column=0)
tk.Entry(name_frame, textvariable=player1_name).grid(row=0, column=1)
tk.Label(name_frame, text="Player 2 (O): ").grid(row=1, column=0)
tk.Entry(name_frame, textvariable=player2_name).grid(row=1, column=1)
tk.Button(name_frame, text="Start Game", command=start_game).grid(row=2, column=0, columnspan=2, pady=10)
name_frame.pack(pady=20)

# Board frame
board_frame = tk.Frame(root)
for i in range(3):
    for j in range(3):
        btn = tk.Button(board_frame, text="", width=10, height=4,
                        font=("Arial", 20), command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

# Status & controls
control_frame = tk.Frame(root)
status_label = tk.Label(control_frame, text="Waiting for players...", font=("Arial", 14))
status_label.pack(pady=5)

score_label = tk.Label(control_frame, text="", font=("Arial", 12))
score_label.pack(pady=5)

tk.Button(control_frame, text="Reset Board", command=reset_board).pack(side="left", padx=10)
tk.Button(control_frame, text="Quit", command=quit_game).pack(side="right", padx=10)

root.mainloop()
