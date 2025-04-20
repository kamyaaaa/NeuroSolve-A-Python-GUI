import tkinter as tk
from tkinter import messagebox

# Initialize window
root = tk.Tk()
root.title("🎮 Tic Tac Toe - Stylish UI")

# Center the window on screen
window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (window_width // 2)
y_pos = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
root.configure(bg="#f0f2f5")

# Game state
board = [""] * 9
current_player = ["X"]
winning_indices = []

# Styles
btn_font = ("Helvetica", 24, "bold")
btn_width = 6
btn_height = 2
color_map = {"X": "#007BFF", "O": "#28A745"}  # Blue for X, Green for O

def check_winner():
    global winning_indices
    combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for a, b, c in combos:
        if board[a] == board[b] == board[c] and board[a] != "":
            winning_indices = [a, b, c]
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def handle_click(index):
    if board[index] == "" and not check_winner():
        board[index] = current_player[0]
        buttons[index].config(text=current_player[0], fg=color_map[current_player[0]], state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                for idx in winning_indices:
                    buttons[idx].config(bg="#ffc107")  # Yellow highlight
                messagebox.showinfo("Game Over", f"🎉 Player {winner} Wins!")
            disable_all_buttons()
        else:
            current_player[0] = "O" if current_player[0] == "X" else "X"
            turn_label.config(text=f"Player {current_player[0]}'s Turn", fg=color_map[current_player[0]])

def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def reset_game():
    global winning_indices
    for i in range(9):
        board[i] = ""
        buttons[i].config(text="", bg="white", state="normal")
    current_player[0] = "X"
    winning_indices = []
    turn_label.config(text="Player X's Turn", fg=color_map["X"])

# Header label
turn_label = tk.Label(root, text="Player X's Turn", font=("Arial", 16, "bold"), bg="#f0f2f5", fg=color_map["X"])
turn_label.pack(pady=20)

# Frame for grid
grid_frame = tk.Frame(root, bg="#f0f2f5")
grid_frame.pack()

# Game buttons
buttons = []
for i in range(9):
    btn = tk.Button(grid_frame, text="", width=btn_width, height=btn_height, font=btn_font,
                    bg="white", command=lambda i=i: handle_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Reset button
reset_button = tk.Button(root, text="🔁 Reset Game", font=("Arial", 12, "bold"),
                         bg="#6c757d", fg="white", command=reset_game)
reset_button.pack(pady=20)

root.mainloop()